numString = '6 371 18 153 28'
nums = numString.split(' ')

stmList = []
for num in nums :
    tong = 0

    for digit in num :
        tong += int(digit)**3

    if tong == int(num):
        stmList.append(int(num))

print(sorted(stmList))


