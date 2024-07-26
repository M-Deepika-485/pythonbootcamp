#creation of class
class Myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
       return a*b
     def div(a,b):
        return a/b
    def mod(a,b):
        return a%b
#creation of object
obj1=Myclass
obj2=Myclass
obj3=Myclass
obj4=Myclass
obj5=Myclass
print(obj1.add(5,6))
print(obj2.sub(5,6))
print(obj3.mul(5,6))
print(obj4.div(5,6))
print(obj5.mod(5,6))
#inheritance
class Animal:
    def speak():
        return "Animal is speaking"
class Dog:
    def bark():
        return "bow...."
obj1=Animal
obj2=Dog
print(obj1.speak())
print(obj2.bark())
#multiple inheritance
class Father:
    def Father_speak():
        return"Father class"
class Mother:
    def Mother_speak():
        return"Mother class"
class Kid(Father,Mother):
    def kid_speak():       
        return"IM kid having properties of Mother class and Father class"
obj1=Kid
print(obj1.Father_speak())
print(obj1.Mother_speak())
print(obj1.kid_speak())
method_over_riding
class Animal:
    def speak():
        return"speaking...."
class Dog:
    def speak():
        return" Dog speaking..."
class Puppy:
    def speak():
        return" Puppy speaking..."
obj3=Puppy
print(obj3.speak())
