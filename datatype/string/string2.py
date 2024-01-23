result = "English = 78 Science = 83 Math = 68 History = 65"
stringList = result.split(" ")
print(stringList)
s = 0
count = 0

for i in stringList:
    if i.isdigit():
        i = float(i)
        s+= i
        count += 1

print(s, count)