import os

path='user/'

def isFile(dir):
    return os.path.isfile(dir)

def isFolder(dir):
    return os.path.isdir(dir)

def joinPath(path_1, path_2):
    return path_1 + os.sep + path_2

def readFileContent(file):
    f = open(file,'r',encoding = 'utf-8')
    # a = f.readline()
    # b = f.readline()
    # c = f.readline()
    d = f.readlines()
    print(d)

def writeFile(file, content):
    file = open(file, "w")
    file.write(content + '\n')
    # Đóng file
    file.close()

def writeAppend(file, content):
    file = open(file, "a")
    l = ['test-4 \n']
    file.writelines(l)
    # Đóng file
    file.close()

# read file
# readFileContent("user/demo.txt")
    
# write file
# writeFile("user/demo.txt", "python demo -3")
writeAppend("user/demo.txt", "python demo -5")

# join path
print(joinPath('user', "demo.txt"))
print(isFile(joinPath('user', "demo.txt")))

# check folder
print(isFolder(path))

# check file
fileList= os.listdir(path)

for f in fileList:
    filePath = os.path.join(path, f)
    print(filePath)
    print(isFile(filePath))

