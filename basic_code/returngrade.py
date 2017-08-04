#Write a function which is given an exam mark, and it returns a string — the grade for that mark

marks = float(input("Enter your marks: "))
def grade(marks):
    if marks >= 75:
        return "First"
    elif marks < 75 and marks >= 70:
        return "Upper Second"
    elif marks < 70 and marks >= 60:
        return "Second"
    elif marks < 60 and marks >= 50:
        return "Third"
    elif marks < 50 and marks >= 45:
        return "F1 Supp"
    elif marks <45 and marks >= 40:
        return "f2"
    elif marks< 40:
        return "f3"
    else:
        return "Invaild marks"

print("Your marks is",marks,"and your grade is",grade(marks))
