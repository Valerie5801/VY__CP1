#VY 2nd Factorial Calculator

#ask user what they want the factorial of
user_input = input("What number do you want the factorial of?: ")
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
def get_factorial():
    number = int(user_input)              #Must be single equals sign in order for it to be the assignment sign
    total = 1                             #Also must be single equals sign in order for it to be the assignment sign
    while number > 0:                     #This must be strictly if the number is greater than zero to prevent multiplying the total by 0, which will cause the result to always be 0.
        total *= number
        number -= 1
        #series_nums.append(number)       #Wait hold on...why do we need a list?
    return total                          #We have to return/print something from a function!


#get_factorial
print(f"It's factorial is...{get_factorial()}") #I had to rephrase.

#for i in list print "i":                 #What is this for loop's purpose??
    #print("equals", total)
"""for i in series_nums:
    print(i)"""


#print("equals", total)                   #I'd love to know where "total" comes from.




#print final statement                    #What do you mean "print final statement"?
