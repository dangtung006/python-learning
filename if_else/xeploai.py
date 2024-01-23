dtb = float(input('Nhap vao diem trung binh: '))

if dtb >=9.0:
    print("Gioi")
elif dtb >=7.0 and dtb < 9.0:
    print("Kha")
elif dtb >=5.0 and dtb < 7.0:
    print("Trung binh")
else:
    print("Yeu")