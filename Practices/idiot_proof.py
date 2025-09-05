#VY 2nd Idiot Proof

while True:
    full_name = input("What is your full name?: ")
    phone_number = input("What is your 9 digit phone number?(don't use dashes or spaces): ")
    gpa = input("What is your GPA?: ")

    check_name = full_name.isalpha()
    check_number = phone_number.isdigit()
    check_gpa = gpa.isdecimal()

    while check_name == False:
        if check_name == True:
            full_name = full_name.strip().title()
            break
    else:
        print("invalid name")

    while check_number == False:
        if check_number == True:
            phone_number = int(phone_number)
            break
    else:
        print("thats not a phone number")

    while check_gpa == False:
        if check_gpa == True:
            gpa = round(float(gpa), 1)
            break
    else:
        print("wah")

    print(f"Your name is {full_name}, your phone number is {phone_number}, and your GPA is currently {gpa}.")
