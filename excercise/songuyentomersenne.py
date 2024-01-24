## Kiem tra so nguyen to mersenne:

def ktraSNT(x):
    if(x < 2) : return False
    
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
        
    return True

### check x  = 2 ** n + 1 ???

def isMersenne(x):
    x += 1
    i = 1

    while 2 ** i < x:
        i+= 1
    return x == 2 ** i

for i in range(1000):
    if ktraSNT(i) and isMersenne(i):
        print(i, end= " ")