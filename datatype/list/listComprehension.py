#[<action> for <item> in <iterator> if<some condition>]

list_1 = [1, 2, 4, 5, 7, 8]

def makeNewList_1():
    newList = []
    for num in list_1:
        newList.append(num * num)
    return newList

def makeNewList_1_v2():
    return[num **2 for num in list_1]

def makeEvenList():
    newList = []
    for num in list_1:
        if num % 2 == 0:
            newList.append(num)
    return newList

def makeEvenListV2():
    return [num for num in list_1 if num % 2 ==0]

list_text = ['apple', 'banana', 'pinaple', 'melon']

def makeTitleList():
    return [text.title() for text in list_text]

def findListItemInclude_a():
    return [text for text in list_text if 'a' in text]

def convertStringToList(words):
    return [word for word in words]

transactions = [100, 200, 350, 500]
TAX_RATE= 0.08
SERVICE_CHARGE = 0.07

def getTotal_price(price):
    return price * (1 + TAX_RATE + SERVICE_CHARGE)

def makeTotalPrices(bills) :
    return [getTotal_price(bill) for bill in bills ]


# print(makeNewList_1_v2())
# print(makeEvenListV2())
# print(makeTitleList())
# print(findListItemInclude_a())
# print(convertStringToList("Hi Everyone"))

print(makeTotalPrices(transactions))