import string
import random
LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def gen_password(length = 8):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
    printable = list(printable)
    random.shuffle(printable)
    randomPass = random.choices(printable, k=length)
    randomPass = "".join(randomPass)
    return randomPass

def main():
    lenthPass = int(input("How long do you want your password: "))
    genPass = gen_password(lenthPass)
    print(genPass)


if __name__ == '__main__':
    main()
