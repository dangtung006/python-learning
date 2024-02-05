from datetime import datetime
crr_date = datetime.now()

## default formate date time (ISO 8601) : 2024-02-05 14:26:14.659346 (YYYY-MM-DD HH:MM:SS.mmmmmmm)
### format type note : 

# %d return the day of month 01 to 31
# %m return the month of year 01 to 12
# %Y return the year in 4-digit format
# %y return the year in 2-digit format

# %A return the full name of the weekday
# %a return  the short name of the weekday
# %B return the full name of month
# %b return the short name of month

# %H return the hour in 24-hour format
# %I return the hour in 12-hour format
# %M return the minute (00 to 59)
# %S return the second (00 to 50)
# %f return the 6-digit microsecond (000000- 999999)


DATE_FORMAT_1 = '%d-%m-%Y'
DATE_FORMAT_2 = '%d/%m/%Y'
DATE_TIME_FORMAT_1 = '%H:%M:%S %d-%m-%Y'
DATE_TIME_FORMAT_2 = '%H:%M:%S %d/%m/%Y'
DAY_DATE_FORMAT = '%A, %d/%m/%Y'
EXACTLY_DATE_TIME_FORMAT = 'at %H:%M:%S on %d.%m'

def getTimeString(date, format=DATE_FORMAT_1) -> str:
    if isinstance(date, datetime) == False:
        raise TypeError("Invalid date time")
    return date.strftime(format)

print(getTimeString(crr_date))
# print(getTimeString(crr_date, DATE_TIME_FORMAT_1))
# print(getTimeString(crr_date, DAY_DATE_FORMAT))
# print(getTimeString(crr_date, EXACTLY_DATE_TIME_FORMAT))