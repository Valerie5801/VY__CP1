#VY 2nd For Loops Notes

import time


nums = [6, 51, 61, 94, 351, 946, 5489, 4, 654, 684]

for num in nums:
    div = num/2
    if div > 100:
        print(f"{div} is half of {num}, and it's still big.")
    else:
        print(num)

print("WONDERHOY\n")
time.sleep(3)

for i in range(1, 10): #Range is not inclusive, so it leaves out 10
    print(i)
time.sleep(3)

print("\ncount by twos")
for x in range(2, 11, 2): #The third argument tells the computer what to count by
    print(x)
time.sleep(3)

print("\nNwod tnuoc") #Count down. The default for counting is 1. To count backwards you do -1.
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("happy new year or 5th annversary who am i kidding only the latter is here")