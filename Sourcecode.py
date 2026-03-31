# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("student-mat.csv", sep=';')

# Select columns (rename G1 → M1, G2 → M2)
df = df[["studytime", "absences", "G1", "G2", "G3"]]
df = df.rename(columns={"G1": "M1", "G2": "M2"})

# Features and target
X = df[["studytime", "absences", "M1", "M2"]]
y = df["G3"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# ===== USER INPUT =====
print("\nEnter student details:")

studytime = int(input("Study time (1-8): "))
absences = int(input("Number of absences: "))
M1 = int(input("Marks in M1: "))
M2 = int(input("Marks in M2: "))

# Predict final grade
prediction = model.predict([[studytime, absences, M1, M2]])
final_grade = round(prediction[0], 2)

print("\nPredicted Final Marks:", final_grade)

# ===== PASS / FAIL =====
if final_grade >= 33:
    print("Result: PASS ✅")
else:
    print("Result: FAIL ❌")

# ===== GRADE SYSTEM =====
if final_grade >= 90:
    print("Grade: A (Excellent 🌟)")
elif final_grade >= 75:
    print("Grade: B (Very Good 👍)")
elif final_grade >= 55:
    print("Grade: C (Good 🙂)")
elif final_grade >= 33:
    print("Grade: D (Average 😐)")
else:
    print("Grade: F (Fail ⚠️)")
