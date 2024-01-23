a= 10
b = 8
ucln = None

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
    print(a, b)
else:
    ucln = a

print(ucln)
