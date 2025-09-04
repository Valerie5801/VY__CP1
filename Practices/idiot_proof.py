#VY 2nd Idiot Proof

full_name = input("What is your full name?: ")
phone_number = int(input("What is your phone number?(don't use dashes or spaces): "))
gpa = input("What is your GPA?: ")

check_name = full_name.isalpha()
check_number = phone_number.isdigit()
check_gpa = gpa.isdecimal()

if check_name == False:
    full_name = full_name.strip().title()

print(f"Your name is {full_name}, your phone number is {phone_number}, and your GPA is currently {gpa}.")