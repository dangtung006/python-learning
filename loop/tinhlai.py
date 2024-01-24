### Mỗi người gửi tiết kiệm không kì hạn với số tiền gốc là [A] đồng theo lãi suất 0.3% mỗi tháng. Hỏi sau bao nhiêu tháng thì người đó rút hiết tiền thì sẽ nhận được số tiền ít nhất là [B] đồng. Biết rằng khi gửi tiết kiệm thì lãi suất không được cộng vào vốn.


A = float(input("Nhập vào tiền gốc: "))
B = float(input("Nhập vào số tiền lãi muốn nhận: "))

lai = 0
thang = 0

while lai < B:
    thang+= 1
    lai += A * 0.3/100

print(f"so thang de co so tien lai {B} là: {thang} tháng")

