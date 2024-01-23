class Xe:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class XeBuyt(Xe):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

bus = XeBuyt("City Bus", 60, 30000)

print(bus.seating_capacity(80))


