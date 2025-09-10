#VY 2nd Random Numbers Notes

import random

# Examples of random numbers
print(random.random()) #float between 0 and 1

print(random.randint(1, 6))


name = input("yo whats your name: \n").strip().title()

#Random stat creator for DnD
stat_one = random.randint(1, 10) + random.randint(1, 10)
stat_two = random.randint(1, 10) + random.randint(1, 10)
stat_three = random.randint(1, 10) + random.randint(1, 10)
stat_four = random.randint(1, 10) + random.randint(1, 10)
stat_five = random.randint(1, 10) + random.randint(1, 10)
stat_six = random.randint(1, 10) + random.randint(1, 10)
stat_seven = random.randint(1, 10) + random.randint(1, 10)


print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

strength = int(input("What stat do you want for your Strength?: ")) + 2
