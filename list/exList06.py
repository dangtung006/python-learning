lst = [160, 158, 158, 160, 159, 158, 159, 160, 158, 161]

# count_lst = []
# for num in lst:
#     count = lst.count(num)
#     count_lst.append(count)

count_list = [lst.count(num) for num in lst]
max = max(count_list)
maxIdx = count_list.index(max)
print(max, lst[maxIdx])