#VY 2nd While Loop Notes
import time
import random

#Infinite
num = 0
break_out = random.randint(1, 50)
while num < 20:
    num += 1 #fix loop
    if num == break_out:
        break
    elif num%2 == 0:
        continue
    print(f"wonderhoy #{num}")
    time.sleep(0.05)
else:
    print("Sunny")

print("something is behind you")