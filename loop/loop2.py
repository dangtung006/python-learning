## Tinh tong S = 1! + 2! + 3! + 4! + 5! + ... 10!

m = 1
tong = 0

for i in range(1,11):
    m = m * i
    tong += m

print(tong)
