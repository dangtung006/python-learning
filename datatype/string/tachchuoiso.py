n = input("Nhap vao 1 chuoi: ")
num=''
word=''

for i in n:
    if i.isdigit():
        num+=i
    elif i.isalpha():
        word+=i

print(num)
print(word)
