## Tao MK:
password = input("Nhap vao mk cua ban: ")

x = bool
y = bool

for char in password:
    if char.isdigit():
        x = True
        break
    else:
        x = False

for char in password:
    if char.isalpha():
        y = True
        break
    else:
        y = False

while len(password) < 6 or x == False or y == False:
    print("Mk phai co do dai it nhat 6 ki tu bao gom it nhat 1 chu cai va 1 chu 6") 
    password = input("Nhap vao mk cua ban: ") 
else:
    print("mk hop le")


### Check Dang nhap he thong:
count = 0
s = input("Nhap vao mk cua ban: ")

while s != password:
    count += 1
    s = input("Nhap vao mk cua ban: ")
    
    if count > 6:
        print("Ban da bi khoa do nhap mk sai qua 6 lan")
        break
else:
    print("Dang nhap thanh cong!!")
