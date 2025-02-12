# class Person:
#     def __init__(self, name, fam):
#         self.name = name
#         self.fam = fam
#
#     def say_hi(self):
#         print("Hello")
#
# class Pupil(Person):
#     pass
#
# class Student(Person):
#     pass
#
# class Teacher(Person):
#     pass
#
# p = Pupil("P", "P")
# s = Student("S", "S")
# t = Teacher("T", "T")
#
# p.say_hi()
# s.say_hi()



# class Swim:
#     def swim(self):
#         print("Men suzushni bimalan")
#
# class English:
#     def speak(self):
#         print("Ingiliz tilida gapiraman")
#
# class Math:
#     def slove(self):
#         print("Misol ishlayman")
#
# class Student(English,Math,Swim):
#     pass



# class Person:
#     def __init__(self, name, fam):
#         self.name = name
#         self.fam = fam
#     def hi(self):
#         print("Hello")
#
# class English(Person):
#     pass
#
# class Uzbek(Person):
#     def hi(self):
#         print("Assalomu alaykum")
#
#
# u = Uzbek("a", "f")
# u.hi()
# e = English("a", "f")
# e.hi()



# class Animal:
#     def __init__(self, name):
#         self.name  = name
#     def sound(self):
#         print("Sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("wow - wow")
#
# class Cat(Animal):
#     def sound(self):
#         print("Miaou")
#
# d = Dog("A")
# d.sound()
#
# c = Cat("M")
# c.sound()


# class Car:
#     def __init__(self, leng):
#         self.leng = leng
#
#     def model(self):
#         print("Lada")
#
# class Ru(Car):
#     pass
#
# class Uzb(Car):
#     def model(self):
#         print("Chevrolet")
#
# class Ger(Car):
#     def model(self):
#         print("Wolswagen")
#         print("BMW")
#         print("Mersades")
#
# r = Ru("ru")
# r.model()


#
#
# class Transport:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#     def info(self):
#         return f"Transport nomi {self.name} u ketyatgan tezlik {self.speed}"
#
#
# class Car(Transport):
#     def info(self):
#         return f"{self.name} nomli avtomobil {self.speed} - tezligda xarakatlanmoqda"
#
# class Bicycle(Transport):
#     def info(self):
#         return f"{self.name} markali velosiped {self.speed} - tezlikda xarakatlanmoqda"
#
# c = Car("C", 250)
# print(c.info())
# v = Bicycle("A", 25)
# print(v.info())
#
#

