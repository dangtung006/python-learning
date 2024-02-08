from pprint import pprint
from collections import ChainMap
capital_1 = {
    "VN" : "Ha Noi",
    "ThaiLand" : "Bangkok"
}

capital_2 = {
    'England' : 'London',
    'France' : 'Paris'
}

# capital_1.update(capital_2)
# pprint(capital_1)

# capital_copy = capital_1.copy()
# capital_copy.update(capital_2)
# print(capital_copy)

### unpack operator :
capitals = { **capital_1, **capital_2}
print(capitals)

### pipe operator 
age_1 = {
    "Peter" : 30,
    'John' : 21
}

age_2 = {
    "Bob" : 25,
    "Alice" : 32,
    'Peter' : 50
}

merege_age = age_1 | age_2
chainAge = dict(ChainMap(age_1, age_2))
print(merege_age)
print(chainAge)