thang = int(input("Nhap vao thang: "))

if thang in (1, 2, 3):
    print('thang {thang} thuoc quy 1')
elif thang in (4, 5, 6):
    print('thang {thang} thuoc quy 2')
elif thang in (7, 8, 9):
    print('thang {thang} thuoc quy 3')
elif thang in (10, 11, 12):
    print('thang {thang} thuoc quy 4')
else:
    print("Thang {thang} khong co tren lich, vui long nhap lai")