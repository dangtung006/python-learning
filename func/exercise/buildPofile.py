def buildProfile(first, last, **userInfo):
    userInfo['firstname'] = first
    userInfo['lastname'] = last
    return userInfo

user = buildProfile("tung", "dang", hometown="TN", dob="9/6/69")
print(user)
