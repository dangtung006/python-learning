# n = ax + by, goi x la so buoc nhay ngan, y la so buoc nhay dai
## y can phai max sao cho n xap xi bang b * y

n = 21
a = 2
b = 5
tongsobuocnhay = 0
minstep = 0
maxstep = 0

for y in range(n//b, -1, -1 ):
    
    totalMin = n - b*y    ## tong so buoc nhay ngan

    if totalMin % a == 0:
        minstep =  totalMin // a  
        maxstep = y
        tongsobuocnhay = maxstep + minstep 
        break

    
print(tongsobuocnhay, maxstep, minstep)
