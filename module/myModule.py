def greetOne(name):
    print(f"Hello {name} !!")

def add(num_1, num_2):
    return num_1 + num_2


person = {
    "name" : "tungdang",
    "age" : 30,
    "job" : "nhat la da ong bo"
}

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f"Hello, my name is {self.name}")


if __name__ == '__main__' :
    print("sub module")
  

