class service:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")
          

Nikmah = service("nikmah")
Nikmah.greet()

