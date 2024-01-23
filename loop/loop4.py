### Tim so hoan thien trong khoang 1 den 50

for num in range(1, 1000):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    if s == num :
        print(num)