ls = [133, 24, 56, 68, 3, 98, 56]
num_odd = sum([num % 2 != 0 for num in ls])
print(num_odd)

myGreeting = "Hello Python Programmer"
vowel_chars = sum(letter in 'aoueiy' for letter in list(myGreeting))
print(vowel_chars)

ls_words = ["zebra", "duck", "chicken", "dog", "rabbit", "crocodile"]
sum_counts = sum([len(animal) > 4 and (sum(letter in 'aoueiy' for letter in list(animal)) >=3) for animal in ls_words])
print(sum_counts)

#### compare :
numbers = [1, 3, -5, 6, 8, -4]

positive_count = sum(num > 0 for num in numbers)
positive_total = sum(num for num in numbers if num > 0)

print(positive_count, positive_total)


