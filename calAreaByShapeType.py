import math

def shape_area(circle = False, regular = False, a = 0, b = 0, c = 0):
    ### cal circle
    if circle:
        return math.pi * a ** 2
    ### cal regular
    elif regular:
        return 1/4 * a * (b ** 2)/math.tan(math.pi/a)
    ### cal rectangle
    elif not c:
        return a * b
    ### cal triangle
    p = (a + b + c )/2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f'circle are is {shape_area(circle=True, a=2)}')