# Student-Performance-Predictor:-
What the project does:-
The Student Performance Predictor is a Python-based machine learning project that predicts a student’s final marks based on their study time, absences, and internal exam scores (M1 and M2). The program also determines if the student passes or fails and assigns a grade (A–F) according to the predicted marks. This project is useful for educators or students who want to estimate academic performance and identify students at risk.

Features:-
Predicts final marks using Linear Regression
Takes user inputs:
Study time (1–8 hours/week)
Number of absences
Marks in M1 ( Exam 1)
Marks in M2 (Exam 2)
Determines Pass/Fail using a limit of 33 marks.
Grades assign based on predicted marks:
A ≥ 90 → Excellent
B 75–89 → Very Good
C 55–74 → Good
D 33–54 → Pass
F < 33 → Fail

Technologies used:-
Python 3.X
pandas for data manupulation and analysis
Sklearn for machine learning algorithm and preorossesing

Project Setup:-
Follow this steps to set the project on your computer: 1.Download the project files
Clone repository using Git:
git clone
Or download the ZIP file and extract it
2.Install Python
Make sure Python version 3.7 or higher is installed
check by running:
python --version
3.Install required Python libraries
Open terminal or command gives rise in the project folder and run:
pip install pandas scikit-learn
4.Place dataset in the project folder
Ensure student-mat.csv is in the same folder as student_predictor.py.
5.Run the program
in the terminal run:
python student_predictor.py
Follow gives rise to enter student details.
6.View output
The program will show predicted final marks, Pass/Fail status, and grade.

How to Use the Student Performance Predictor:-
1.Run the program
Open a terminal/command prompt in the project folder and type:
python student_predictor.py
2.Enter student details when prompted
Study time (hours per week, 1–8)
Number of absences
Marks in M1 (first internal exam)
Marks in M2 (second internal exam)
3.View the results
The program will display:
Predicted final marks (G3)
Pass/Fail status
Grade (A–F)
4.Interpret the output
Grades indicate performance:
A: Excellent ,B: Very Good ,C: Good ,D: Average (Pass) ,F: Fail

Devloped by
Name :Rishabh Nambiar
Reg no : 25BAC10017

