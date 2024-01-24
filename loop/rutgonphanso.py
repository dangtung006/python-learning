def ucln(a, b):
    while a != b:
        if a > b:
            a-= b
        else:
            b-=a
    return a

tu = int(input("Nhap vao tu so: "))
mau = int(input("Nhap vao mau so: "))

uclnOfTuvamau = ucln(tu, mau)

print(f"Phan so rut gon la: {int(tu/uclnOfTuvamau)} / {int(mau/uclnOfTuvamau)}")