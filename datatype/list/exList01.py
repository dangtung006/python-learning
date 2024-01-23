# viết chương trình tạo ra list n phần tử , các phần tử đều là số nguyên từ (1, 100)
from random import randrange
n = int(input("Nhap vao so phan tu : "))
lst = [0] * n

for i in range(n):
    rd = randrange(1, 101)
    print("rd : " ,  rd)
    lst[i] = rd

print(lst)