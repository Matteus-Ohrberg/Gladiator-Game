import time
import random
import os
import setMatchesCombat
import colorama
from colorama import init

init(autoreset=True)

#TODO: 10 fights in increasing difficulty, increasing player HP, better descriptions(?), multi-combat (animals), selfID for descriptions?
#Bravery points? Shields???

bodyParts = ["head", "torso", "left leg", "right leg", "left arm", "right arm"] # Used for non descriptive descriptions.



def alexiosOmorfan(): # Fuck you, Alexios. # Alexios should have 60 HP ? # Alexios is a humanoid cat by the way.
    hitDetect = False # Making sure damage calculations doesn't run with nil value.
    accuracyCheck = random.randint(1, 100) + 15 # Alexios has increased chance to hit, +15 flat increase.
    
    if setMatchesCombat.distance <= 2:
        attackChoice = random.randint(1, 4) # Random choice between the following: Punch, Scratch, Block, Step back

        if attackChoice == 1: # Punch
            if accuracyCheck <= 70:
                attackDamage = random.randint(7, 14) # Random Damage
                print("Alexios punches your" + random.choice(bodyParts) + "!") # Non-descriptive description of where Alexios attacks you.
                print("Alexios damages you for", attackDamage, "HP!") # Prints the amount of DMG Alexios does
                hitDetect = True
            
            else:
                print("Alexios throws a punch at you but misses!")
        
        elif attackChoice == 2: # Scratch / claw
            if accuracyCheck <= 55:
                attackDamage = random.randint(5, 23) # Random Damage, but riskier.
                print("Alexios claws your ", random.choice(bodyParts) + "!")
                print("Alexios damages you for", attackDamage, "HP!")
                hitDetect = True
            
            else:
                print("Alexios missed when trying to claw you.") # "Claw you" doesn't feel right as a description.

        elif attackChoice == 3: # Block
            setMatchesCombat.blockingPlayer = 0.3 # 70% DMG reduction if blocked
            print("Alexios blocks your next attack!") # I could make it so Alexios heals up 70% of the attack the player did, but that'd require me to rewrite some code and I don't feel like doing that.

        elif attackChoice == 4: # Step Back:
            setMatchesCombat.distance += 1
            print("Alexios steps back!")
    
    elif setMatchesCombat.distance > 2:
        attackChoice = random.randint(1, 2) # Throw rock and step forward

        if attackChoice == 1: # Throw stone
            if accuracyCheck <= 60:
                attackDamage = random.randint(4, 7)
                print("Alexios throws a rock at you! The rock hits your", random.choice(bodyParts))
                hitDetect = True

            else:
                print("Alexios throws a rock at you, but they miss!")
        
        if attackChoice == 2: # Step forward
            setMatchesCombat.distance -= 1
            print("Alexios steps forward!")
    
    if hitDetect == True:
        setMatchesCombat.playerHitpoints -= attackDamage * setMatchesCombat.blockingEnemy
    setMatchesCombat.blockingEnemy = 1

# Location is a variable to keep track of cardinal directions. 1 is north, 2 is east, 3 is south, 4 is west.
global enemyLocation
enemyLocation = 2

global playerLocation
playerLocation = 1

def antimemes():
    global enemyLocation
    hitDetect = False
    accuracyCheck = random.randint(1, 100)
    locationMove = random.randint(1, 20)

    if setMatchesCombat.distance <= 2:
        attackChoice = random.randint(1, 4) # 1 and 2 for attack, 3 is for block, 4 is for move back.

        if attackChoice == 1 or 2 and accuracyCheck <= 70: #I realised Alexios' code is unoptimised, oops.
            attackDamage = random.randint(5, 25)
            print("Your opponent hits you with their sword!")
            print("The opponent damages you for:", attackDamage, "HP!")
            hitDetect = True
        
        elif attackChoice == 3:
            print("Your opponent blocks your next attack!")
            setMatchesCombat.blockingPlayer = 0.2
        
        elif attackChoice == 4:
            print("Your opponent seems to back away!")
            setMatchesCombat.distance += 1
    
    elif setMatchesCombat.distance > 2:
        attackChoice = random.randint(1, 4) # 1 is for location, 2 and above is for moving closer

        if attackChoice == 1: # CAUTION FOR HUMAN EYES: HORRIBLE CODE BELOW
            if enemyLocation == 1 and locationMove < 11: # If north (1) and locMove below 11, go west (4)
                enemyLocation = 4
            
            elif enemyLocation == 1 and locationMove > 10: # If north (1) and locMove more than 10, go east (2)
                enemyLocation = 2
            
            elif enemyLocation == 2 and locationMove < 11: # If east (2), and locMove below 11, go north (1)
                enemyLocation = 1
            
            elif enemyLocation == 2 and locationMove > 10: # If east (2), and locMove more than 10, go south (3)
                enemyLocation = 3
            
            elif enemyLocation == 3 and locationMove < 11: # if south (3), and locMove below 11, go east (2)
                enemyLocation = 2
            
            elif enemyLocation == 3 and locationMove > 10: # If south (3), and locMove more than 10, go west (4)
                enemyLocation = 4
            
            elif enemyLocation == 4 and locationMove < 11: # If west (4), and locMove below 11, go south (3)
                enemyLocation = 3
            
            elif enemyLocation == 4 and locationMove > 10: # If west (4), and locMove more than 10, go north (1)
                enemyLocation = 1
            
            print("You feel that your opponent has moved location!!")
        

        elif attackChoice > 1:
            print("Your opponent seems to get closer!")
            setMatchesCombat.distance -= 1
    
    if hitDetect == True:
        setMatchesCombat.playerHitpoints -= attackDamage * setMatchesCombat.blockingEnemy
    setMatchesCombat.blockingEnemy = 1