myTuple = (1, 2, 3, 'a', 'b', 'c')

print(myTuple)

## access item in tuple:
print(myTuple[0])

### immutable type 
try:
    myTuple[0] = 0
except Exception as err:
    print(str(err))

### check length of tuple :
print(len(myTuple))

#### unpack tuple:
one , two, three, a, b, c = myTuple
print(one , two, three, a, b, c)

first, *middle,  last =  myTuple
print(first, middle, last)

### check item in tuple :
print(3 in myTuple)

## check index of item:
print(myTuple.index(3))

### count item in tuple:
print(myTuple.count(3))

### sort tuple :
print(tuple(sorted((1, 5, 6, 2, 4, 8, 3))))

### extend a tuple :
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
print(tuple1 + tuple2)

### loop through a tuple :
for item in myTuple:
    print(item)

#### compare tuple :
tuple1 = ('apple', 'banana', 'orange')
tuple2 = ('apple', 'banana', 'orange')
tuple3 = ('apple', 'banana', 'pear')

print(tuple1 == tuple2)  # Output: True
print(tuple1 != tuple3)  # Output: True
print(tuple1 < tuple3)   # Output: True
print(tuple1 > tuple3)   # Output: False

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(tuple1 == tuple2)  # Output: False
print(tuple1 < tuple2)   # Output: True
print(tuple1 > tuple2)   # Output: False