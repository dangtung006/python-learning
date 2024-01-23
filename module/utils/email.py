TEST_EMAILS = ['tungdang@gmail.com', 'xuantocdo@gmail.com.vn', 'thangty@sayruou.com']

def splitEmail(email):
    emailname = email[0:email.index('@')]
    emaildomain = email[email.index('@')+1:]
    return [emailname, emaildomain]

def logEmail(emailname, emaildomain):
    print(f'email name is {emailname.upper()} with domain is {emaildomain.upper()}')

def makeInputEmail():
    return input("nhap vao email: ").strip()