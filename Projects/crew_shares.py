#VY 2nd Crew Shares

num_crew = int(input("A crew is sailing on a ship this evening. How many members are there?: "))
total_money = round(float(input("They have earned a large sum of money! How much money did they earn: ")), 2)

amount_shares = num_crew + 7 + 3 - 2 #the reason i add 7 and 3 shares is for the captain and the first mate respectively. I subtracted two because I removed their singular share.
share_value = total_money / num_crew
cap_amount = share_value * 7
first_amount = share_value * 3
crew_mem = share_value - 500

print(f"The crew earned ${total_money:.2} that night.")
print(f"The crew is made up of {num_crew} members.")

print("The captain didn't have enough time to equally divvy up all of the money before releasing everyone to port. \nHe decided to give each crew member $500, and then sat down with his first mate to discuss.")

print(f"After the captain and the first mate divvied up all of the money to each of the crew...")
print(f"The captain gets ${cap_amount:.2}")
print(f"The first mate gets ${first_amount:.2}")
print(f"And each member of the crew still needs ${crew_mem:.2}")