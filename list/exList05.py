#Viết chương trình in ra số lớn thứ 2 và số nhỏ thứ 2 của danh sách và in ra index của chúng
#Vi du cho list sau : 

lst = [1, 3, 2, 5, 8, 9, 10]

##LG :
lst_2 = []
for i in lst:
    if i == max(lst):
        continue
    else:
        lst_2.append(i)
 
lst_3 = []
for i in lst:
    if i == min(lst):
        continue
    else:
        lst_3.append(i)

lst_idx = []
for i in range(len(lst)):
    if lst[i] == max(lst_2) or lst[i] == min(lst_3):
        lst_idx.append(i)
        
print(lst_idx)

    