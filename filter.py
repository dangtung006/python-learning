source = ["python" , "js", '3', '0', "New York", '1']

numlist = filter(lambda item: item.isdigit(), source)
wordlist = filter(lambda item: item.isalpha(), source)

print(list(numlist), list(wordlist))

persons = [('tung', 18), ('hung', 21), ('hang', 20)]

olderthan18 = filter(lambda item: item[1] > 18, persons)
print(list(olderthan18))


countries = [
    ('Vietnam' , 'Asia', 5000),
    ('Laos' , 'Asia', 2000),
    ('China', 'Asia', 11800)
]


asiaCountries = filter(lambda item: item[1] == 'Asia', countries)
print(list(asiaCountries))
asiaAndGreaterthan5000 = filter(lambda item: item[1] == 'Asia' and item[2] > 5000, countries)
print(list(asiaAndGreaterthan5000))

group_3 = filter(lambda item: item[1] == 'Asia' and (5000 <= item[2] <= 20000), countries)

