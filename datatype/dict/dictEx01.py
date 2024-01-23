## check an string is an unique string
def unique(str):
    char_set = {}
    for char in str:
        if char in char_set:
            return False
        char_set[char] = True
    return True

print(unique("asdc"))
print(unique("asdca"))