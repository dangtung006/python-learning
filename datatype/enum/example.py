from enum import Enum
from time import sleep

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)         # Output: Color.RED
print(Color.RED.value)   # Output: 


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Function to determine if a day is a weekend day or a weekday
def is_weekend(day):
    return day in [Weekday.SATURDAY, Weekday.SUNDAY]

# Usage example
today = Weekday.TUESDAY
print("Is today a weekend day?", is_weekend(today))  # Output: False

weekend_day = Weekday.SATURDAY
print("Is weekend_day a weekend day?", is_weekend(weekend_day))  # Output: True

class TrafficLight(Enum):
    RED = "Stop"
    YELLOW = "Prepare to stop"
    GREEN = "Go"

# Function to simulate a traffic light changing state
def simulate_traffic_light():
    for light in TrafficLight:
        print(light.value)
        if light != TrafficLight.GREEN:
            sleep(3)  # Wait for 3 seconds
        else:
            sleep(5)  # Wait for 5 seconds

# Simulate the traffic light
simulate_traffic_light()