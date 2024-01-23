### strings is a sequence of characters
### cac tinh chat cua string: ordered(tuan tu), imutable(k the thay doi), text presentation (buoi dien van van)
### Mutation data types : List, dict, set, bytearray
### Imutaion data types: int, float, decimal, string, tuple, range, complex, frozenset, bool, bytes


### create a string :
## use single quotes or double quotes:

greeting = 'hell0 everyone'
greeting_word = "what'sup"

intro = 'I\'m a studen,"a really good student" '
hometown = "I'm from \"VN\""
longText = 'Lorem Ipsum is simply dummy text of the printing \
    and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s,\
    when an unknown printer took a galley of type and \
    scrambled it to make a type specimen book.'

print(intro, hometown)
print(longText)

### access char in string:
mystring = 'I am Tung Dang'
char_4 = mystring[0]
lastChar = mystring[-1]
print(char_4, lastChar)

### Imutable:
try:
    mystring[0] = 'M'
except Exception as Err:
    print(Err)

### Slicing :
myWord = "What's your name?"
print(myWord[:5]) ## cat tu dau den truoc vi tri thu 5
print(myWord[5:]) ## cat tu vi tri thu 5 tro di
print(myWord[1:5]) ### cat tu vi tri thu 1 den truoc vi tri 5
print(myWord[::-1]) ## reverse a string
print(myWord[::2]) ## take every second character : Wa' ornm?

### Concatenate string:

gt = 'Hello everyone'
channel = 'My Channel'
myGrt = gt + ' Welcome you to ' + channel
print(myGrt)

### loop through a string 

myStringForGreeting = 'Xin chao cac ban'

if 'X' in myStringForGreeting:
    print('X found')

# for char in myStringForGreeting:
#     print(char)

### String Method : strip(), title(), upper(), lowercase(), split, reverse, replace, index, find()
ask = 'Can you help me'
changeAsk = ask.replace('me', 'she')
print(changeAsk)

#### Format string: %, format(), f'{}'
## %:
funChannel = 'Fun channel'
myGrtChannel = 'Welcome to my %s' % funChannel
print(myGrtChannel)

pi = 3.14159
s = 'pi number'
myString = "variable is %f from %s" % (pi, s)
print(myString)
## format()
name = 'Tung Dang'
city= 'TN'
height = 1.699669
myIntro = "I'm {} and from {}. I'm {:.3f}".format(name, city, height)
print(myIntro)
## f''
print(f"Hello, I am {name}. I am {height:.2f}")