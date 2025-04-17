# GradeBook Program
# You are a student and you are trying to organize your subjects and grades using Python.
# Let’s explore what we’ve learned about lists to organize your subjects and scores.

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

gradebook[-1][1] = gradebook[-1][1] + 5

for subject_grade in gradebook:
    if subject_grade[0] == "poetry":
        subject_grade.remove(85)
        break

for subject_grade in gradebook:
    if subject_grade[0] == "poetry":
        subject_grade.append("Pass")
        break

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
