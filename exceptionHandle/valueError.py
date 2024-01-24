try:
    a = int(input("Nhap vao 1 so: "))
except ValueError as err:
    print("Value Err input: ", err)
