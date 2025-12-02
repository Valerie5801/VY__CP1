#VY 2nd Final Project

#Import the random library

#user_location is 1                     #The room where the user is located in. This will change when the user moves inside of each room function.
#list spirit_location is 3, 6, 8, 5     #Where the user can encounter enemies, probably change later
#boss_location is 9                     #The final room

#User stats (placeholder numbers)
#dictionary user_stats
    #Health is 50
    #Attack is 5
    #Defense is 2
    #Guard is False                     #This is a flag for the combat function so the program knows if it needs to temporarily increase the user's defense stat.
    #charged_counter is 0               #Will only be used if the user is fighting the final boss.

#Spirit stats
#dictionary spirit_stats                #The stats for the enemy that the user encounters. Perhaps add another kind of enemy if I have time by doing a nested dictionary.
    #Type is Spirit                     #So I can check in the combat functions what enemy the user fights.
    #Health is 30
    #Attack is 4
    #Defense is 1

#Final boss stats
#dictionary boss_stats
    #Type is Boss
    #Health is 70
    #Attack is 6
    #Defense is 4
    #charged_counter is 0               #This counts how many times the boss uses the charged attack. To keep this fair, I'm keeping track and capping it at 3 times.

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
#Define user_combat with parameter enemy_stat:                  #I don't want to change the enemy_stats dictionary as I'll be using it multiple times. The dictionary will instead be a parameter, so I should be able to access the values like normal.
    #Show "Your Turn"                                           #I do need to change the user's stats though.
    #If the enemy that the user is fighting is a regular spirit:
        #Show "1. Attack, 2. Flee, 3. Expel, 4. Guard"                    #Maybe add an option to use an item in battle. Show each option on it's own line.
    #Else if the enemy that the user is fighting is the final boss:
        #Show "1. Attack, 2. Flee, 3. Charge Attack, 4. Guard"            #Charge attack works like the boss's charged attack, but the user can use it 2 times.
    #Show "What would you like to do?: " and get Input for variable user_choice
    #If user_action is 1:
        #Get the value for the user's Attack and the value for the enemy's Defense. Find the difference and assign the final value to variable damage
        #Subtract damage from the enemy's health
        #If enemy's health is less than 0:
            #Set enemy's health to 0
        #Show "You attacked. [enemy name] now has [put enemy's health here] health left."   #If I add multiple enemies, change this.
    #If user_action is 2:
        #Use the random library to pick a number from 1 to 10. Set this number to variable flee_chance
        #If flee_chance is less than or equal to 3:             #This is so if flee_chance is 1, 2, or 3, the user flees successfully. If not, they stay in the battle.
            #Show "You successfully ran away."
            #Set enemy's health to -1                           #This is needed so when I make the main combat function later, I can use the enemy's health to check if the user just ran away or actually defeated it.
                                                                    #This way, I can see if the user deserves to get rewards or not.
        #Else:
            #Show "You failed to run away."
    #If user_action is 3 AND the enemy that the user is fighting is a spirit:
        #Show "You try to erase the spirit from existence."
        #Use the random library to pick a number from 1 to 10. Set this number to variable expel_chance.
        #If expel_chance equals 1:                              #Making this a 1 in 10 chance of working, aka a 10% chance of working.
            #Show "You successfully expelled the spirit."
            #Set the enemy's health to 0
        #Else:
            #Show "You failed to expel the spirit."
    #Else if user_action is 3 AND the enemy that the user is fighting is the final boss:       #Will only run if the enemy is the final boss.
        #Show "You do a charged attack."
        #Add four to the user's attack stat and set this value to damage.
        #Subtract damage from the enemy's health.
        #If enemy's health is less than 0:
            #Set the enemy's health to 0.
        #Show "[the enemy's name] now has [put enemy's health here] health left."
    #If user_action is 4:
        #Set the user's "guard" key to the value True
        #Show "You guarded yourself."
    #Return user_stats and enemy_stats


#Define enemy_combat:
    #Show "Enemy's Turn"
    #Subtract the enemy's attack stat with the user's defense stat, and set this value to the variable defense.
    #If the user guarded:
        #Subtract 2 from damage
        #Set the value for the key "guard" (that is in the user_stat's dictionary) to False.
    #Subtract the damage from the user's health.
    #If user_health is less than 0:
        #Set user_health to 0
    #Show "Spirit attacks you for [put damage here]. You now have [put user_health here] left."
    #Return user_stats and enemy_stats

#Define boss_combat:                                            #It's okay to change the dictionary for the final boss as it will only be fought once each game.
    #Show "Enemy's turn"
    #Use the random module to generate a random number from 1 to 2 and set it to the variable boss_action
    #If boss_action is 1:                                       #Normal attack.
        #Subtract the user's Defense stat with the boss's Attack stat. Set this number to variable damage.
        #Subtract damage from the user's health.
        #If the user's health is less than 0:
            #Set the user's health to 0.
    #If boss_action is 2:                                       #Charged attack.
        #Add 2 to the boss's attack stat and set that number to variable damage.
        #Subtract damage from user's health.                    #There is no need to subtract defense as this is a charged attack, which ignores defense.
        #Add 1 to the value of the key charged_counter in the boss's dictionary (refer above)

#Define main_battle with parameter enemy:
    #Show "A wild [enemy name here] appeared!"
    #Use the random module to select either 1 or 2. Set this value to the variable going_first.
    #If going_first is 1:                                       #User goes first if it's 1, enemy goes first if it's 2.
        #Show "You are going first."
        #If the enemy that the user is fighting is the spirit:
            #While True loop:
                #Run the user_combat function with the parameters of the spirit.
                #Set user_stats and current_enemy to the returned values of the function      #Needed since I don't want to change the original dictionary that holds the base enemy's stats.
                #Run the enemy_combat function with the arameters