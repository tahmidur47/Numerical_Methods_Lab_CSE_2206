'''
Write a Python program to calculate a student's grade based on their marks.
 The program should:
 Take the student's marks (0–100) as input.
 Use conditional statements to determine the grade according to the following rules:
 a. 90–100: GradeA
 b. 80–89: Grade B
 c. 70–79: Grade C
 d. 60–69: Grade D
 e. Below 60: Grade F
 Print the grade.

'''


marks = int(input("Enter marks: "))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks <= 89:
    print("Grade B")
elif marks >= 70 and marks <= 79:
    print("Grade C")
elif marks >= 60 and marks <= 69:
    print("Grade D")
else:
    print("Grade F")
