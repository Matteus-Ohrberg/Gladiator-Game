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
                print("Alexios claws your", random.choice(bodyParts) + "!")
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