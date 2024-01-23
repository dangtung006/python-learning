import qlsv.data as d 

def makeInput(msg) :
    field = input(f"{msg} : ")
    return field

# def checkExistStudent():

def findStudent(id):
    for i in range(0, len(d.listStudent)) :
        if d.listStudent[i]['id'] == id:
            return [i, d.listStudent[i]]
        
    return False

def logMsg(msg):
    print(f"**{msg}**")

def addStudent():
    logMsg("Them sinh vien")
    id = makeInput("Nhap ID sinh vien")
    name = makeInput("Nhap Ten Sinh Vien")

    while True:
        student = findStudent(id)
        print("student: " , student)
        if student != False:
            print("Da ton tai")
            id = makeInput("Nhap ID sinh vien")
        else:
            break

    d.listStudent.append({ "id" : id, "name" : name})

def editStudent():
    logMsg("Sua sinh vien")
    id = makeInput("Nhap vao Id can sua: ")
    student = findStudent(id)

    if student == False:
        return logMsg("Khong tim thay sinh vien")
    
    name = makeInput("Nhap ten sinh vien")

    student[1]["name"] = name
    d.listStudent[student[0]] = student[1]
    


def removeStudent():
    logMsg("Xoa sinh vien")
    id = makeInput("Nhap Id can xoa: ")

    student = findStudent(id)
    if student != False:
        d.listStudent.remove(student[1])
        print("Xoa sinh vien thanh cong")
    else:
        print("Khong tim thay sinh vien can xoa")    

    
def showStudents():
    logMsg("Danh sach Sinh Vien Hien Tai")
    for i in range(0, len(d.listStudent)):
        print(d.listStudent[i])