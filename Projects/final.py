#VY 2nd Final Project

#Import the random library

#user_location is 1                     #Starting room
#list spirit_location is 3, 6, 8, 5     #Where the user can encounter enemies, probably change later
#boss_location is 9                     #The final room

#User stats (placeholder numbers)
#dictionary user_stats
    #Health is 50
    #Attack is 5
    #Defense is 2
    #Guard is False                     #This is a flag for the combat function so the program knows if it needs to temporarily increase the user's defense stat.

#Spirit stats
#dictionary spirit_stats                #The stats for the enemy that the user encounters. Perhaps add another kind of enemy if I have time by doing a nested dictionary.
    #Health is 30
    #Attack is 4
    #Defense is 1

#Final boss stats
#dictionary boss_stats
    #Health is 70
    #Attack is 6
    #Defense is 4

#Items (two items that increase each stat, six items in total)
#dictionary items
    #dictionary bandage
        #Use is 1                       #this means that this can only be used one time. This will be changed to 0 if the user uses it.
        #Property is Healing            #meaning it's a healing item
        #Effect is 10                   #Heals 10 hp
        #in_inventory is False          #Checking if user has the item
        #Room is TBD                    #decide what room this will be in (draw the dang map will ya)
    #dictionary healing_potion
        #Use is 1
        #Property is Healing
        #Effect is 25
        #in_inventory is False
        #Room is TBD
    #dictionary defense_potion
        #Use is 1
        #Property is Defense
        #in_inventory is False
        #Room is TBD
    #dictionary attack_potion
        #Use is 1
        #Property is Attack
        #in_inventory is False
        #Room is TBD
    #dictionary dagger
        #Use is Equip                   #Meaning user can equip or not equip
        #Property is Attack             #raises attack
        #Effect is 5                    #by 5
        #is_equipped is False           #This will be changed later if the user decides to equip it.
        #Room is TBD
    #dictionary shield
        #Use is Equip
        #Property is Defense
        #Effect is 3
        #is_equipped is False

#Combat functions
#Define user_combat with parameter enemy_stats:                       #I don't want to change the enemy_stats dictionary as I'll be using it multiple times. The dictionary will instead be a parameter, so I should be able to access the values like normal.
    #Show "Your Turn"
    #Show "1. Attack, 2. Flee, 3. Expel, 4. Guard"              #Maybe add an option to use an item in battle. Show each option on it's own line.
    #Show "What would you like to do?: " and get Input for variable user_action
    #If user_action is 1:
        #Get the value for the user's Attack and the value for the enemy's Defense. Find the difference and assign the final value to variable damage
        #Subtract damage from the enemy's health
        #If enemy's health is less than 0:
            #Set enemy's health to 0
        #Show "You attacked. Spirit now has [put enemy's health here] health left."   #If I add multiple enemies, change this.
    #If user_action is 2:
        #Use the random library to pick a number from 1 to 10. Set this number to variable flee_chance
        #If flee_chance is less than or equal to 3:             #This is so if flee_chance is 1, 2, or 3, the user flees successfully. If not, they stay in the battle.
            #Show "You successfully ran away."
            #Return user_stats
            #End Function
        #Else:
            #Show "You failed to run away."
    #If user_action is 3:
        #Show "You try to erase the spirit from existence."
        #Use the random library to pick a number from 1 to 10. Set this number to variable expel_chance.
        #If expel_chance equals 1:                              #Making this a 1 in 10 chance of working, aka a 10% chance of working.
            #Show "You successfully expelled the spirit."
            #Return user_stats
            #End Function
        #Else:
            #Show "You failed to expel the spirit."
    #If user_action is 4:
        #Set the user's "guard" key to the value True
        #Show "You guarded yourself."
    #Return user_stats, enemy_stats

#Define enemy_combat with parameter enemy_stats:
    #Show "Enemy's Turn"
    #Subtract the enemy's attack stat with the user's defense stat, and set this value to the variable defense.
    #If the user guarded:
        #Subtract 2 from damage
        #Set the value for the key "guard" (that is in the user_stat's dictionary) to False.
    #Subtract the damage from the user's health.
    #If user_health is less than 0:
        #Set user_health to 0
    #Show "Spirit attacks you for [put damage here]. You now have [put user_health here] left."
    #End Function