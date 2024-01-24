try:
    a = int(input("Nhap vao 1 so: "))
except ValueError as err:
    print("Value Err input: ", err)


try:
    myList = [1, 4, 6]
    myList.remove(2)
except ValueError as err :
    print("Value Err is : " , err)