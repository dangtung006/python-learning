nums = [1, 2, 3, 6 , 7, 8]
odd = filter(lambda x : x % 2 == 0, nums)
even = filter(lambda x : x % 2 != 0, nums)

print(list(odd))
print(list(even))