#VY 2nd Basic Calculator

print("I can do addition, subtraction, multiplication, division, exponents, integer division, or modulo.")
while True:
    equation_select = input('What equation would you like me to do?(type "quit" to stop): ')
    if equation_select.lower().strip() == 'quit': #terminating the program
        print("Goodbye.")
        break 
    else:
        print("Alright then.")
        input_one = int(input("Give me an integer: "))
        input_two = int(input("Give me another integer: "))
        addition = input_one + input_two
        subtraction = input_one - input_two
        multiplication = input_one * input_two
        division = round(input_one/input_two, 2)
        exponents = input_one**input_two
        int_division = input_one//input_two
        modulo = input_one%input_two
        
        if equation_select.lower().strip() == 'addition':
            print(f"{input_one} + {input_two} = {addition}")
        elif equation_select.lower().strip() == 'subtraction':
            print(f"{input_one} - {input_two} = {subtraction}")
        elif equation_select.lower().strip() == 'multiplication':
            print(f"{input_one} * {input_two} = {multiplication}")
        elif equation_select.lower().strip() == 'division':
            print(f"{input_one} / {input_two} = {division}")
        elif equation_select.lower().strip() == 'exponents':
            print(f"{input_one} ** {input_two} = {exponents}")
        elif equation_select.lower().strip() == 'integer division':
            print(f"{input_one} // {input_two} = {int_division}")
        elif equation_select.lower().strip() == 'modulo':
            print(f"{input_one} % {input_two} = {modulo}")    