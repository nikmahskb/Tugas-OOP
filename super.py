# parent class
class Animal(object):
    def __init__(self, name, kingdom):
        self.name = name
        self.kingdom = kingdom

    def display(self):
        print(f"This is {self.name}")

        
    
# child class
class Food(Animal):  #Food mewarisi dari Animal
    def display(self):
        super().display(), print(f"{self.name} classified as {self.kingdom}")  


my_animal = Food("Cow", "mammals")
my_animal.display()