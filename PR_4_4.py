marks=float(input("Enter the marks of the student: "))
if marks >= 90:
    grade = 'A'
elif marks >=80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
elif marks >= 50:
    grade = 'E'
else:
    grade = 'F'
    
print("The student grade is:", grade)