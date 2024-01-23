f = open("student.txt", "a+", encoding="utf-8")


while True:
    mssv = input("Nhap vao stt cua sv: ")
    if mssv == "":
        break

    Hoten = input("Nhap vao ten sinh vien : ")
    Lop = input("Nhap vao Lop : ")
    Quequan = input("Nhap vao que quan : ")

    f.write("\t".join([mssv, Hoten, Lop, Quequan]) + "\n")
f.close()

#Read File after writing :
f = open("student.txt", "r", encoding="utf-8")
print("\t".join(["mssv", "Hoten", "Lop", "Quequan"]))
ctx = f.readlines()
for l in ctx:
    print(l)
