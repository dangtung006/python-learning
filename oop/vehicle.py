class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass


class Car():

    tax = 1
    instanceCar = 0

    def __init__(self, brand, founded_year, price, original):
        self.brand_ = brand
        self.founded_year = founded_year
        self.price_ = price
        self.original_ = original
        Car.instanceCar += 1

    def getVal(self):
        return self.price_ * self.tax
    
    @classmethod
    def from_string(cls, car_string):
        brand, founded_year, price, original = car_string.split('-')
        founded_year = int(founded_year)
        price = int(price)
        return cls(brand, founded_year, price, original)
    
    @staticmethod
    def checkCarPrice(price):
        if price > 1000:
            return "So expensive"
        return 'really cheap'
        

    
    

#######
mybus = Bus("City Bus", 200, 10000)
print(f"The bus is {mybus.name}")

######
BMW = Car("BMW", 1980, 3000, "Germany")
Toyota = Car("Toyota", 1981, 3000, "Japanese")
Ferrari = Car.from_string("Ferrari-1981-3000-Italy")

print(f"Total car is {Car.instanceCar}")

BMW.name = "My redcar"
Toyota.name = "JapanCar"
Toyota.tax = 1.2

print(f'My car is {BMW.name} from {BMW.original_} and it is about {BMW.getVal()} $')
print(f'His car is {Toyota.name} from {Toyota.original_} and it is about {Toyota.getVal()} $')
print(Ferrari.__dict__)
print(Car.checkCarPrice(500))
