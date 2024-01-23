import math

def giaiPTBac2(a, b, c):

    if(a == 0):
        if(b == 0):
            print("Phuong trinh VN")
        else:
            print(f"Phuong Trinh co 1 nghiem = {-c/b}")
        return
    
    delta = b * b - 4 * a * c
    
    if(delta < 0):
        print("Phuong Trinh VN")
    elif(delta == 0):
        print(f"Phuong Trinh co 1 nghiem kep= {-b/(2* a)}")
    else:
        print(f"Phuong trinh co 2 nghiem x1 = { (-b + math.sqrt(delta))/ (2 * a) } va x2 = {(-b - math.sqrt(delta))/ (2 * a)}")

a = float(input("Nhap he so bac hai, a= "))
b = float(input("Nhap he so bac nhat, b= "))
c = float(input("Nhap he so tu do, c= "))

giaiPTBac2(a, b, c)


