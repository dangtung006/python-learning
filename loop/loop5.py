# S = 1/1**2 + 1/2**2 ... + ... 1/n** 2

tong = 0
n = 3

for i in range(1, n + 1):
    tong += 1/(i**2)

print(round(tong, 3))