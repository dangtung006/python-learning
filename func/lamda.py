squareNum = lambda num : num ** 2
isEven = lambda num : num % 2 == 0
countTotal = lambda a, b : a + b
getMax = lambda a, b :  a if a > b else b
titleWord = lambda word : word.title()


sortByKey = lambda point : point[1]
sortByAbs = lambda val : abs(val)


# print(squareNum(2))
# print(isEven(4))
from functools import reduce

print(sorted([(1, -2), (2, -1)], key = sortByKey))
print(sorted([-1, -2, 5, -9, -5], key = sortByAbs))
print(list(map(titleWord, ['apple', 'google', 'facebook'])))
print(list(filter(isEven, [1, 2, 4, 5, 6, 8])))

print(reduce(countTotal, [1, 3, 4, 5, 8, 9]))
print(reduce(getMax, [1, 3, 4, 6, 7, 8, 9]))