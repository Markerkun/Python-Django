#1
#Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини, ціну. 
#Реалізуйте методи класу для введення-виведення даних та інших операцій

class Car:
    def __init__(self, model, year, manufacturer, volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.volume = volume
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year}) - {self.color}, {self.volume}L, ${self.price}"
    
    def input_data(self):
        self.model = input("Введіть модель: ")
        self.year = int(input("Введіть рік випуску: "))
        self.manufacturer = input("Введіть виробника: ")
        self.volume = float(input("Введіть об'єм двигуна (в літрах): "))
        self.color = input("Введіть колір машини: ")
        self.price = float(input("Введіть ціну: "))
        
    def update_price(self, new_price):
        self.price = new_price
        print(f"Ціна на {self.model} тепер становить: ${self.price}")

    
car1 = Car("Model S", 2020, "Tesla", 0.0, "Red", 79999)
print(car1)
car2 = Car("", 0, "", 0.0, "", 0.0)
car2.input_data()
print(car2)

#2
#Реалізуйте клас «Книга». Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну.
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}) - {self.genre}, published by {self.publisher}, priced at ${self.price}"
    
    def input_data(self):
        self.title = input("Введіть назву книги: ")
        self.year = int(input("Введіть рік видання: "))
        self.publisher = input("Введіть видавця: ")
        self.genre = input("Введіть жанр: ")
        self.author = input("Введіть автора: ")
        self.price = float(input("Введіть ціну: "))
        
    def apply_discount(self, percentage):
        if 0 < percentage <= 100:
            self.price -= self.price * (percentage / 100)
            print(f"\nЗастосовано знижку {percentage}%. Нова ціна: {self.price:.2f} грн")
        else:
            print("Некоректний відсоток знижки.")

        
book1 = Book("The Great Gatsby", 1925, "Scribner", "Novel", "F. Scott Fitzgerald", 10.99)
print(book1)
book2 = Book("", 0, "", "", "", 0.0)
book2.input_data()
print(book2)

#3
#Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.
#Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"{self.name} in {self.city}, {self.country} (Opened: {self.opening_date}) - Capacity: {self.capacity}"
    
    def input_data(self):
        self.name = input("Введіть назву стадіону: ")
        self.opening_date = input("Введіть дату відкриття (ДД.ММ.РРРР): ")
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.capacity = int(input("Введіть місткість: "))

stadium1 = Stadium("Wembley Stadium", "09.03.2007", "UK", "London", 90000)
print(stadium1)
stadium2 = Stadium("", "", "", "", 0)
stadium2.input_data()
print(stadium2)