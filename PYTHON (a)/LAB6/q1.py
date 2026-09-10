import numpy as np


marks = np.array([
    [85, 78, 90],
    [72, 88, 76],
    [95, 91, 89],
    [68, 75, 80],
    [88, 92, 85],
    [76, 81, 79],
    [90, 85, 94],
    [65, 70, 72],
    [82, 79, 88],
    [91, 87, 93]
])

print("1. Number of students:", marks.shape[0])

print("2. Number of subjects:", marks.shape[1])

print("3. Marks of 5th student:", marks[4])


print("4. Mathematics marks:", marks[:, 0])

print("5. Average marks in each subject:", np.mean(marks, axis=0))


print("6. Highest mark in each subject:", np.max(marks, axis=0))


print("7. Lowest mark in each subject:", np.min(marks, axis=0))

student_average = np.mean(marks, axis=1)
print("8. Average marks of each student:", student_average)

highest_student = np.argmax(student_average)

print("9. Student with highest average: Student", highest_student + 1)
print("   Highest average:", student_average[highest_student])