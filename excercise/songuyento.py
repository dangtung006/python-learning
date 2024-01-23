import math

def isPrimeNumber(n):
    if( n < 2 ) :
        return False
    
    canbacHai = int(math.sqrt(n))

    for i in range(2, canbacHai + 1):
        if(n % i == 0):
            return False  
        
    return True

# n= int(input("Nhap vao 1 so nguyen: "))
# print(f"{n} la so nguyen to: ", isPrimeNumber(n))
