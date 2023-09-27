"""
chapter 8; classes

class features
single file per class
OR
Multiple classes can be contained in one file

inheritance - derived/child class can use attributes and methods of parent class
multiple inheritance - derived/child class can inherit attributes and methods from more than one class
polymophism - derived/child classes can override class methods of parent class

class variables - for use by all methods in the class
instance variables - for use by the specific method in which the variable is declared/created

"""

# __init__ method allows every instance of a class to be created/initialized with be specific parameters
# the __init__ method called a constructor as well
# self variables allows info can be shared easily and efficiently

import random


class Person:
    def __init__(self, firstname, lastname, health, status):
        " initialize attributes to be used in/available for all class \ class method in this class, and for class objects created \ "

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hello, my name {} {}".format(self.firstname,self.lastname,self.health,self.status))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print ("{} is totally healthy!". format(self.firstname))
        elif self.health <=76:
            print("{} feels unwell.".format(self.firstname))
        elif self.health <=50:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious".format(self.firstname))

Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()

class Enemy(Person):
    def __init__(self,weapon,firstname,lastname,health, status):
        super().__init__(firstname,lastname,health,status)
        self.weapon = weapon

    def hurt(self, other): 
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -=5
        print(other.health)
    def insult(self,other):
        if other.health<= 80:
            print("{}, you are tired and weak".format(other.firstname))
       
    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False
Alex = Enemy('rock', 'Alex', 'Wayne', 75, status = False )

Alex.hurt(Maria)
Alex.insult(Rey)
Alex.insult(Lee)

Alex.steal(Rey)
#Rey.steal(Alex) - will cause an error
