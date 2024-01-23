words = """
    Toi cham hoc
    Toi chiu kho
    Toi dep trai
"""

count = 0

for i in range(len(words)):
    if words[i] == 'T' and words[i+1] == 'o' and words[i + 2] == 'i':
        count += 1

print(count)