class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def updateOdometer(self, mileage):
        self.odometer_reading = mileage
    
    def incrementOdometer(self, miles):
        self.odometer_reading  += miles

    def readOdometer(self):
        print(f'This car has {self.odometer_reading} miles on it')

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def fillGasTank(self):
        print("Fill gas")

class ElectricCar(Car):

    def __init__(self, make, model, year, battery):
        super().__init__(make, model, year)
        self.batterySize = battery

    def describeBattery(self):
        print(f'This car has a {self.batterySize}-kWh battery')
    
    def getRange(self):

        range = 0
        if self.batterySize == 75:
            range = 260
        elif self.batterySize == 100:
            range = 315

        print(f'This car can go about {range} miles on a full charge')

    def fillGasTank(self):
        print("This car doent need a gas tannk")
        

myCar = Car('audi', 'a4', 2019)
## sua doi truc tiep gia tri cua thuoc tinh:
myCar.odometer_reading = 23
## sua doi gia tri cua thuoc tinh thong qua phuong thuc
myCar.updateOdometer(23_500)
myCar.incrementOdometer(100)
print(myCar.get_descriptive_name())
myCar.readOdometer()

myElectricCar = ElectricCar('tesla', 'model s', '2019', 75)
myElectricCar.describeBattery()
myElectricCar.getRange()
myElectricCar.fillGasTank()
