from datetime import datetime

def getDateObject(dateString):
    return datetime.strptime(dateString, '%Y-%m-%d')

def islessthanBirthDay(dobObj):
    today = datetime.now()
    return (today.month, today.day) < (dobObj.month, dobObj.day)

def cal_age(dob):
    ### dob is date string, example : '1990-01-01'
    dobObj = getDateObject(dob)
    today = datetime.now()
    # if islessthanBirthDay(dobObj) == True:
    #     return today.year - dob.year - 1
    # return today.year - dob.year
    return today.year - dobObj.year - islessthanBirthDay(dobObj)

