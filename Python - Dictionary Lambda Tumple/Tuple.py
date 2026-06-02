Tuple = (52, 67, 69)
print(Tuple)
print(type(Tuple))
print(Tuple[0])

try:
    Tuple[0] = 100 #Неможна змінювати елементи кортежу
except TypeError as e:
    print("Error:", e)

print(f"Кількість елементів у кортежі: {len(Tuple)}")

for i in Tuple:
    print(i)
print()
i=0
while i < len(Tuple):
    print(f"Tuple[{i}]={Tuple[i]}")
    i += 1