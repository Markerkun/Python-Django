mysquart = lambda x: x * x

print(mysquart(11))

#########

def square(x):
    return x * x

print(square(12))

students = [
    {"name": "Тарас Бубля", "age": 19},
    {"name": "Олександр Петров", "age": 18},
    {"name": "Марія Іванова", "age": 20},
]
#Мутація - зміна об'єкта, який вже існує 

students.sort(key=lambda student: student["age"])
print(students)
##################################

sorted_students = sorted(students, key=lambda student: student["age"])
print(sorted_students)

print(type(students[0]))