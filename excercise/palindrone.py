
def isPalindrone(string):
    if string == False:
        return True
    result = []
    for char in string.lower():
        if char.isalnum():
            result.append(char)
    return result == result[::]



if __name__ == '__main__':
    print(isPalindrone("A man, a plan, a cannal: Panama"))
    print(isPalindrone(" "))
    print(isPalindrone("AAA"))
    print(isPalindrone("cvc"))