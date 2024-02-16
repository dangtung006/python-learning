##set là một kiểu dữ liệu dùng để lưu trữ tập hợp các phần tử duy nhất, không có thứ tự. Cụ thể, mỗi phần tử trong một set sẽ chỉ xuất hiện một lần duy nhất trong tập hợp.


## define a set:
my_set = {1, 2, 3}
my_another_set = set([4, 5, 6])

### imutable data type :
my_set.add(2)
my_set.add(4)
print(my_set)
### remove item:
my_set.remove(2)
print(my_set)

### thao tac tren tap hop;
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {2, 3}

print(set1.union(set2))      # Output: {1, 2, 3, 4}
print(set1.intersection(set2)) # Output: {2, 3}
print(set1.difference(set2)) # Output: {1}
print(set1.issubset(set2))    ### kiểm tra tập con Output: False
print(set3.issubset(set2))    ### kiểm tra tập con Output: True

#### loop through a set :
my_set = {1, 2, 3}
for item in my_set:
    print(item)

