## sang so nguyen to:
def isMersenne(x):
    x += 1
    i = 1

    while 2 ** i < x:
        i+= 1
    return x == 2 ** i

n = 10000
numList = [True] * n
soNt = []

for i in range(2, n):
    if numList[i] == True:
        for j in range(2 * i, n, i ):
            numList[j] = False


for i in range(2, n):
    if numList[i] == True:
        soNt.append(i)


for i in range(2, n):
    if numList[i] == True and isMersenne(i) == True:
        print(i)

### tim so nguyen to lan nhat co n chu so:
n = int(input("Nhap vao so chu so : "))
max = int('9'* n)

while max not in soNt:
    max-= 1
print(max)



