# Required Parameter and default parameter:

def makeWelcome(name, greeting):
    print(f'{name}, {greeting}')

def makeWelcome_v2(name, greeting = "Welcome to my channel"):
    print(f'{name}, {greeting}')

def countTotals(a, b, c):
    print(a, b, c)
    print(a+b+c)

#varible-length parameter
# *args use to pass any positional argument to yours fn
# **args use to pass any keyword argument to yours fn
    
def makeReq(req, res, *args, **kwargs):
    print(req, res)

    for arg in args:
        print(arg)

    for key, val in kwargs.items():
        print(f'key {key} has val= {val}')

makeWelcome_v2("Hai Nam")
#position Argument
countTotals(1, 3, 5)
#keyword Argument
countTotals(a=3, b=1, c=5)
makeReq([1], [2], 'Object', 1, 4, 5.6, time="aaa", day="ccc")

