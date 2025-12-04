#VY 2nd Final Project

#Import the random library

#user_location is 1                     #The room where the user is located in. This will change when the user moves inside of each room function.
#list spirit_location is 3, 6, 4        #Where the user can encounter enemies
#boss_location is 9                     #The final room

#User stats (placeholder numbers for all numbers)
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
        #Room is 7                      #decide what room this will be in
    #dictionary healing_potion
        #Use is 1
        #Property is Healing
        #Effect is 25
        #in_inventory is False
        #Room is 2
    #dictionary defense_potion
        #Use is 1
        #Property is Defense
        #in_inventory is False
        #Room is 5
    #dictionary attack_potion
        #Use is 1
        #Property is Attack
        #in_inventory is False
        #Room is 2
    #dictionary dagger
        #Use is Equip                   #Meaning user can equip or not equip
        #Property is Attack             #raises attack
        #Effect is 5                    #by 5
        #is_equipped is False           #This will be changed later if the user decides to equip it.
        #Room is 6
    #dictionary shield
        #Use is Equip
        #Property is Defense
        #Effect is 3
        #is_equipped is False
        #Room is 6

#Combat functions
#Define user_combat with parameter enemy_stat:                  #I don't want to change the enemy_stats dictionary as I'll be using it multiple times. The dictionary will instead be a parameter, so I should be able to access the values like normal.
    #Show "Your Turn"                                           #I do need to change the user's stats though.
    #If the enemy that the user is fighting is a regular spirit:
        #Show "1. Attack, 2. Flee, 3. Expel, 4. Guard"
    #Else if the enemy that the user is fighting is the final boss:
        #Show "1. Attack, 2. Flee, 3. Charge Attack, 4. Guard"            #Charge attack works like the boss's charged attack, but the user can use it 2 times.
    #Show "What would you like to do?: " and get Input for variable user_choice
    #If user_action is 1:
        #Get the value for the user's Attack and the value for the enemy's Defense. Find the difference and assign the final value to variable damage
        #Subtract damage from the enemy's health
        #Check the enemy's health if it's 0 or less. If so, set it to 0.
        #Show the enemy's health and damage it took.
    #If user_action is 2:
        #If the enemy that the user is fighting is the final boss:
            #Show "Are you sure you want to back out?" and get the user's response
            #If they do, then set the user's location to the one they were at previously.
        #Else if the enemy that the user is fighting is a spirit:
            #Use the random library to pick a number from 1 to 10.
            #If this number is either 3 or less, let the user run away. Set the enemy's health to -1 so the program can check later if the user deserves rewards or not.
    #If user_action is 3 AND the enemy that the user is fighting is a spirit:
        #Show "You try to erase the spirit from existence."
        #Use the random library to pick a number from 1 to 10.
        #If that number is 1, set the enemy's health to 0.
        #If not, let the user know they failed.
    #Else if user_action is 3 AND the enemy that the user is fighting is the final boss:       #Will only run if the enemy is the final boss.
        #Show "You do a charged attack."
        #Add four to the user's attack stat and set this value to damage.
        #Subtract damage from the enemy's health.
        #Check the enemy's health. If it's less than 0, set it to 0.
        #Show how much health the enemy has left.
    #If user_action is 4:
        #Set the user's "guard" key to the value True
        #Show "You guarded yourself."
    #Return user_stats and enemy_stats


#Define enemy_combat with parameter enemy_stat:
    #Show "Enemy's Turn"
    #Subtract the enemy's attack stat with the user's defense stat, and set this value to the variable defense.
    #If the user guarded:
        #Subtract 2 from damage
        #And set the value for the key "guard" (that is in the user_stat's dictionary) to False.
    #Subtract the damage from the user's health.
    #If user_health is less than 0, set the user's health to 0 (to prevent negative health).
    #Show "Spirit attacks you for [put damage here]. You now have [put user_health here] left."
    #Return user_stats and enemy_stats

#Define boss_combat:                                            #It's okay to change the dictionary for the final boss as it will only be fought once each game.
    #Show "Enemy's turn"
    #Use the random module to generate a random number from 1 to 2 and set it to the variable boss_action
    #Make this loop in case the boss already used all of it's charged attacks. This is so the user can't get a free turn.
        #If boss_action is 1:                                       #Normal attack.
            #Subtract the user's Defense stat with the boss's Attack stat. Set this number to variable damage.
            #Subtract damage from the user's health.
            #If the user's health is less than 0, set the user's health to 0.
        #If boss_action is 2 AND charged_counter is less than 3:                                       #Charged attack.
            #Add 2 to the boss's attack stat and set that number to variable damage.
            #Subtract damage from user's health and check user's health. If user's health is less than 0, set it to 0.                    #There is no need to subtract defense as this is a charged attack, which ignores defense.
            #Add 1 to charged_counter.

