## viet chuong chinh tinh tong tu 0 den 1 so nguyen bat ki, so do dc nhap vao ban phim.
# a = int(input("Nhap vao 1 so nguyen bat ki: "))
# total = 0
# for i in range(0, a+1):
#     total += i

# print(total)


## tim so chan tu 0 den 10 theo thu tu tang dan
# for i in range(0, 11, 2):
#     print(i)

## tom so chan tu 0 den 10 theo thu tu giam dan :
# for i in range(10, 0, -2):
#     print(i)

# for i in range(0, 10):
#     if i % 2 == 0:
#         print(i)

## tinh tong so chan tu 0 den 10:
# tong_chan = 0 
# for i in range(0, 11):
#     if i % 2 == 0:
#         tong_chan+= i
# print(tong_chan)

## Tinh tong so le tu 0 den 10:

tong_le = 0
for i in range(0, 11):
    if i % 2 == 0:
        continue
    else:
        tong_le += i

print(tong_le)
