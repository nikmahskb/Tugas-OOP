# parent class
class Animal(object):
    def __init__(self, name, kingdom, food, classification):
        self.name = name
        self.kingdom = kingdom
        self.food = food
        self.classification = classification
       
    def display(self):
        print(f"This is {self.name}, one of {self.kingdom} in the world")

        
    
# child class
class Food(Animal):  #Food mewarisi dari Animal
    def details(self):
        print(f"{self.name} likes eating {self.food}")

# another child class that inheritance from child and parent class
class Classification(Food):
    # def __init__(self, name, kingdom, food, classification):
    #     self.food = food
    #     self.classification = classification

    def anim_class(self):
        print(f"they are {self.classification}")

my_animal = Classification("Cow", "mammals", "grass", "herbivore")
my_animal.display()
my_animal.details()
my_animal.anim_class()
