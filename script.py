last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = zip(subjects, grades)

print(list(gradebook))

subjects.append('computer science')
grades.append(100)

gradebook = list(zip(subjects, grades))

gradebook.append(("visual arts", 93))

full_gradebook = gradebook + last_semester_gradebook

print(list(full_gradebook))

