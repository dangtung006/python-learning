import time

timstmp = time.time() ## return current time (floating point number) in seconds from the epoch

dateString = time.ctime(timstmp) ## receive a time in second and return a string in local time
print(dateString, type(dateString)) 
localTime = time.localtime(timstmp) ## receive a time in second and return a tuple expressing local time
print(localTime) 

mKtime = time.mktime(localTime)  
print(mKtime)  
    ###mktime(tuple) -> floating point number Convert a time tuple in local time to seconds since the Epoch.

ascTime = time.asctime(localTime)
print(ascTime)
    # asctime([tuple]) -> string
    # Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
    # When the time tuple is not present, current time as returned by localtime()
    # is used.

formatedTime = time.strftime('%d/%m/%Y')
print(formatedTime)   
    # strftime(format[, tuple]) -> string
    # Convert a time tuple to a string according to a format specification.
strPtime = time.strptime("01/01/2023", '%d/%m/%Y')
print(strPtime)
    # strptime(string, format) -> struct_time
    # Parse a string to a time tuple according to a format specification.
# help(time.strptime)