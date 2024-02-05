from datetime import datetime
crr_date = datetime.now()

## default formate date time (ISO 8601) : 2024-02-05 14:26:14.659346 (YYYY-MM-DD HH:MM:SS.mmmmmmm)
### format type note : 

# %d return the day of month 01 to 31
# %m return the month of year 01 to 12
# %Y return the year in 4-digit format
# %y return the year in 2-digit format

DATE_FORMAT_1 = '%d-%m-%Y'
DATE_FORMAT_2 = '%d/%m/%Y'
DATE_TIME_FORMAT_1 = ''




def getTimeString(date, format=DATE_FORMAT_1):
    return date.strftime(format)

print(getTimeString(crr_date))