# viết chương trình nhập vào 1 danh sách sau đó :
# - tạo ra 1 list mới với các phần tử có giá trị bằng bình phương của các phần tử tương ứng trong list cũ
# - tìm các phần tử có giá trị lớn hơn 50

lst = []
count = 0
n = int(input("Nhap vao so phan tu : "))

while count < n:
    count = count + 1
    item = int(input(f"Nhap vao phan tu thu {len(lst) + 1}: "))
    lst.append(item)


########
lstPow2 = []
for i in lst:
    lstPow2.append(i ** 2)

print(lstPow2)

#######
lstGt50= []
for item in lstPow2:
    if(item > 50):
        lstGt50.append(item)
print(lstGt50)



