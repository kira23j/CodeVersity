class Python:
    def __init__(self):
        print("hello from python oop")
sample=Python()
print(sample)

# ---------------------------------
class MusicIntrument:
    def __init__(self,name,origin) :
        self.name=name
        self.origin=origin
        print(name,"from",origin)

begena=MusicIntrument("begena","ethiopia")
masinko=MusicIntrument("masinko","Ethiopia")
print(begena, masinko)

# -------------------------

class Book():
    def __init__(self,title,author,genre,price=100):
        self.title=title
        self.author=author
        self.genre=genre
        self.price=price
    def describe(self):
        print(f"The book name is {self.title} which is written by {self.title} with a price of {self.price} and its genre is {self.genre}")
love_to_death=Book("fikir eske mekabir","hadis alemayehu","romantic")
print(love_to_death.describe())

# -----------------------
class SmartPhones:
    def __init__(self):
        self.company="Apple"
        self._firmware=150
    def get_firmaware(self):
        return self._firmware
iphone=SmartPhones()
print(iphone.get_firmaware)
print(iphone.company)
# ------------define properties with property method
class Height:
    def __init__(self,km):
        self.meters=km/1000
    def get_kmeters(self):
        return self.meters*1000
    def set_km(self,km):
        if km>0:
            pass
    sample=property(get_kmeters,set_km)
inc=Height(4)
print(inc.sample)
# using getattr and setattr functions





# using hasattr and delattr functions



#  class methods
class EthioMeals:
    def __init__(self,coffee,dorowot,injera) :
        self.coffee=coffee
        self.dorowot=dorowot
        self.injera=injera
    @classmethod
    def MealLovers(cls):
        return cls(coffee=0,injera=5,dorowot=8)
sample=EthioMeals(coffee=4,injera=4,dorowot=8)
print(sample.MealLovers())






