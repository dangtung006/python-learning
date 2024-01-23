nam = int(input("Nhap vao nam can kiem tra: "))

if (nam % 4 ==0 or nam % 100 == 0) or nam % 400 == 0:
    print(f'{nam} la nam nhuan')
else:
    print(f'{nam} khong la nam nhuan')