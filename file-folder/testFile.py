# r: chỉ cho phép đọc file
# r+: cho phép đọc và ghi file khi ghi file thì đè lên dòng đầu tiên của file
# w: chỉ cho ghi file
# w+: cho phép đọc và ghi file khi ghi thi ghi đè nội dung mới lên file
# a: chỉ cho phép ghi file, con trỏ đặt ở cuối file nên khi ghi thi ghi nội dung vào cuối file
# a+: cho phép đọc và ghi file,không trả về nội dung khi đọc file con trỏ đặt ở cuối file nên khi ghi thi ghi nội dung vào cuối file

def readFileContent(file):
    ctx = file.readlines()
    print("ctx", ctx)
    for i in ctx:
        print(i)

def handleFile_1(f):
    try:
        f.write("day la dong 6" + "\n")
        readFileContent(f)
    except Exception as err:
        print(err)
    finally:   
        f.close()

def handleFile_2():
    with open("test.txt", 'a', encoding="utf-8") as f:
        f.write("day la dong 6" + "\n")
        readFileContent(f)
    # try:
    #     with open("test.txt", 'a', encoding="utf-8") as f:
    #         f.write("day la dong 6" + "\n")
    #         readFileContent(f)

    # except Exception as err:
    #     print(err)
    # finally:
    #     f.close()


f = open("test.txt", 'a', encoding="utf-8")
handleFile_2()


