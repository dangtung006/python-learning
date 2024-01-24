# so dac biet : aNb = k * N , tim N

k = 91
a = 4
b = 5
n = 0
multiple  = None

while multiple != k * n:
    n+=1
    multiple = int(f'{a}{n}{b}')
 
print(f'so can tim la N = {n}')