def getFormattedName(fstname, lstname):
    fullname = f"{fstname} {lstname}"
    return fullname.title()


while True:
    print("\n Please tell me your name")
    print("(print 'q' at any time to quit)")

    f_name = input("First name :  ")

    if f_name == 'q' :
        break

    l_name = input("Last name :  ")

    if f_name == 'q' :
        break

    print(f'\n Hello , {getFormattedName(f_name, l_name)}')
