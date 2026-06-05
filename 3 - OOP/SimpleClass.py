class Car:
    def drive(this): #Without "this" doesn't work
        print("Wroooom!!")

audi = Car()
audi.drive()

print()

class Animal:
    def speak(this):
        print("Roooaaar!!")

class MiniPig(Animal): #Imitation
    def speak(this):
        print("Oink-oink!")

class Cat(Animal):
    def speak(this):
        print("Meoow")


miniPig = MiniPig()
cat = Cat()

miniPig.speak()
cat.speak()

print()

#List of anonim objects
myAnimals = [MiniPig(), Cat()]

for a in myAnimals:
    a.speak()

print()

def talk(obj):
    obj.speak()

talk(MiniPig())
talk(Cat())    