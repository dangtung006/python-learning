## sang so nguyen to:

n = 1000
numList = [True] * n
soNt = []

for i in range(2, n):
    if numList[i] == True:
        for j in range(2 * i, n, i ):
            numList[j] = False


for i in range(2, n):
    if numList[i] == True:
        soNt.append(i)

print(soNt)
