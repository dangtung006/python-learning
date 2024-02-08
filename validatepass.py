import re

def check_digit(pwd: str) -> bool:
    return bool(re.search(r'[0-9]', pwd))

def check_uppercase(pwd: str) -> bool:
    return bool(re.search(r'[A-Z]', pwd))

def check_lowercase(pwd: str)-> bool:
    return bool(re.search(r'[a-z]', pwd))

def check_special_char(pwd: str)-> bool:
    return bool(re.search(r'[~!@#$%^&?]', pwd))

def check_white_space(pwd: str)-> bool:
    return bool(re.search(r'\s', pwd))

def check_len(pwd: str)-> bool:
    # return True if len(pwd) >= 6 and len(pwd) <=12 else False
    return 6 <= len(pwd) <= 12


def main():
    yourpass = input("Chose youre password: ")

    if all([
        check_digit(yourpass),
        check_lowercase(yourpass),
        check_uppercase(yourpass),
        not check_white_space(yourpass),
        check_special_char(yourpass),
        check_len(yourpass)
    ]):
        print("Your password are so strong")
    
    else:
        print("Your password has not met the following requirements: ")

        if not check_digit(yourpass):
            print("-Your password must have at least (0-9)")

        if not check_lowercase(yourpass):
            print("-Your password must have at least one upper-case letter (A-Z)")

        if not check_uppercase(yourpass):
            print("-Your password must have at least one lower-case letter (a-z)")

        if not check_special_char(yourpass) :
            print("-Your password must have at least one special character (~!@#$%^&?)")

        if check_white_space(yourpass):
            print("-Your password must not contain white space character")

        if check_len(yourpass):
            print("-Your password length must be at 6 character and most 12 character (0-9)")

main()