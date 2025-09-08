#VY 2nd Formattng Outputs Notes

name = "Jake"
age = 21
grade = .75
money = 25
print("Hello {}, nice 2 meet you i guess. You are very old because you are {:E} years old. You have {:%} grade. You have ${:.2f}, thats money.".format(name, age, grade, money))

#f-string
print(f"Hello {name}, nice 2 meet you i guess. You are very old because you are {age:E} years old. You have {grade:%} grade. You have ${money:.2f}, thats money.")