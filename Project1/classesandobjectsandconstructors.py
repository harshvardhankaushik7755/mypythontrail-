class Person:
    def __init__(self, n, o):
        print("Hey I am a person")
        self.name = n
        self.occ = o
    # name = "harsh"
    # occ = "web developer"
    
    def info(self):
            print(f"{self.name} is a {self.occ}")
a = Person("harsh", "developer")
b = Person("yashu", "cryer")
a.info()
b.info()
# print(a.name)
a.name = "yashu"
a.occ = "crying"
a.info()
b.info()