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
    def __init__(self, name, kingdom, food, classification):
        self.food = food
        self.classification = classification

        #invoking the __init__ of the parent class
        Animal.__init__(self, name, kingdom)
        #jika tidak dipanggil maka outputnya error
    
    def details(self):
        print(f"{self.name} likes eating {self.food}")
        print(f"thats why {self.name} known as {self.classification}")   ## herbivore, omnivore, carnivore


my_animal = Food("Cow", "mammals", "grass", "herbivore")
my_animal.display()
my_animal.details()