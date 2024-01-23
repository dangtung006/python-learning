
a = input('Nhap vao 1 so: ')

nums = [int(i) for i in a]
sumNums = sum(nums)
result = bool

if sumNums < 2 :
    result = False
else:
    for i in range(2, sumNums):
        if sumNums % i == 0:
            result = False
            break
    result = True

if result == True:
    print(f'Tong cac chu so cua {a} la so ngt')
else:
    print(f'Tong cac chu so cua {a} k la so ngt')