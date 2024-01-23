# Viết chương trình trả lời kết quả phép toán :
quest = ["2 + 5 + 7=","5*10=","12%2=","5//2="]

#LG:

for i in quest:
    k = i.strip("=")
    result = eval(k)
    ans = float(input(f"{i} "))

    if result == ans:
        print("corect")
    else:
        print("WRONG!!!: the correct answer is: " , result)