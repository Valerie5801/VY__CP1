#VY 2nd Squared Numbers

#make a list of numbers to square
numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]

squared = list(map(lambda num: num**2, numbers)) #use map and lambda to make a list of squared numbers easily. convert this into a list.
for i in range(len(numbers)): #make a for loop that goes the length of the numbers list.
    print(f"Original Number: {numbers[i]}, Squared: {squared[i]}") #use i as the index number. The number from the squared list should correspond to the number in the numbers list as they are the same length and use the same index number.