
def my_reverse_func(a):
    result = None
    count = len(a) - 1

    if type(a) == str:
        result = ""
        while count>=0:
            result += a[count]
            count -= 1
    
    elif type(a) == list:
        result = []
        while count >=0:
            result.append(a[count])
            count -= 1

    return result

print(my_reverse_func([1,2,3,4,5,6]))