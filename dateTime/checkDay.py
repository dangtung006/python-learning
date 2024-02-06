from datetime import datetime, time
import pytz
TIME_ZONES = pytz.all_timezones


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

def isGreaterThanCurrent(date, time):
    dateObj = datetime.combine(date.date(), time)
    return dateObj > datetime.now() 

### print(isGreaterThanCurrent(getDateObject("2024-01-30"), time(12, 30)))
# print(TIME_ZONES)

utc_datetime = datetime.utcnow() ### init datetime obj in UTC
utc_now = datetime.now(pytz.utc)

print("utc_datetime", utc_datetime)
print("utc_now", utc_now)
# utc_datetime 2024-02-06 03:44:55.839285
# utc_now 2024-02-06 03:44:55.839285+00:00


NY_TIMEZONE = pytz.timezone("America/New_York")
ny_datetime = utc_datetime.replace(tzinfo=pytz.utc).astimezone(NY_TIMEZONE)

lodonDt = datetime(2024, 1, 1, tzinfo=pytz.timezone('Europe/London'))
nyDt  = lodonDt.astimezone(pytz.timezone('America/New_York'))

print(nyDt)

naive_dt = datetime(2022, 1, 1)
aware_dt = datetime(2022, 1, 1, tzinfo=pytz.timezone('America/New_York'))
utc_aware_dt = aware_dt.astimezone(pytz.utc)

print(f"Naive datetime: {naive_dt}")
print(f"Aware datetime: {aware_dt}")
print(f"UTC Aware datetime: {utc_aware_dt}")


