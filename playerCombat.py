import random
import colorama
from colorama import init
import time
import SpecializationPick
import os
#TODO add armor, none (1) chain (0.9) plate (0.8) magic (0.6)

init(autoreset=True) #Will reset colour after every line
# SpecializationPick.specializationPicker()
# weaponList = [["Spear", "Trident"], ["Longsword", "Shortsword", "Dagger"], ["Mace", "Flail"], ["Fists"]] #May not use list, probs for appearance
# print("You chose the weapon:", weaponList[(SpecializationPick.chosenCategory - 1)][(SpecializationPick.chosenWeapon - 1)])
#########################TODO: MAKE THE STATS CALCULATIONS AND COMBAT SYSTEM.

global playerHitpoints #Global PlayerHP variable.
playerHitpoints = 100
global playerArmor #damage - playerArmor / 2
playerArmor = 0


global enemyHitpoints #Global PlayerHP variable.
enemyHitpoints = 100
global enemyArmor #damage - enemyArmor / 2
enemyArmor = 0

global distance
distance = 5 #Distance variable to let me add range to weapons.

global playerStun #2 stun variables in order to add stunning to the game
global enemyStun
playerStun = 0
enemyStun = 0

global loopBreak
loopBreak = False

def PlayerCombat():
    global enemyStun #Sorry 'bout the global variables, turns out I need them INSIDE the function aswell. How eye-burning!
    global playerStun
    global distance
    global enemyArmor
    global playerArmor
    global playerHitpoints
    global enemyHitpoints
    global loopBreak

    if playerStun == 0:
        accuracyCheck = random.randint(1, 100) # Random number to roll for accuracy. To make higher likelyhood of hitting, decrease accuracy check number on each specified weapon
        
        #SPEARS~~--~~**~~--~~SPEARS~~--~~**~~--~~SPEARS~~--~~**~~--~~SPEARS~~--~~**~~--~~SPEARS~~--~~**~~--~~SPEARS~~--~~**~~--~~SPEARS#
        if SpecializationPick.chosenCategory == 1:
            if SpecializationPick.chosenWeapon == 1:
                if distance <= 4:
                    print("Attack [1], Sweep at Legs (Chance to stun) [2], Step back [3], Surrender [0]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck <= 35: # If accuracy check is equal to or above 35 (65% chance), attack is successful.
                        attackRoll = random.randint(12, 16) # Base damage at 12 for spears, give or take 2 for damage variation.
                        attackDamage = attackRoll * enemyArmor
                        print()
                        print("You thrust your spear at your opponent!")
                        print(colorama.Fore.GREEN, "You deal:", attackDamage, "damage towards them!")

                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10) # Stun is a 40% chance. If stunned, add 1 to stun counter.
                            if stunChance <= 4:
                                print("You swing at your opponents legs and hit them, knocking them over!")
                                enemyStun += 1
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 3:
                        print("You take a step away from the opponent")
                        distance += 1
                    
                    elif attackChoice == 0:
                        print("You yell out that you surrender!")
                        time.sleep(1.5)
                        surrenderScore = 0 #Surrender score is so far only affected by HP.

                        if playerHitpoints > enemyHitpoints:
                            print("The audience seems surprised! They thought that you were in the lead.")
                            surrenderScore += 2

                        elif playerHitpoints < enemyHitpoints:
                            print("The audience does not seem surprised, as you have fallen behind your opponent")
                            surrenderScore -= 1
                        
                        else:
                            print("The audience is confused! As both you and your opponent seem equal in the fight so far")
                        
                        YeaOrNay = random.randint(1, 10)
                        YeaOrNay + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")
                            loopBreak = not loopBreak
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerHitpoints -= 100

                elif distance > 4:
                    print("Throw Spear [1], Step Forward [2]")
                    print("(Note that spear is immediately picked up after throw)")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 40: # If accuracy is 40 or above (60%), hit.
                        attackRoll = random.randint(8, 12)
                        attackDamage = attackRoll * enemyArmor
                        print()
                        print("You aim your spear and throw it towards your opponent!")
                        print(colorama.Fore.GREEN, "You deal:", attackDamage, "damage towards your opponent!")
                    
                    elif attackChoice == 2:
                        print("You step towards your opponent")
                        distance -= 1


            
            elif SpecializationPick.chosenWeapon == 2:
                if distance <= 4:
                    print("Attack [1], Sweep at Legs (Chance to stun) [2], Step back [3], Surrender [0]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 50: # If accuracy check is equal to or above 50 (50% chance), attack is successful.
                        attackRoll = random.randint(16, 20)
                        attackDamage = attackRoll * enemyArmor
                        print()
                        print("You thrust the trident at your opponent!")
                        print(colorama.Fore.GREEN, "You deal:", attackDamage, "damage towards them!")

                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You swing at your opponents legs and hit them, knocking them over!")
                                enemyStun += 1
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 3:
                        print("You take a step away from the opponent")
                        distance += 1
                    
                    elif attackChoice == 0:
                        print("You yell out that you surrender!")
                        time.sleep(1.5)
                        surrenderScore = 0

                        if playerHitpoints > enemyHitpoints:
                            print("The audience seems surprised! They thought that you were in the lead.")
                            surrenderScore += 2

                        elif playerHitpoints < enemyHitpoints:
                            print("The audience does not seem surprised, as you have fallen behind your opponent")
                            surrenderScore -= 1
                        
                        else:
                            print("The audience is confused! As both you and your opponent seem equal in the fight so far")
                        
                        YeaOrNay = random.randint(1, 10)
                        YeaOrNay + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")
                            loopBreak = not loopBreak
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerHitpoints -= 100

                elif distance > 4:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1


        #BLADES~~--~~**~~--~~BLADES~~--~~**~~--~~BLADES~~--~~**~~--~~BLADES~~--~~**~~--~~BLADES~~--~~**~~--~~BLADES~~--~~**~~--~~BLADES#
        elif SpecializationPick.chosenCategory == 2:
            if SpecializationPick.chosenWeapon == 1:
                if distance <= 3:
                    print("Attack [1], Bash (Chance to stun) [2], Step back [3], Surrender [0]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 40:
                        attackRoll = random.randint(25, 35)
                        attackDamage = attackRoll * enemyArmor
                        print()
                        print("You slowly swing your longsword at your opponent!")
                        print(colorama.Fore.GREEN, "You deal:", attackDamage, "damage towards your opponent!")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You bash your opponent, stunning them!")
                                enemyStun += 1
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 3:
                        print("You take a step away from the opponent")
                        distance += 1
                    
                    elif attackChoice == 0:
                        print("You yell out that you surrender!")
                        time.sleep(1.5)
                        surrenderScore = 0

                        if playerHitpoints > enemyHitpoints:
                            print("The audience seems surprised! They thought that you were in the lead.")
                            surrenderScore += 2

                        elif playerHitpoints < enemyHitpoints:
                            print("The audience does not seem surprised, as you have fallen behind your opponent")
                            surrenderScore -= 1
                        
                        else:
                            print("The audience is confused! As both you and your opponent seem equal in the fight so far")
                        
                        YeaOrNay = random.randint(1, 10)
                        YeaOrNay + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")
                            loopBreak = not loopBreak
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerHitpoints -= 100

                elif distance > 3:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1
            
            elif SpecializationPick.chosenWeapon == 2:
                if distance <= 2:
                    print("Attack [1], Bash (Chance to stun) [2], Step back [3], Surrender [0]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 40:
                        attackRoll = random.randint(8, 12)
                        attackDamage = attackRoll * enemyArmor
                        print()
                        print("You swing your sword at your opponent!")
                        print(colorama.Fore.GREEN, "You deal:", attackDamage, "damage towards your opponent!")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You bash your opponent, stunning them!")
                                enemyStun += 1
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 3:
                        print("You take a step away from the opponent")
                        distance += 1
                    
                    elif attackChoice == 0:
                        print("You yell out that you surrender!")
                        time.sleep(1.5)
                        surrenderScore = 0

                        if playerHitpoints > enemyHitpoints:
                            print("The audience seems surprised! They thought that you were in the lead.")
                            surrenderScore += 2

                        elif playerHitpoints < enemyHitpoints:
                            print("The audience does not seem surprised, as you have fallen behind your opponent")
                            surrenderScore -= 1
                        
                        else:
                            print("The audience is confused! As both you and your opponent seem equal in the fight so far")
                        
                        YeaOrNay = random.randint(1, 10)
                        YeaOrNay + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")
                            loopBreak = not loopBreak
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerHitpoints -= 100
                
                elif distance > 2:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1

            elif SpecializationPick.chosenWeapon == 3:
                if distance <= 1:
                    print("Attack [1], Grab (Chance to stun) [2], Step back [3], Throw Dagger [4] Surrender [0]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 20:
                        if enemyStun > 0:
                            attackRoll = random.randint(30, 40)
                            attackDamage = attackRoll * enemyArmor
                        else:
                            attackRoll = random.randint(2, 8)
                            attackDamage = attackRoll * enemyArmor
                        print()
                        print("You stab your opponent!")
                        print(colorama.Fore.GREEN, "You deal:", attackDamage, "damage towards your opponent!")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You grab your opponent, surprising your them!")
                                enemyStun += 2
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 3:
                        print("You take a step away from the opponent")
                        distance += 1
                    
                    elif attackChoice == 0:
                        print("You yell out that you surrender!")
                        time.sleep(1.5)
                        surrenderScore = 0

                        if playerHitpoints > enemyHitpoints:
                            print("The audience seems surprised! They thought that you were in the lead.")
                            surrenderScore += 2

                        elif playerHitpoints < enemyHitpoints:
                            print("The audience does not seem surprised, as you have fallen behind your opponent")
                            surrenderScore -= 1
                        
                        else:
                            print("The audience is confused! As both you and your opponent seem equal in the fight so far")
                        
                        YeaOrNay = random.randint(1, 10)
                        YeaOrNay + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")
                            loopBreak = not loopBreak
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerHitpoints -= 100
                
                elif distance > 2:
                    print("Throw Dagger [1], Step Forward [2]")
                    print("(Note that throwing your dagger will not result in you losing it.)")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 30:
                        attackRoll = random.randint(4, 8)
                        attackDamage = attackRoll * enemyArmor
                        print()
                        print("You throw your dagger towards your opponent!")
                        print(colorama.Fore.GREEN, "You deal:", attackDamage, "damage towards your opponent!")

                    elif attackChoice == 2:
                        print("You step towards your opponent")
                        distance -= 1
        

        #BLUNTS~~--~~**~~--~~BLUNTS~~--~~**~~--~~BLUNTS~~--~~**~~--~~BLUNTS~~--~~**~~--~~BLUNTS~~--~~**~~--~~BLUNTS~~--~~**~~--~~BLUNTS#
        elif SpecializationPick.chosenCategory == 3:
            if SpecializationPick.chosenWeapon == 1:
                if distance <= 2:
                    print("Attack [1], Bash (Chance to stun) [2], Step back [3], Surrender [0]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 45:
                        attackRoll = random.randint(18, 22)
                        attackDamage = attackRoll * enemyArmor
                        print()
                        print("You swing your mace at the opponent!")
                        print(colorama.Fore.GREEN, "You deal:", attackDamage, "damage towards your opponent!")
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You stunned your opponent!")
                                enemyStun += 1
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 7:
                                print("You bash your opponent, stunning them!")
                                enemyStun += 1
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 3:
                        print("You take a step away from the opponent")
                        distance += 1
                    
                    elif attackChoice == 0:
                        print("You yell out that you surrender!")
                        time.sleep(1.5)
                        surrenderScore = 0

                        if playerHitpoints > enemyHitpoints:
                            print("The audience seems surprised! They thought that you were in the lead.")
                            surrenderScore += 2

                        elif playerHitpoints < enemyHitpoints:
                            print("The audience does not seem surprised, as you have fallen behind your opponent")
                            surrenderScore -= 1
                        
                        else:
                            print("The audience is confused! As both you and your opponent seem equal in the fight so far")
                        
                        YeaOrNay = random.randint(1, 10)
                        YeaOrNay + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")
                            loopBreak = not loopBreak
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerHitpoints -= 100
                
                elif distance > 2:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1
            
            elif SpecializationPick.chosenWeapon == 2:
                if distance <= 2:
                    print("Attack [1], Bash (Chance to stun) [2], Step back [3], Surrender [0]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 50:
                        attackRoll = random.randint(18, 22)
                        attackDamage = attackRoll
                        print()
                        print("You swing your sword at your opponent!")
                        print(colorama.Fore.GREEN, "You deal:", attackDamage, "damage towards your opponent!")
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You stunned your opponent!")
                                enemyStun += 1
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 7:
                                print("You bash your opponent, stunning them!")
                                enemyStun += 1
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 3:
                        print("You take a step away from the opponent")
                        distance += 1
                    
                    elif attackChoice == 0:
                        print("You yell out that you surrender!")
                        time.sleep(1.5)
                        surrenderScore = 0

                        if playerHitpoints > enemyHitpoints:
                            print("The audience seems surprised! They thought that you were in the lead.")
                            surrenderScore += 2

                        elif playerHitpoints < enemyHitpoints:
                            print("The audience does not seem surprised, as you have fallen behind your opponent")
                            surrenderScore -= 1
                        
                        else:
                            print("The audience is confused! As both you and your opponent seem equal in the fight so far")
                        
                        YeaOrNay = random.randint(1, 10)
                        YeaOrNay + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")
                            loopBreak = not loopBreak
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerHitpoints -= 100
                
                elif distance > 2:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1


        #OTHER~~--~~**~~--~~OTHER~~--~~**~~--~~OTHER~~--~~**~~--~~OTHER~~--~~**~~--~~OTHER~~--~~**~~--~~OTHER~~--~~**~~--~~OTHER~~--~~OTHER#
        elif SpecializationPick.chosenCategory == 4:
            if SpecializationPick.chosenWeapon == 1:
                if distance <= 1:
                    print("Attack [1], Grab (Chance to stun) [2], Step back [3], Surrender [0]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 10:
                        attackRoll = random.randint(1, 3)
                        attackDamage = attackRoll * enemyArmor
                        print()
                        print("You punch your opponent!")
                        print(colorama.Fore.GREEN, "You deal:", attackDamage, "damage towards your opponent!")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You bash your opponent, stunning them!")
                                enemyStun += 1
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 3:
                        print("You take a step away from the opponent")
                        distance += 1
                    
                    elif attackChoice == 0:
                        print("You yell out that you surrender!")
                        time.sleep(1.5)

                        if playerHitpoints > enemyHitpoints:
                            print("The audience seems surprised! They thought that you were in the lead.")

                        elif playerHitpoints < enemyHitpoints:
                            print("The audience does not seem surprised, as you have fallen behind your opponent")
                        
                        else:
                            print("The audience is confused! As both you and your opponent seem equal in the fight so far")
                        
                        time.sleep(1.5)
                        print("The audience decides to let you live.")
                        loopBreak = not loopBreak
                
                elif distance > 1:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1

    elif playerStun > 0:
        print("You are stunned!")