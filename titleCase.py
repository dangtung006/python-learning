import string
### bulid in func
def my_capwords(sentence: str) -> str:
    sentence = sentence.split()
    sentence = " ".join( word[0].upper() + word[1:].lower() for word in sentence)
    return sentence


sentence = "i'm ZeRo, You're my ]-[eRo"
print(my_capwords(sentence))
print(string.capwords(sentence))