
"""
Multiple inheritance 
- when one class inherits from multiple classes, and is able to use attributes and methods from
both classes. 

2 ways to do:
    1. method resolution order
    2. Super (but not recommended)

class Animal():
    def __init__(self, sound,look):
    ...
class Place():
    def __init__(self,climate, lat,lon)

class Mamma(Animal, Place)
    def __init__(self, sound,look,lat,lon, food)
        Animal.__init__(self,sound,look)
        Place.__init__(self,climate,lon)
        self.food = food
    """

#Parent class 1

class Item():
    def __init__(self, sku):
        self.sku = sku
    
    def print_sku(self):
        print("The sku is {}.".format(self.sku))


#Parent class 2

class Garment():
    def __init__(self, section,type): 
        self.section = section
        self.type = type
    def print_garment(self):
        print("The garment is section{}. {}.".format(self.section,self.type))

#Child Class 
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name 
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color,self.name))

Blouse = Shirts("0001", 43, "Tops","Formal Blouse", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()