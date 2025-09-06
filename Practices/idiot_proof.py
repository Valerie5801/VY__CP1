#VY 2nd Idiot Proof

full_name = input("What is your full name?: ").strip().title()
phone_one = input("What are the first three digits of your phone number?:")
phone_two = input("What are the second three digits of your phone number?:")
phone_three = input("What are the last three digits of your phone number?:")
gpa = round(float(input("What is your GPA?: ")), 1)

phone_number = phone_one + " " + phone_two + " " + phone_three



print(f"Your name is {full_name}, your phone number is {phone_number}, and your GPA is currently {gpa}.")
