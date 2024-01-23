import qlsv.student as st 

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