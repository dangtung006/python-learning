num = '12'
n = 4
stri = '12'
for i in range(n-1):
    totalPow2 = sum([int(i)**2 for i in num])
    num = f'{totalPow2}'
    stri += f' {num}'

print(stri)
