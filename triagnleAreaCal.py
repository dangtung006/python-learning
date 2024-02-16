import math


def cal_triangle_area(a, b, c):
    if all([
        a + b > c,
        a + c > b,
        c + b > a
    ]):
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area
    else :
        return "Invalid Triangle"

print("Enter 3 triangle side lengths: ")
a, b, c = [float(input("f{i} = ")) for i in 'abc']

area = cal_triangle_area(a, b, c)
print(area)
