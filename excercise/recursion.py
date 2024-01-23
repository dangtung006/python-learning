def giaithua(n):
    if n == 0:
        return 1
    else:
        return n * giaithua(n - 1)

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


n = int(input("Nhap vao so n: "))

for i in range(1, n+1, 1):
    print(fibo(i), end=" ")
