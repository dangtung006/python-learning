from time import perf_counter

def fib(n):
    if n < 2:
        return n
    return fib(n -1) + fib(n -2)


startTime = perf_counter()
print(fib(30))
endTime = perf_counter()
print(f"time elaps in {endTime - startTime} s")