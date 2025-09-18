#VY 2nd Booleans Notes

import time
import datetime as date

over = False
print(over)

name = "Aubrey"
print(bool(name))

zero = 0
print(bool(zero))

current_time = time.time()
readable_time = time.ctime(current_time)

print(f"Current Time in seconds since January 1, 1970(epoch time): {current_time}")
print(f"Current Time: {readable_time}")

now = date.datetime.today()
hour = now.hour()

# Month = %m (%b, %B)
# day = %d
# Year = %Y or %y
# hour = %H
# minutes = %M
# Seconds = %S


print(f"Current time according to datetime: {now}")
print(f"Hour: {hour}")

print(f"My hour variable is a String: {isinstance(hour, str)}")