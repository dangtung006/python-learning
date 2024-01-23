def giaiThuaV1(n):
    gt=1

    if(n == 1 or n == 0):
        return gt
    else:
        for i in range(2, n+1):
            gt = gt * i
        return gt
    
def giaiThuaV2(n):
    if(n == 0):
        return 1
    else:
        return n * giaiThuaV2(n - 1 )

n = int(input("Nhap vao so nguyen duong n = "))
print(f"giai thua cua {n} bang:  ", giaiThuaV2(n))