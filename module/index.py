#special variable python : __name__ , __package__ , __file__ , __spec__ , __doc__ , __loader__, __cached__ , builtins__

from myModule import greetOne, person, Person
from utils.email import splitEmail, logEmail, makeInputEmail, TEST_EMAILS
from utils.format import fomatWithDecimals, decimal_format, decimal_format_2, PERCENT_FORMAT, PERCENT_2_FORMAT, roundDown_format, roundUp_format

# from utils import email as emailUtil
# from email import splitEmail, logEmail, makeInputEmail, TEST_EMAILS

if __name__ == '__main__':
    print(fomatWithDecimals(1.23444, decimal_format(2)))
    print(fomatWithDecimals(123444, decimal_format_2(2)))
    print(fomatWithDecimals(1.23444, roundUp_format(3)))
    print(fomatWithDecimals(0.8, PERCENT_2_FORMAT))

    # email = makeInputEmail()
    # result = splitEmail(email)
    # logEmail(result[0], result[1])

    # for email in TEST_EMAILS:
    #     result = splitEmail(email)
    #     logEmail(result[0], result[1])

    # greetOne("Tung Dang")
    # print(f'Hi my name is {person["name"]}, Im {person["age"]} years old')
    # newPerson = Person("Tung Dang", 21)
    # newPerson.hello()
