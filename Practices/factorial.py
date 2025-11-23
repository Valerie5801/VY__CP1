#VY 2nd Factorial Calculator

#ask user what they want the factorial of
#user_input = input("What number do you want the factorial of?: ")
#add line 1 to list                       #You mean the first line? It's kinda unclear.
#series_nums = [user_input]               #I can't name a list, "list" as it's variable, so I came up with my own name
                                          #Also why do we need a list??
#def get_factorial:
    #number == line1 input
    #total == 1
    #while number >= 0:
        #total *= number
        #number -= 1
        #list.append(number)
def get_factorial(usr_num):               #made it take in a parameter for modularity
    number = int(user_input)              #Must be single equals sign in order for it to be the assignment sign
    total = 1                             #Also must be single equals sign in order for it to be the assignment sign
    while number > 0:                     #This must be strictly if the number is greater than zero to prevent multiplying the total by 0, which will cause the result to always be 0.
        total *= number
        number -= 1
        #series_nums.append(number)       #Wait hold on...why do we need a list?
    return total                          #We have to return/print something from a function!


print("This is a factorial calculator.")

while True:                               #While True loop so user can do as many factorials as they want.
    #ask user what they want the factorial of
    user_input = input("What number do you want the factorial of?(limit of 3 digits): ") #I moved this down here to make the code easier to read and for organization.

    #get_factorial
    print(f"The factorial of {user_input} is...{get_factorial(user_input)}") #I had to rephrase.

    another_factor = input("Do you want to get the factorial of another number?(y/n): ")
    if another_factor == "n":
        print("Thank you for using the factorial calculator.")
        break

#for i in list print "i":                 #What is this for loop's purpose??
    #print("equals", total)
"""for i in series_nums:
    print(i)"""


#print("equals", total)                   #I'd love to know where "total" comes from.




#print final statement                    #What do you mean "print final statement"?
