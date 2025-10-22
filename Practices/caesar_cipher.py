#VY 2nd Caesar Cipher
#Create two functions: One will be used for decoding and one will be used for encoding.
    #Inside the functions, have two inputs from the user: one for the shift value, and one for the message itself.
def encode():
    message = input("Give a message you want to encode: ")
    while True:
        shift_value = input("Give a shift value: ") #fail-safe incase user types in a non-integer shifting value
        if not shift_value.isdigit():
            print("Invalid input. Try again.")
        else:
            break
    new_message = "" #create a variable to store the new message
    for char in message: #Loop through the string for each character.
        final_char = ""
        final_num = 0
        if not char.isalpha():
            continue
        else:
            ascii_num = ord(char)
            final_num = ascii_num + shift_value
            if final_num > 122 and char.islower():
                final_num = 97
            elif final_num > 90 and char.isupper():
                final_num = 65
            final_char = chr(final_num)
            
        #new_message += final_char
    return new_message

#Create an input asking for the user if they want to encode or decode.
user_choice = input("Would you like to encode or decode?(e/d):")

#Make an if statement checking if they want to encode or decode.
if user_choice.lower().strip() == "e":
    #If they asked for encoding, run the function for encoding and use the user inputs as the arguments for the parameters.
    #Print out the encoded message.
    print(f"Your encoded message: {encode()}")
else:
    #If they want to decode, get the user's input for the shift value and the message, then use those two values as arguments for the parameters.
    #print out the decoded message.
    print("yum")
