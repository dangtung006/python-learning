thang = int(input("Nhap vao thang : "))

if thang in (1, 3, 5, 7, 8, 12):
    print(f'thang {thang} co 31 ngay')
elif thang in (4, 6, 9, 11):
    print(f'thang {thang} co 30 ngay')
elif thang == 2:
    n = int(input("Vui long nhap vao nam: "))
    if (n % 4 == 0 and n % 400 == 0) or n % 100 == 0:
        print(f'thang {thang} nam {n} co 28 ngay')
    else:
        print(f'thang {thang} nam {n} co 29 ngay')
