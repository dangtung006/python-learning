### join only string , not number
python = "".join(['p', 'y', 't', 'h', 'o' , 'n'])
print(python)

a = "Hello"
b = "world"
sentence = " ".join([a, b])
print(sentence)

phone = "-".join(["062", "3", "81", "3064", "3385"])
print(phone)


def makeTriangleSymbol():
    n = int(input("Enter a number : "))
    symbol = input("Enter a symbol : ")
    shape = '\n'.join(symbol * i for i in range(n))
    print(shape)


lst = ["1", "2", "4", "hero", "money", "5"]
numbers = " >> ".join(item for item in lst if item.isdigit())
chars = " ## ".join(item for item in lst if item.isalpha())
print(numbers, chars)

### concate string with fstring format
sub_1 = "Math"
sub_2 = "History"

print(f'My favorite subjects are : {sub_1} , {sub_2}')

myStar = "*"
my50Star = myStar* 50
print(my50Star)