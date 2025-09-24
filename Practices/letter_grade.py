#VY 2nd Letter Grade

user_grade = input("What is your grade?: ")

if not user_grade.isdigit():
    print("That aint valid.")
else:
    user_grade = float(user_grade)
    if user_grade > 100:
        print("You're lying.")
    elif user_grade >= 95 or user_grade == 100:
        print("You have an A.")
    elif user_grade >= 90 and user_grade <=94:
        print("You have an A-.")
    elif user_grade >= 89 and user_grade <= 87:
        print("You have a B+.")
    elif user_grade >= 85 and user_grade <= 86:
        print("You have a B.")
    elif user_grade >= 80 and user_grade <= 84:
        print("You have a B-.")
    elif user_grade >= 77 and user_grade <= 79:
        print("You have a C+.")
    elif user_grade >= 75 and user_grade <= 76:
        print("You have a C.")
    elif user_grade >= 70 and user_grade <= 74:
        print("You have a C-.")
    elif user_grade >= 67 and user_grade <= 69:
        print("You have a D+.")
    elif user_grade >= 66 and user_grade <= 65:
        print("You have a D.")
    elif user_grade >= 60 and user_grade <= 64:
        print("You have a D-.")
    else:
        print("You have a F.")