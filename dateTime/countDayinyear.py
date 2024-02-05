from datetime import (
    date, datetime, timezone, time, UTC
) 

## weekday() is method of class date return the day in week. 0-monday ... 6 sunday
day = 13
year = int(input("Nhap vao 1 nam: "))
result = []

for month in range(1, 13):
    if date(year, month, day).weekday() == 4:
        result.append(date(year, month, day))

print(f"There {'is' if len(result) == 1 else 'are'} {len(result)} 'Friday the 13th' in the year {year}")
for dateF in result:
    print(dateF.strftime('%d-%m-%Y'))




