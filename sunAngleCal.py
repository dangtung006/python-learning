time = input("Enter time of day: ")

hour, minutes = map(int, time.split(":"))
DEEGREE_SIGNAL = chr(176)
ONE_MINUTE_ANGLE = 180/720

if time == "18:00" :
    angle = 180
    print(f"Sun angle is {angle}{DEEGREE_SIGNAL}. It's the last minute to see the sun!")

elif hour > 18 or hour < 6:
    print("There is no sun to calculate angle")

else:
    time_in_minutes = (hour - 6) * 60 + minutes
    angle = time_in_minutes * ONE_MINUTE_ANGLE
    print(f'Sun angle is {angle}{DEEGREE_SIGNAL}')
