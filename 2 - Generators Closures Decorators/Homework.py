#1
#Створіть функцію, яка повертає всі непарні числа в діапазоні.
#Функція приймає початок і кінець діапазону як параметри. 
#Використовуйте механізм генераторів усередині функції.
def odd_numbers_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

print(list(odd_numbers_generator(1, 10)))

#2
#Створіть функцію, яка повертає всі значення зі списку, що не перебувають у діапазоні, зазначеному користувачем. 
#Функція приймає список, початок і кінець діапазону як параметри. 
#Використовуйте механізм генераторів усередині функції.
def out_of_range_generator(lst, start, end):
    for num in lst:
        if num < start or num > end:
            yield num
ma_list = out_of_range_generator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 7)

print(list(ma_list))

#3
#Для виконання цього завдання обов'язково використовуйте механізм функцій вищого порядку (higher order functions). 
#Створіть функцію, що відображає лінію (горизонтальну або вертикальну) з використанням символу, зазначеного користувачем. 
#Користувач визначає символ і яку лінію відображати.
def horizontal_line(symbol):
    print(symbol * 10)

def vertical_line(symbol):
    for _ in range(5):
        print(symbol)

def show_line(symbol, function_to_call):
    function_to_call(symbol)

show_line('*', horizontal_line)
show_line('|', vertical_line)

#4
#Створіть функцію, що повертає список з усіма парними числами, від 0 до 100000.
#Використовуючи механізм декораторів, порахуйте скільки секунд знадобилося для обчислення всіх чисел. 
#Відобразіть на екран кількість секунд і всі парні числа від 0 до 100000.
import time

def timer_decorator(func):
    def wrapper(start, end):
        start_time = time.time()
        result = func(start, end)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання: {execution_time:.6f} секунд\n")
        return result
    return wrapper

@timer_decorator
def get_even_numbers(start, end):
    evens = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            evens.append(num)
    return evens

all_evens = get_even_numbers(20, 200)
print(f"Знайдено чисел: {len(all_evens)}")


