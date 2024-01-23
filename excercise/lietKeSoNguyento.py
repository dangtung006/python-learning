from songuyento import isPrimeNumber

def listPrimeNumslessthanN(n):

    result=""
    if(n >= 2):
        result = result + "2" + " "
        for i in range(3, n + 1):
            if(isPrimeNumber(i)):
                result = result + str(i) + " "
    
    print(result)


n = int(input("Nhap vao so nguyen duong n = "))
listPrimeNumslessthanN(n)