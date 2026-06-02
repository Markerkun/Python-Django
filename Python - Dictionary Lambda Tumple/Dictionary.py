student = {
    "name": "Тарас Бубля",
    "age": 19,
    "grade": 52,
}

print(student)
print(student["name"])
print(student.get("name"))
#########
student["email"] = "TBublia@gmail.com"

print(student)
###############
del student["grade"]

print(student)
###############
for key in student:
    print(f"{key}: {student[key]}")


