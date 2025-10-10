#VY 2nd Password Strength

#1. Create a while True loop (in case if the user would like to check multiple passwords)
while True:
    print("I can check the strength of your password based on a scale of 1-5 using this criteria: \n-Password contains at least least 8 characters \n-Password contains at least one uppercase letter \n-Password contains at least one lowercase letter \n-Password contains at least one number \n-Password contains at least one special character")
    #2. Create a variable called "strength_score" and set it to 0. This will be the variable that keeps track of how strong the user's passwords are.
    strength_score = 0
    #3. Create five variables, each currently set to False. Each variable will keep track of one of five conditions: Length, if the password has uppercase letters, if the password has loewrcase letters, if the password has numbers, and if the password has special characters.
    length_pass = False
    upper_pass = False
    lower_pass = False
    num_pass = False
    special_pass = False
    #4. Make a list of characters that are considered "special characters"
    special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "+", "="]
    #5. Get a string input from the user asking for a password they would like to check.
    user_pass = input("Give me a password for me to check: ")
    #6. Make a for loop that loops through the string. 
    for char in user_pass:
        #7. Inside said for loop, check what data type is the character. 
            #If we are checking for if the character is an uppercase, and it is an uppercase letter, make the variable keeping track of uppercase letters True. Do this for the rest of the three conditions, and for the rest of the string.
        if char.isupper():
            upper_pass = True
        if char.islower():
            lower_pass = True
        if char.isdigit():
            num_pass = True
        if char in special_chars:
            special_pass = True

    #8. After finishing the for loop, check the length of the password by using the len() method. If it has more than 8 characters (including spaces), make the variable that is keeping track of length True.
    len_check = len(user_pass)
    if len_check >= 8:
        length_pass = True

    #9. After checking the length, look at the variables holding booleans. For each variable that holds True, add 1 to strength_score.
    if length_pass:
        strength_score += 1
    if upper_pass:
        strength_score += 1
    if lower_pass:
        strength_score += 1
    if num_pass:
        strength_score += 1
    if special_pass:
        strength_score += 1
        
    #10. After adding up the score, print out strength_score and make a conditional to print out one of four things:
        #If strength_score is less than or equal to 2, show "Password strength: Weak."
        #If strength_score is 3, show "Password strength: Moderate."
        #If strength_score is 4, show "Password strength: Strong."
        #If strength_score is 5, show "Password strength: Very Strong."
    #Bonus: Check if the password is deemed weak. If so, check in what areas is it lacking in (what variables are still False), and print out suggestions based on it to make the password stronger.
        #Example: If the password does not have special characters, print out, "Try adding a special character."
    #11.A Ask the user if they want to check another password.
        #If the user says they want to exit, show "Goodbye", and break out of the loop.
        #If the user says they want to check another password, run another loop.