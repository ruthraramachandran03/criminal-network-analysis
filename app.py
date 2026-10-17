import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# PAGE SETTINGS
st.set_page_config(
    page_title="AI Network Intelligence",
    page_icon="🔷",
    layout="wide"
)

# CYBERSECURITY DESIGN
st.markdown("""
<style>
.stApp {
    background-color: #050b18;
    color: #e0f2fe;
}

header[data-testid="stHeader"] {
    background-color: transparent;
}

.block-container {
    padding-top: 2rem;
}

h1 {
    color: #22d3ee !important;
    text-shadow: 0 0 15px #0891b2;
}

h2, h3 {
    color: #67e8f9 !important;
}

p, label {
    color: #dbeafe;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0c1e36, #020817);
    border-right: 1px solid #164e80;
}

div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #102b49, #081629);
    border: 1px solid #087cae;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 0 12px #0891b220;
}

div[data-testid="stMetricValue"] {
    color: #22d3ee;
}

div[data-testid="stMetricLabel"] {
    color: #bfdbfe;
}

.stButton button {
    background: linear-gradient(90deg, #075985, #0891b2);
    color: white;
    border: 1px solid #22d3ee;
    border-radius: 8px;
}

hr {
    border-color: #164e80;
}
</style>
""", unsafe_allow_html=True)


# SAMPLE DATA
persons = pd.DataFrame({
    "Person ID": [
        "P001", "P002", "P003", "P004",
        "P005", "P006", "P007", "P008"
    ],
    "Name": [
        "Person_A", "Person_B", "Person_C", "Person_D",
        "Person_E", "Person_F", "Person_G", "Person_H"
    ],
    "Age": [32, 41, 29, 35, 38, 27, 45, 31]
})

connections = [
    ("P001", "P003"),
    ("P002", "P003"),
    ("P002", "P004"),
    ("P004", "P005"),
    ("P005", "P006"),
    ("P006", "P007"),
    ("P007", "P008")
]

G = nx.Graph()
G.add_nodes_from(persons["Person ID"].tolist())
G.add_edges_from(connections)


# SIDEBAR
with st.sidebar:
    st.markdown("# 🔷 CYBER INTEL")
    st.caption("AI NETWORK INTELLIGENCE")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "Network Analysis",
            "Person Records",
            "About Project"
        ]
    )

    st.divider()
    st.success("System Online")
    st.info("Sample Dataset Active")


# HEADER
st.markdown(
    "<p style='letter-spacing:3px;color:#22d3ee'>"
    "INTELLIGENCE / NETWORK OPERATIONS</p>",
    unsafe_allow_html=True
)

st.title("AI-POWERED")
st.header("CRIMINAL NETWORK ANALYSIS SYSTEM")

st.caption(
    "Connecting Data • Revealing Patterns • Exploring Relationships"
)

st.divider()


# DASHBOARD PAGE
if page == "Dashboard":

    st.subheader("◈ NETWORK OVERVIEW")

    c1, c2, c3 = st.columns(3)

    c1.metric("TOTAL PERSONS", len(persons))
    c2.metric("PHONE RECORDS", 8)
    c3.metric("VEHICLES", 8)

    c4, c5, c6 = st.columns(3)

    c4.metric("LOCATIONS", 8)
    c5.metric("ORGANIZATIONS", 8)
    c6.metric("TRANSACTIONS", 8)

    st.divider()

    left, right = st.columns([2, 1])

    # NETWORK GRAPH
    with left:
        st.subheader("◈ NETWORK CONNECTION MAP")

        fig, ax = plt.subplots(figsize=(9, 6))

        fig.patch.set_facecolor("#071426")
        ax.set_facecolor("#071426")

        pos = nx.spring_layout(G, seed=42)

        nx.draw_networkx_edges(
            G,
            pos,
            ax=ax,
            edge_color="#0891b2",
            width=2
        )

        nx.draw_networkx_nodes(
            G,
            pos,
            ax=ax,
            node_color="#22d3ee",
            node_size=1400,
            edgecolors="#a5f3fc",
            linewidths=2
        )

        nx.draw_networkx_labels(
            G,
            pos,
            ax=ax,
            font_color="#031525",
            font_size=9,
            font_weight="bold"
        )

        ax.axis("off")

        st.pyplot(fig)
        plt.close(fig)

        st.caption(
            "Fictional sample relationships. Connections do not prove criminal activity."
        )

    # CONNECTED PERSONS
    with right:
        st.subheader("◈ TOP CONNECTIONS")

        ranking = pd.DataFrame([
            {
                "Person ID": person,
                "Connections": G.degree[person]
            }
            for person in G.nodes()
        ])

        ranking = ranking.sort_values(
            by="Connections",
            ascending=False
        )

        st.dataframe(
            ranking,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("◈ ENTITY DISTRIBUTION")

        entity_data = pd.DataFrame({
            "Entity": [
                "Persons",
                "Phones",
                "Vehicles",
                "Locations",
                "Organizations",
                "Transactions"
            ],
            "Count": [8, 8, 8, 8, 8, 8]
        })

        fig2, ax2 = plt.subplots(figsize=(6, 4))

        fig2.patch.set_facecolor("#071426")
        ax2.set_facecolor("#071426")

        ax2.pie(
            entity_data["Count"],
            labels=entity_data["Entity"],
            autopct="%1.0f%%",
            startangle=90,
            textprops={"color": "white"},
            colors=[
                "#22d3ee",
                "#34d399",
                "#fbbf24",
                "#a78bfa",
                "#f472b6",
                "#60a5fa"
            ]
        )

        st.pyplot(fig2)
        plt.close(fig2)

    st.divider()

    st.subheader("◈ PERSON CONNECTION DETAILS")

    details = pd.DataFrame([
        {
            "Person ID": person,
            "Direct Connections": G.degree[person]
        }
        for person in sorted(G.nodes())
    ])

    st.dataframe(
        details,
        use_container_width=True,
        hide_index=True
    )


# NETWORK ANALYSIS PAGE
elif page == "Network Analysis":

    st.subheader("◈ NETWORK ANALYSIS")

    selected_person = st.selectbox(
        "Select Person ID",
        sorted(G.nodes())
    )

    connected_people = list(G.neighbors(selected_person))

    st.metric(
        "DIRECT CONNECTIONS",
        len(connected_people)
    )

    if connected_people:
        st.write("### Connected Persons")

        for person in connected_people:
            st.write("🔹", person)
    else:
        st.info("No direct connections found.")


# PERSON RECORDS PAGE
elif page == "Person Records":

    st
