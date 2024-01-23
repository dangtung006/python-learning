class Student:
    
    _data = []

    def makeInput(msg):
        field = input(f"{msg} : ")
        return field
    
    def logMsg(msg):
        print(f"**{msg}**")

    def findStudent(self, id):
        for i in range(0, len(self._data)) :
            if self._data[i]['id'] == id:
                return [i, self._data[i]]
        
        return False
    
    def addStudent(self):
        self.logMsg("Them sinh vien")
        id = self.makeInput("Nhap ID sinh vien")
        name = self.makeInput("Nhap Ten Sinh Vien")

        while True:
            student = self.findStudent(id)
            print("student: " , student)
            if student != False:
                print("Da ton tai")
                id = self.makeInput("Nhap ID sinh vien")
            else:
                break

        self._data.append({ "id" : id, "name" : name})
    
    def editStudent(self):
        self.logMsg("Sua sinh vien")
        id = self.makeInput("Nhap vao Id can sua: ")
        student = self.findStudent(id)

        if student == False:
            return self.logMsg("Khong tim thay sinh vien")
    
        name = self.makeInput("Nhap ten sinh vien")

        student[1]["name"] = name
        self._data[student[0]] = student[1]

    def removeStudent(self):
        self.logMsg("Xoa sinh vien")
        id = self.makeInput("Nhap Id can xoa: ")

        student = self.findStudent(id)

        if student != False:
            self._data.remove(student[1])
            print("Xoa sinh vien thanh cong")
        else:
            print("Khong tim thay sinh vien can xoa")    

    
    def showStudents(self):
        self.logMsg("Danh sach Sinh Vien Hien Tai")
        for i in range(0, len(self._data)):
            print(self._data)


    
st = Student()
actionType = 0

while actionType >= 0:
    if actionType == 1:
        st.addStudent()
    elif actionType == 2:
        st.removeStudent()
    elif actionType == 3:
        st.editStudent()
    elif actionType == 4:
        st.showStudents()

    print("Chọn chức năng muốn thực hiện:")
    print("Nhập 1: Thêm sinh viên")
    print("Nhập 2: Xóa sinh viên")
    print("Nhập 3: Sửa sinh viên")
    print("Nhập 4: Xem danh sách sinh viên")
    print("Nhập 0: Thoát khỏi chương trình")

    actionType = int(input())
    if actionType == 0:
        break
