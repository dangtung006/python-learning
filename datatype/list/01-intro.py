#### create a list :
fruits  = ['banana', 'apple', 'grape', 'cherry', 'jackfruit', 'melon', 'leechi', 'conut']
demoList = [1,2,1,3,4,1, 'a', 'b']
myTestList = list()
####### access element in list:
print(fruits[0]) ## phan tu dau
print(fruits[-1]) ## phan tu cuoi

### slicing list
print(fruits[2:]) ## cat va bo di cac phan tu truoc vi tri thu n ['grape', 'cherry']
print(fruits[:2]) ## cat va bo di cac phan tu từ vi tri thu n : ['banana', 'apple]
print(fruits[1:2]) ## cat va bo di cac phan tu trước vị trí thứ 1 đến vị trí thứ 2

### Note :
newFruits = fruits[::] ## clone, copy array
print(newFruits)
print(fruits[::-1]) ### reverse array
print(fruits[::2]) ## loc ra cac phan tu co index += 2

############ add item to list #######
doubleList = demoList * 2
print(doubleList)

### add item to list
demoList.append("test")
print(demoList)

### add muliti item to list
demoList.extend(['1', 1, 3])
print('demolist dc noi them : ', demoList)

### add item to a specific position :
demoList.insert(2, 'a')
print(demoList)

### remove item to list #######
demoList.pop() ### remove the last item in list:
demoList.pop(1) ### remove the item in 1 index
demoList.remove(3) ### xoa phan tu dau tien tim thay co value = 3 trong list
demoList.clear() ### change list to empty list
del demoList[1] ### xoa phan tu o vi tri thu 1

########## sắp xếp list ############### :
numsList = [1,2, 6, 7, 8, 10, 2]
numsList.sort(reverse=True)
print("sort: lssit" ,  numsList)
print(sorted(numsList))

## đảo ngược list
demoList.reverse()
print(demoList)

### Loop through a list :
for fruit in fruits:
    print(fruit)

american_presidents = ['Bill Clinton', 'Bush', 'Obama', 'Trump']
for idx, president in enumerate(american_presidents, start=1):
    print(f"president #{idx}: {president}")

###### 1 số ham khac #######
print(len(demoList))
print(demoList.count(1))
print(demoList.count('a'))
print('a o vi tri thu: ', demoList.index('a')) ## tim vi tri cua phan tu dau tien tim thay:
print(sum([1,2, 3]))
print(min([1,2, 3]))
print(max([1,2, 3]))
