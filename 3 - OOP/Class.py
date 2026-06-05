class Student:
    #Конструктор
    #self або this обов'язкові
    def __init__(self, name):
        #name is public
        self.name = name
        #age is protected, because of "_"
        self._age = 18
        #Hobby is private, because of double "_"
        self.__hobby = "Hobby horsing"

    #ToString
    def __str__(self):
        return f"Student name: {self.name}, age: {self._age}, hobby: {self.__hobby}"
    
    def getHobby(self):
        return self.__hobby

Taras = Student("Taras Bublia")

print("Name =", Taras.name)
print("Age = ", Taras._age)
#print("Hobby = ", Taras.__hobby)   #Cannot access
print(Taras)
print("Hobby = ", Taras.getHobby())