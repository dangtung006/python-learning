class Xe:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

class XeWithNothing :
    pass

xe1 = XeWithNothing()
xe2 = Xe(max_speed=200, mileage=20000)
print(xe2.max_speed)
