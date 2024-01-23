class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @property
    def fullname(self):
        return f'{self.brand} {self.model}'
    
    @fullname.setter
    def fullname(self, full_name):
        brand, model = full_name.split(" ")
        self.brand = brand
        self.model = model

    @fullname.deleter
    def fullname(self):
        self.brand = None
        self.model = None
MyBMW = Car("haaah", "hhhiii")
# print(MyBMW)
# print(MyBMW.fullname)
MyBMW.fullname = "BMW i320"
print(MyBMW.brand)
print(MyBMW.model)
