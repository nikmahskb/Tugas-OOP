class Animal:
  
    def intro(self):
        print("Ada banyak jenis hewan.")

    def detail(self):
        print("Sebagian hewan berkaki empat.")

class sapi(Animal):
  
    def detail(self):
        print("Sapi makan rumput.")

class kucing(Animal):

    def detail(self):
        print("Kucing makan ikan.")

obj_hewan = Animal()
obj_sapi = sapi()
obj_kucing = kucing()

obj_hewan.intro()
obj_hewan.detail()

obj_sapi.intro()
obj_sapi.detail()

obj_kucing.intro()
obj_kucing.detail()
