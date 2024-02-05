from datetime import date, time, datetime, timedelta
import time

### init date of today :
today = date.today()
### access proverty :
# print(today.day, today.month, today.year)
### access methods :

### init start time of day
# hour = time()
# endHour = time(23, 59, 59)
# print(endHour.hour, endHour.minute, endHour.second)

## init datetime :
dt = datetime(2024, 1, 12, 23, 55, 59)
print(dt.date()) ## get date 
print(dt.time()) ## get time
print(datetime.now()) ## datetime.now() return datetime object

## init datetime object by time string :
# timeString = '01-01-2023' 
# objectdt = datetime.strptime(timeString, '%d-%m-%Y')
dy1 = timedelta(days=10)
dy2 = timedelta(days=5)
print(dy1 -dy2)
# help(timedelta)