#Define main_battle with parameter enemy:
    #Show "A wild [enemy name here] appeared!"
    #Use the random module to select either 1 or 2. Set this value to the variable going_first.
    #If the enemy that the user is fighting is a spirit:
        #If going_first is 1:                                       #User goes first if it's 1, enemy goes first if it's 2.
            #Show "You are going first."
            #Run the user_combat function with spirit_stats as the parameter
            #Set user_stats and current_enemy to the returned values of the function      #Needed since I don't want to change the original dictionary that holds the base enemy's stats.
            #Make a new variable turn and set it equal to "enemy"
            #While True loop:
                #If turn is "enemy":
                    #Show "Enemy's turn"
                    #Run the enemy_combat function with spirit_stats as the parameter
                    #Set user_stats and current_enemy to the returned values of the function
                    #Set turn to "player"
                    #Check for user and enemy health if they're 0. If the user's health is 0, let the user know they lost. If the enemy's health is 0, let the user know they won.
                #If turn is "player":
                    #Show "Your turn."
                    #Run the user_combat function with spirit_stats as the parameter
                    #Set user_stats and current_enemy to the returned values of the function
                    #Set turn to "enemy"
                    #Check for user and enemy health if they're 0. If the user's health is 0, let the user know they lost. If the enemy's health is 0, let the user know they won. 
        #Else if going_first is 2:
            #Show "Enemy is going first."
            #Run the enemy_combat function with spirit_stats as the parameter
            #Set user_stats and current_enemy to the returned values of the function
            #Make a new variable turn and set it equal to "player"
            #While True loop:
                #If turn is "enemy":
                    #Show "Enemy's turn"
                    #Run the enemy_combat function with spirit_stats as the parameter
                    #Set user_stats and current_enemy to the returned values of the function
                    #Set turn to "player"
                    #Check for user and enemy health if they're 0. If the user's health is 0, let the user know they lost. If the enemy's health is 0, let the user know they won. Break out of the loop if eiher is true.
                    #Show "Your turn."
                    #Run the user_combat function with spirit_stats as the parameter
                    #Set user_stats and current_enemy to the returned values of the function
                    #Set turn to "enemy"
                #Check for user and enemy health if they're 0. If the user's health is 0, let the user know they lost. If the enemy's health is 0, let the user know they won. Break out of the loop is either is true.
    #If the user is fighting the final boss, do something similar to above, however use the final boss function instead and return the final boss's stats.
    #Return user_stats and the enemy's stats


#Functions related to the menu (the thing where the user can select if they want to explore, move, or use an item)
#Define movement with parameter of the user's location:
    #if the user's location is 1:
        #Let the user go to rooms 4 or 2
    #else if the user's location is 2:
        #Let the user go to rooms 4, 1, or 6
    #else if the user's location is 3:
        #Let the user go to rooms 5, 7, or 8
    #else if the user's location is 4:
        #Let the user go to rooms 1, 2, or 7
    #else if the user's location is 5:
        #Let the user go to rooms 6, 7, 3, or 8
    #else if the user's location is 6:
        #Let the user go to rooms 2, 5, or 8
    #else if the user's location is 7:
        #Let the user go to rooms 4, 5, or 3
    #else if the user's location is 8:
        #Let the user go to rooms 5, 3, 6, or 9
    #Set the user's location to the room they selected.
    #Return the user's location

#Define inventory with parameters of the item dictionary and user's stats:
    #Look through the items and check the is_inventory key to see if it's set to True or False.
    #For all the items that are in the inventory, print them out to the user.
    #Ask the user if they want to use or equip an item.
    #If the user says yes:
        #Ask what item they want to use/equip
        #Check if it's in the dictionary. If it's not, ask the user to try again.
        #If the user changes their mind, return the user's stats item dictionary and end the function.
        #If the item that the user selected is a 1 use, check the stat that it affects and change the user's stat accordingly.
        #If the item that the user selected is an equipable (the dagger and shield), set their is_equipped key to True and check what stat it affects, and change the user's stat accordingly.
    #If the user says no:
        #Ask the user if they want to unequip an item:
        #If the user says yes:
            #Ask what item they want to uneaquip.
            #If the item is a 1 use, ask the user to try again.
            #If the user changes their mind, return the user's stats item dictionary and end the function.
            #If the item is either the sword and shield (check for is_equipped) and it's currently equipped, set that item's is_equipped to False, check what stat it affects, and remove that effect accordingly.
            #Set the item's location to the same location as the user's location, showing that the user dropped it in the room that they were in. 
        #If the user says no:
            #exit the function and return the user's stats and the dictionary of items.

#Define explore with parameters of the item dictionary:
    #Look through the dictionary of items and check each of the items room number that they are in. If the user's location is the same as the item location, put the name of the item in the item_room list (a few rooms have two items in them, so I'll make a list to accomodate for that.).
    #Show the user the list of items that are in the room and ask the user if they want to take an item.
    #If they say yes, ask them what item they want to take.
    #If the item is not in the room, ask them to select an existing item in the room.
    #If the item is in the room, find the is_inventory key of the item and make it to True.
    #Remove the item's name from the list. If the list is not empty, show what else is in the list and ask the user if they want to take it.
    #If there's not, end the function.
    #Return the item dictionary

#Define menu:
    #Use the above three functions for this function.
    #Tell the user that they can either look in their inventory, explore, or move to another room.
    #If the user wants to move to another room, run the movement function.
    #If the user wants to look in the inventory, run the inventory function.
    #If the user wants to explore, run the explore function.


#Function for restarting.
#Define restart:
    #Ask the user if they want to restart (let them know it will reset their progress).
    #If they do:
        #Set all of the variables and dictionaries to their values that they were at the start of the program.
    #End the function.


#Main game

#Introduce the user to the setting and their main objective at the start of the game.
#While True loop:
    #If the user's health is 0:
        #Run the restart function
    #If the final boss's health is 0:
        #Congratulate the user and run the restart function
    #Run the menu function
    #If the user's location is 9 (the same room where the final boss is at):
        #Ask the user if they want to fight the final boss
        #If so, run the main_battle function with the final boss's stats as the parameters.
    #Check if the user's location is in the list of where the basic enemies are:
        #If it is, run the main_battle function.
        #If not, continue a new iteration of the loop (go back to the menu function)