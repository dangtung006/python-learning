while True:
    ## Lay input dau vao
    hten = input("Nhap ho ten cua ban: ")
    mhon = input("Nhap ten mon hoc: ")
    diem = float(input("Nhap diem"))

    print(f'Hoc sinh {hten.title()} du thi mon {mhon.title()} voi ket qua {diem} diem')

    ## Xep loai Diem hoc sinh
    if diem >= 7:
        print('Xep loai : KHA')
    elif diem < 7 and diem > 4 :
        print('Xep loai : TRUNG BINH')
    else:
        print('Xep loai : YEU')
    
    ## Kiem tra dieu kien thoat chuong trinh :
    thoat = input("Nhap q de thoat chuong trinh, hoac nhap phim bat ki de tiep tuc: ")
    if thoat == 'q' or thoat == 'Q':
        break

    
