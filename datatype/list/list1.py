list = [1,2,1,3,4,1, 'a', 'b']


### 1 số hàm cơ bản:
print(len(list))
print(list.count(1))
print(list.count('a'))

## chen a vào vị trí thứ 2
list.insert(2, 'a')
print(list)

## tim vi tri cua phan tu dau tien tim thay:
print('a o vi tri thu: ', list.index('a'))

### noi 1 list khac vao list ban dau :
list.extend(['1', 1, 3])
print('List dc noi them : ', list)

### sắp xếp list :
numsList = [1,2, 6, 7, 8, 10, 2]
# numsList.sort()
# print("sort: lssit" ,  numsList)
print(sorted(numsList))

## đảo ngược list
list.reverse()
print(list)

## xoa các phần tử trong list, list trở thành list rỗng:
list.clear()
print(list)