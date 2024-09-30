# parent class
class Animal(object):
    def __init__(self, name, kingdom):
        self.name = name
        self.kingdom = kingdom

    def display(self):
        print(self.name)
        print(self.kingdom)
        
    
# child class
class Food(Animal):  #Food mewarisi dari Animal
    def details(self):
        print(f"This is {self.name}")
        print(f"Kingdom: {self.kingdom}")   ## herbivore, omnivore, carnivore


my_animal = Food("Cow", "mammals")
my_animal.display()
my_animal.details()