list_1 = ["hello", 1, "python", 2, "coders", 3]
result = sorted([item for item in list_1 if type(item) == int]) + sorted([item for item in list_1 if type(item) == str])
print(result)

ls_sentence = [
    "a bit longer",
    "I'm the longest",
    "shortest",
    "me much longer"
]

print(sorted(ls_sentence, key=len))


ls_dolar = ["more$$$" , "give$", "me$$" , "money$$$$"]
ls_dolar.sort(key= lambda item: item.count("$"))

print(ls_dolar)

### sort muliple condidions :
name_list = [
    ("Alex" , "Demina"),
    ("Brian" , "Taylor"),
    ("Alex" , "McKay"),
    ("Brian" , "Dennis")
]

result_sortName = sorted(name_list, key=lambda name: (name[0], name[1]))
print(result_sortName)

lst_G_and_dolar  = ["$$$$GGGG", "GGG$$$", "$G$", "G$" ]
lst_G_and_dolar.sort(key=lambda item: (item.count("$"), item.count("G")))
print(lst_G_and_dolar)



