## Protected

class Animal:
    def __init__(self, name, kingdom):
        self._name = name
        self._kingdom = kingdom
    
    # disebut method function
    def display(self):
        # print("test")
        return self._name, self._kingdom
    

class Food(Animal):
    def details(self):
        print(f"This is {self._name}, {self._name} is {self._kingdom}")

my_animal = Food("Cow", "mammals")
print(my_animal._name)
print(my_animal._kingdom)
my_animal.details()


# Private

class Animal:
    def __init__(self, name, kingdom):
        self.__name = name
        self.__kingdom = kingdom
    
    # disebut method function
    def display(self):
        return self.__name, self.__kingdom
    

class Food(Animal):
    def details(self):
        print(f"This is {self.__name}, {self.__name} is {self.__kingdom}")

my_animal = Animal("Cow", "mammals")
print(my_animal)
# print(my_animal.__name)
# print(my_animal.__kingdom)
# my_animal.display()
