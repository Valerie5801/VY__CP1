#VY 2nd Average Grade

pe = float(input("What is your grade in P.E.?: "))
computer_science = float(input("What is your grade in Computer Science?: "))
math = float(input("What is your grade for Math?: "))
english = float(input("What is your grade in English?: "))
chemistry = float(input("What is your grade in Chemistry?: "))
health = float(input("What is your grade in Health?: "))

total = pe + computer_science + math + english + chemistry + health
average = total/7

print("Your average grade across all classes is", round(average, 2))