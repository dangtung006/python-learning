name, age, grade = ("John", 23, 17) #### define student info
name, email, phone = ('John Doe', 'john@example.com', '123-456-7890') ### store contact
name, unit, price = ("laptop", 2, 1500) ### store invoice
location = (40.7128, -74.0060)  # New York City's latitude and longitude

# Định nghĩa các hằng số cho màu sắc
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)


#### pass tuple as a param in function:
def calculate_area(rectangle):
    # rectangle là một tuple chứa chiều dài và chiều rộng của hình chữ nhật
    length, width = rectangle
    area = length * width
    return area

# Khai báo một tuple biểu diễn chiều dài và chiều rộng của hình chữ nhật
dimensions = (5, 10)
# Gọi hàm calculate_area và truyền dimensions vào
result = calculate_area(dimensions)

print("Diện tích của hình chữ nhật là:", result)

