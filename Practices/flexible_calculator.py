#VY 2nd Flexible Calculator

#define a function with parameters numbers and calculation. numbers should be *args
def calculator(*numbers, calculation):
    #
    if calculation == "sum":
        total = 0
        for number in numbers:
            total += number
        average = total/len(numbers)

#greet the user and print out what operations are available. In this case, they should be: sum, average, max, min, and product
print("This is a flexible calculator.")
print("Available operations: sum, average, max, min, product.")

#start a while True loop here to in case the user wants to do multiple calculations
while True:
    #ask they what operation they want to perform
    user_choice = input("What operation do you want to perform?: ")
    nums_choice = [] #make an empty list as the parameter for numbers
    while True: #another while True loop for an infinite amount of numbers
        print("Enter numbers(type 'done' when finished): ")
        user_num = input("Number: ")
        if user_num == "done": #check if the user is done typing in numbers
            break
        else:
            nums_choice.append(user_num)
        
