# Viết chương trình nhập vào 1 list:
# in ra có bao nhiêu số nhỏ hơn 5
# in ra ví trí index của nhưng số đó

# LG :

lst = []
count = 0
n = int(input("Nhap vao so phan tu : "))

while count < n:
    count = count + 1
    item = int(input(f"Nhap vao phan tu thu {len(lst) + 1}: "))
    lst.append(item)


dem = 0
lstIdx = []

for i in range(len(lst)):
    if lst[i] > 5:
        dem += 1
        lstIdx.append(lst[i])

print(dem, lstIdx)
