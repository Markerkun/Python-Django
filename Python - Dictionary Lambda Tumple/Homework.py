Tuple1 = (31, 52, 83, 64)
Tuple2 = (31, 53, 64, 86)
Tuple3 = (64, 86, 31, 92)

#1: Маємо три кортежі цілих чисел. Знайдіть елементи, які є у всіх кортежах.
def FindSameNum(Tuple1, Tuple2, Tuple3):
    SameNum = []
    for i in Tuple1:
        if i in Tuple2 and i in Tuple3:
            SameNum.append(i)
    for i in Tuple2:
        if i in Tuple1 and i in Tuple3 and i not in SameNum:
            SameNum.append(i)
    for i in Tuple3:
        if i in Tuple1 and i in Tuple2 and i not in SameNum:
            SameNum.append(i)
    return SameNum

#2: Маємо три кортежі цілих чисел. Знайдіть елементи, які унікальні для кожного списку.
def FindUniqNum(Tuple1, Tuple2, Tuple3):
    UniqNum = []
    for i in Tuple1:
        if i not in Tuple2 and i not in Tuple3:
            UniqNum.append(i)
    for i in Tuple2:
        if i not in Tuple1 and i not in Tuple3:
            UniqNum.append(i)
    for i in Tuple3:
        if i not in Tuple1 and i not in Tuple2:
            UniqNum.append(i)
    return UniqNum

print(f"Унікальні числа: {FindUniqNum(Tuple1, Tuple2, Tuple3)}")

#3: Маємо три кортежі цілих чисел. Знайдіть елементи, які є в кожному з кортежів і знаходяться в кожному

def FindSameNumInEach(Tuple1, Tuple2, Tuple3):
    SameNumInEach = []
    for i in Tuple1:
        if i in Tuple2 and i in Tuple3:
            SameNumInEach.append(i)
    for i in Tuple2:
        if i in Tuple1 and i in Tuple3 and i not in SameNumInEach:
            SameNumInEach.append(i)
    for i in Tuple3:
        if i in Tuple1 and i in Tuple2 and i not in SameNumInEach:
            SameNumInEach.append(i)
    return SameNumInEach
