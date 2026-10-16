from sklearn.linear_model import LogisticRegression

# Sample training data
X = [
    [1, 0],
    [2, 0],
    [3, 1],
    [4, 1],
    [5, 1]
]

# 0 = Low Risk
# 1 = High Risk
y = [0, 0, 0, 1, 1]

# Create ML model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Test data
new_person = [[4, 1]]

# Predict
prediction = model.predict(new_person)

print("ML Model Started")

if prediction[0] == 1:
    print("Prediction: High Risk")
else:
    print("Prediction: Low Risk")

print("ML Model Completed")