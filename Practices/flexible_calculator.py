#VY 2nd Flexible Calculator

#define a function with parameters numbers and calculation. numbers should be *args as we don't know how many numbers the user wants to input
def calculator(calculation, *numbers):
    #make a conditional for each option
    if calculation == "sum": #conditional for the sum. Return the total
        print(f"Calculating total of: {numbers}")
        total = 0 #variable for the total
        for number in numbers: #loop through the numbers that user gave
            total += number #add it all to the total
        return f"Total: {total}"
    elif calculation == "average": #return the average if user chose average
        print(f"Calculating average of: {numbers}")
        total = 0 #variable for the total
        for number in numbers:
            total += number
        average = total/len(numbers) #since this is aveage, divide the total by how many numbers there are
        return f"Average: {average}"
    elif calculation == "max": #calculation for the highest number.
        print(f"Calculating max of: {numbers}")
        high_num = 0 #make a variable for the highest number
        for number in numbers:
            if number >= high_num:
                high_num = number #set the high_num variable to the number if the number is the new highest number
        return f"Max: {high_num}" #return the highest value
    elif calculation == "min":
        print(f"Calculating min of: {numbers}")
        low_num = 10000000000000000000000000000000000000000000000 #make a variable for the lowest number. This must be insanely high, so all of the user's numbers should be less than this. This way, the lowest number the user inputted will be assined to this.
        for number in numbers:
            if number <= low_num:
                low_num = number #assign the low_num variable the user's number if it's the lowest so far.
        return f"Min: {low_num}"
    elif calculation == "product":
        print(f"Calculating product of: {numbers}")
        product = 1 #instead of making this zero, make it 1. If we make it zero, the output will always be zero (anything times zero is zero)
        for number in numbers:
            product *= number
        return f"Product {product}"


#greet the user and print out what operations are available. In this case, they should be: sum, average, max, min, and product
print("This is a flexible calculator.")
print("Available operations: sum, average, max, min, product.")

#start a while True loop here to in case the user wants to do multiple calculations
while True:
    #ask they what operation they want to perform
    user_choice = input("What operation do you want to perform?: ")
    all_num = []
    print("Enter numbers(type 'done' when finished): ")
    while True: #another while True loop for an infinite amount of numbers
        user_num = input("Number: ")
        if user_num == "done": #check if the user is done typing in numbers
            break
        if user_num.isalpha(): #fail-safe in case user does not put a number or 'done'
            print("Do a number please.")
        else:
            all_num.append(float(user_num)) #add the number as a float to the empty list. This list will be used as the argument for the function.
    print(calculator(user_choice, *all_num))
    another_calc = input("Do you want to peform another calculation?(yes/no): ")
    if another_calc == "no": #break out of the loop once user is done
        print("Thank you for using the flexible calculator.")
        break
