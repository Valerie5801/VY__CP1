#VY 2nd Caesar Cipher
#Create two functions: One will be used for decoding and one will be used for encoding.
    #Inside the functions, have two inputs from the user: one for the shift value, and one for the message itself.
def encode():
    message = input("Type a message you want to encode: ")
    while True:
        shift_value = input("Give a shift value: ") #fail-safe incase user types in a non-integer shifting value
        if not shift_value.isdigit():
            print("Invalid input. Try again.")
        else:
            shift_value = int(shift_value)
            break
    new_message = "" #create a variable to store the new message
    for char in message: #Loop through the string for each character.
        final_char = ""
        if not char.isalpha(): #accomodate for any non-letter character
            new_message += char
            continue
        else:
            ascii_num = ord(char) + shift_value
            if ascii_num > 122 and char.islower(): #make it so that it wraps around the alphabet if we go past Z or z.
                ascii_num = 97
            elif ascii_num > 90 and char.isupper():
                ascii_num = 65
        final_char = chr(ascii_num)
        new_message += final_char
    return new_message

def decode():
    message = input("Type a message you want to decode: ")
    while True:
        shift_value = input("Give a shift value: ") #fail-safe incase user types in a non-integer shifting value
        if not shift_value.isdigit():
            print("Invalid input. Try again.")
        else:
            shift_value = int(shift_value)
            break
    new_message = "" #create a variable to store the new message
    for char in message: #Loop through the string for each character.
        final_char = ""
        if not char.isalpha(): #accomodate for any non-letter character
            new_message += char
            continue
        else:
            ascii_num = ord(char) - shift_value #Since this is decoding, we must go backwards.
            if ascii_num < 97 and char.islower(): #make it so that it wraps around the alphabet if we go past A or a.
                ascii_num = 122
            elif ascii_num < 65 and char.isupper():
                ascii_num = 90
        final_char = chr(ascii_num)
        new_message += final_char
    return new_message


while True: #Make a while True statement so the user can use the program as many times as they want and can choose to exit whenever they want.
    #Create an input asking for the user if they want to encode or decode.
    user_choice = input("Would you like to encode or decode?(e/d): ")

    #Make an if statement checking if they want to encode or decode.
    if user_choice.lower().strip() == "e":
        #If they asked for encoding, run the function for encoding and use the user inputs as the arguments for the parameters.
        #Print out the encoded message.
        print(f"Your encoded message: {encode()}")
    else:
        #If they want to decode, get the user's input for the shift value and the message, then use those two values as arguments for the parameters.
        #print out the decoded message.
        print(f"Your decoded message: {decode()}")
    
    user_cont = input("Would you like to try another message?(y/n): ") #Ask the user if they want to try another message
    if user_cont == "y":
        continue
    elif user_cont == "n":
        print("Goodbye.")
        break
