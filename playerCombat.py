import random
import colorama
from colorama import init
import time
import SpecializationPick
import os

init(autoreset=True) #Will reset colour after every line

global difficulty # Lists used for: "ai" weapon choice, "ai" armor choice, and difficulty.
global weaponList
global armorList
weaponList = ["Spear", "Trident", "Longsword", "Shortsword", "Dagger", "Mace", "Flail", "Fists"]
# armorList = ["None", "leather", "Chainmail", "FullPlate", "Magic"]
# difficultyList = [1, 0,9, 0.8, 0.7, 0,6]
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ armorList and difficultyList are unused, use it to understand my thought process maybe.


global playerHitpoints #Global PlayerHP variable.
playerHitpoints = 100
global playerArmor 
playerArmor = 0


global enemyHitpoints #Global EnemyHP variable.
enemyHitpoints = 100
global enemyArmor
enemyArmor = 0
global enemyWeapon

global distance
distance = 5 #Distance variable to let me add range to weapons.

global playerStun #2 stun variables in order to add stunning to the game
global enemyStun
playerStun = 0
enemyStun = 0

global loopBreak
loopBreak = False

global playerSurrenderDamageCheck

def difficultySelect():
    global difficulty
    print("Select difficulty, each level increases the likelyhood of enemy getting better armor.")
    print("(Damage reduction per armor level is 10 percent)")
    print("Easy [1], Normal [2], Difficult [3], Hard [4], Unfair [5]")
    difficulty = int(input())


def armorPicker(): 
    global playerArmor
    HasArmorBeenPicked = False

    while HasArmorBeenPicked == False: #Copy pasted loop from above #As of OCT 20, loop does not work
        os.system('cls')
        print("Remember: You cannot change armor until the dev adds a way!")
        print("Armors: None [1], Leather [2], Chainmail [3], Full-plate [4], Magic [5]")
        print("Note: This only reduces damage by 10 percent per level and doesn't change any descriptions")
        
        armorPick = int(input())

        if armorPick == 1:
            os.system('cls')
            print("Confirm No armor? Yes [1], No [2]")
            confirmPick = int(input())

            if confirmPick == 1:
                playerArmor = 1
                HasArmorBeenPicked = not HasArmorBeenPicked
            
            else:
                continue
        
        if armorPick == 2:
            os.system('cls')
            print("Confirm Leather armor? Yes [1], No [2]")
            confirmPick = int(input())

            if confirmPick == 1:
                playerArmor = 0.9
                HasArmorBeenPicked = not HasArmorBeenPicked
            
            else:
                continue
        
        if armorPick == 3:
            os.system('cls')
            print("Confirm Chainmail armor? Yes [1], No [2]")
            confirmPick = int(input())

            if confirmPick == 1:
                playerArmor = 0.8
                HasArmorBeenPicked = not HasArmorBeenPicked
            
            else:
                continue
        
        if armorPick == 4:
            os.system('cls')
            print("Confirm Full-plate armor? Yes [1], No [2]")
            confirmPick = int(input())

            if confirmPick == 1:
                playerArmor = 0.7
                HasArmorBeenPicked = not HasArmorBeenPicked
            
            else:
                continue
        
        if armorPick == 5:
            os.system('cls')
            print("Confirm Magic armor? Yes [1], No [2]")
            confirmPick = int(input())

            if confirmPick == 1:
                playerArmor = 0.6
                HasArmorBeenPicked = not HasArmorBeenPicked
            
            else:
                continue


def enemyChoiceFunc(): # This has to be the worst way to do random armor for enemies
    global enemyWeapon
    global enemyArmor
    enemyWeapon = random.choice(weaponList)
    if difficulty == 1:
        jankyArmorSelect = random.randint(1, 100)

        if jankyArmorSelect >= 50:
            enemyArmor = 1

        elif jankyArmorSelect >= 20:
            enemyArmor = 0.9

        elif jankyArmorSelect >= 15:
            enemyArmor = 0.8
        
        elif jankyArmorSelect >= 10:
            enemyArmor = 0.7
        
        else:
            enemyArmor = 0.6
    ##################################
    elif difficulty == 2:
        jankyArmorSelect = random.randint(1, 100)

        if jankyArmorSelect >= 60:
            enemyArmor = 1

        elif jankyArmorSelect >= 35:
            enemyArmor = 0.9

        elif jankyArmorSelect >= 20:
            enemyArmor = 0.8
        
        elif jankyArmorSelect >= 10:
            enemyArmor = 0.7
        
        else:
            enemyArmor = 0.6
    ##################################
    elif difficulty == 3:
        jankyArmorSelect = random.randint(1, 100)

        if jankyArmorSelect >= 70:
            enemyArmor = 1

        elif jankyArmorSelect >= 45:
            enemyArmor = 0.9

        elif jankyArmorSelect >= 25:
            enemyArmor = 0.8
        
        elif jankyArmorSelect >= 15:
            enemyArmor = 0.7
        
        else:
            enemyArmor = 0.6
    ##################################
    elif difficulty == 4:
        jankyArmorSelect = random.randint(1, 100)

        if jankyArmorSelect >= 90:
            enemyArmor = 1

        elif jankyArmorSelect >= 70:
            enemyArmor = 0.9

        elif jankyArmorSelect >= 40:
            enemyArmor = 0.8
        
        elif jankyArmorSelect >= 20:
            enemyArmor = 0.7
        
        else:
            enemyArmor = 0.6
    ##################################
    elif difficulty == 5:
        jankyArmorSelect = random.randint(1, 100)

        if jankyArmorSelect >= 95:
            enemyArmor = 1

        elif jankyArmorSelect >= 85:
            enemyArmor = 0.9

        elif jankyArmorSelect >= 65:
            enemyArmor = 0.8
        
        elif jankyArmorSelect >= 35:
            enemyArmor = 0.7
        
        else:
            enemyArmor = 0.6
    ##################################


def PlayerCombat():
    global enemyStun #Sorry 'bout the global variables, turns out I need them INSIDE the function aswell. How eye-burning!
    global playerStun
    global distance
    global enemyArmor
    global playerArmor
    global playerHitpoints
    global enemyHitpoints
    global loopBreak
    global playerSurrender
    global playerSurrenderDamageCheck
    attackDamage = 0

    if playerStun == 0:
        accuracyCheck = random.randint(1, 100) # Random number to roll for accuracy. To make higher likelyhood of hitting, decrease accuracy check number on each specified weapon
        
        #SPEARS~~--~~**~~--~~SPEARS~~--~~**~~--~~SPEARS~~--~~**~~--~~SPEARS~~--~~**~~--~~SPEARS~~--~~**~~--~~SPEARS~~--~~**~~--~~SPEARS#
        if SpecializationPick.chosenCategory == 1:
            if SpecializationPick.chosenWeapon == 1:
                if distance <= 4:
                    print("Attack [1], Sweep at Legs (Chance to stun) [2], Step back [3], Surrender [0]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 35: # If accuracy check is equal to or above 35 (65% chance), attack is successful.
                        attackRoll = random.randint(12, 16) # Base damage at 12 for spears, give or take 2 for damage variation.
                        attackDamage = attackRoll * enemyArmor
                        print()
                        print("You thrust your spear at your opponent!")
                        print(colorama.Fore.GREEN + "You deal:", attackDamage, "damage towards them!")
                    
                    elif attackChoice == 1 and accuracyCheck <= 34:
                        print("You try to hit your opponent, but you miss!")

                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10) # Stun is a 40% chance. If stunned, add 1 to stun counter.
                            if stunChance <= 4:
                                print("You swing at your opponents legs and hit them, knocking them over!")
                                enemyStun += 1
                            if stunChance >= 5:
                                print("You swing at your opponents legs, but you miss!")
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
                        
                        surrenderRNG = random.randint(1, 10)
                        YeaOrNay = surrenderRNG + surrenderScore #Shitty surrender system, just RNG based.
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")

                            playerSurrender = True
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerSurrenderDamageCheck = True
                            attackDamage = 100
                    else:
                        print()

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
                        print(colorama.Fore.GREEN + "You deal:", attackDamage, "damage towards your opponent!")
                    
                    elif attackChoice == 1 and accuracyCheck <= 39:
                        print("You threw your spear but missed!")
                    
                    elif attackChoice == 2:
                        print("You step towards your opponent")
                        distance -= 1
                    
                    else:
                        print()


            
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
                        print(colorama.Fore.GREEN + "You deal:", attackDamage, "damage towards them!")

                    elif attackChoice == 1 and accuracyCheck <= 49:
                        print("Your attack on the opponent misses!")

                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You swing at your opponents legs and hit them, knocking them over!")
                                enemyStun += 1
                            elif stunChance >= 5:
                                print("You swing at your opponents legs and miss!")
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
                        
                        surrenderRNG = random.randint(1, 10)
                        YeaOrNay = surrenderRNG + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")

                            playerSurrender = True
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerSurrenderDamageCheck = True
                            attackDamage = 100
                    
                    else:
                        print()

                elif distance > 4:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1
                    
                    else:
                        print()


        #BLADES~~--~~**~~--~~BLADES~~--~~**~~--~~BLADES~~--~~**~~--~~BLADES~~--~~**~~--~~BLADES~~--~~**~~--~~BLADES~~--~~**~~--~~BLADES#
        elif SpecializationPick.chosenCategory == 2:
            if SpecializationPick.chosenWeapon == 1:
                if distance <= 3:
                    print("Attack [1], Bash (Chance to stun) [2], Step back [3], Surrender [0]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 60:
                        attackRoll = random.randint(25, 35)
                        attackDamage = attackRoll * enemyArmor
                        print()
                        print("You slowly swing your longsword at your opponent!")
                        print(colorama.Fore.GREEN + "You deal:", attackDamage, "damage towards your opponent!")
                    
                    elif attackChoice == 1 and accuracyCheck <= 59:
                        print("Your opponent dodges your slow swing!")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You bash your opponent, stunning them!")
                                enemyStun += 1
                            if stunChance >= 5:
                                print("You try to bash your opponent, but you miss!")
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
                        
                        surrenderRNG = random.randint(1, 10)
                        YeaOrNay = surrenderRNG + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")

                            playerSurrender = True
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerSurrenderDamageCheck = True
                            attackDamage = 100
                    
                    else:
                        print()

                elif distance > 3:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1
                    
                    else:
                        print()
            
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
                        print(colorama.Fore.GREEN + "You deal:", attackDamage, "damage towards your opponent!")
                    
                    if attackChoice == 1 and accuracyCheck <= 39:
                        print("You miss your opponent!")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You bash your opponent, stunning them!")
                                enemyStun += 1
                            elif stunChance >= 5:
                                print("You bash at your opponent but miss!")
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
                        
                        surrenderRNG = random.randint(1, 10)
                        YeaOrNay = surrenderRNG + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")

                            playerSurrender = True
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerSurrenderDamageCheck = True
                            attackDamage = 100

                    else:
                        print()
                
                elif distance > 2:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1
                    
                    else:
                        print()

            elif SpecializationPick.chosenWeapon == 3:
                if distance <= 1:
                    print("Attack [1], Grab (Chance to stun) [2], Step back [3], Surrender [0]")
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
                        print(colorama.Fore.GREEN + "You deal:", attackDamage, "damage towards your opponent!")
                    
                    elif attackChoice == 1 and accuracyCheck <= 19:
                        print("Your opponent dodges!")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You grab your opponent, surprising your them!")
                                enemyStun += 2
                            if stunChance >= 5:
                                print("You try to grab your opponent but they dodge!")
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
                        
                        surrenderRNG = random.randint(1, 10)
                        YeaOrNay = surrenderRNG + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")

                            playerSurrender = True
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerSurrenderDamageCheck = True
                            attackDamage = 100
                    
                    else:
                        print()
                
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
                        print(colorama.Fore.GREEN + "You deal:", attackDamage, "damage towards your opponent!")

                    elif attackChoice == 1 and accuracyCheck <= 29:
                        print("You miss the dagger throw.")

                    elif attackChoice == 2:
                        print("You step towards your opponent")
                        distance -= 1
                    
                    else:
                        print()
        

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
                        print(colorama.Fore.GREEN + "You deal:", attackDamage, "damage towards your opponent!")
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You stunned your opponent!")
                                enemyStun += 1
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 1 and accuracyCheck <= 44:
                        print("You miss!")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 7:
                                print("You bash your opponent, stunning them!")
                                enemyStun += 1
                            if stunChance >= 8:
                                print("you bash at your opponent, but miss!")
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
                        
                        surrenderRNG = random.randint(1, 10)
                        YeaOrNay = surrenderRNG + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")

                            playerSurrender = True
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerSurrenderDamageCheck = True
                            attackDamage = 100
                        
                    else:
                        print()
                
                elif distance > 2:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1
                    
                    else:
                        print()
            
            elif SpecializationPick.chosenWeapon == 2:
                if distance <= 2:
                    print("Attack [1], Bash (Chance to stun) [2], Step back [3], Surrender [0]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1 and accuracyCheck >= 50:
                        attackRoll = random.randint(18, 22)
                        attackDamage = attackRoll
                        print()
                        print("You swing your flail at your opponent!")
                        print(colorama.Fore.GREEN + "You deal:", attackDamage, "damage towards your opponent!")
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You stunned your opponent!")
                                enemyStun += 1
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 1 and accuracyCheck <= 49:
                        print("You miss!")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 7:
                                print("You bash your opponent, stunning them!")
                                enemyStun += 1
                            if stunChance >= 8:
                                print("You bash at your opponent, but you miss!")
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
                        
                        surrenderRNG = random.randint(1, 10)
                        YeaOrNay = surrenderRNG + surrenderScore
                        time.sleep(1.5)
                        if YeaOrNay >= 6:
                            print("The audience decides to let you live.")

                            playerSurrender = True
                        else:
                            print("The audience decides that you shall die.")
                            time.sleep(2)
                            print("Your opponent surprises you, killing you.")
                            playerSurrenderDamageCheck = True
                            attackDamage = 100
                    
                    else:
                        print()
                
                elif distance > 2:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1
                    
                    else:
                        print()


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
                        print(colorama.Fore.GREEN + "You deal:", attackDamage, "damage towards your opponent!")
                    
                    elif attackChoice == 1 and accuracyCheck <= 9:
                        print("Your opponent looks confused as to why you are using fists to fight! (Miss!)")
                    
                    elif attackChoice == 2:
                        if enemyStun == 0:
                            stunChance = random.randint(1, 10)
                            if stunChance <= 4:
                                print("You grab your opponent, stunning them!")
                                enemyStun += 1
                            if stunChance <= 5:
                                print("The opponent dodges your attempt to grab them!")
                        else:
                            print("Your opponent is already stunned!")
                    
                    elif attackChoice == 3:
                        print("You take a step away from the opponent")
                        distance += 1
                    
                    elif attackChoice == 0:
                        print("You yell out that you surrender!")
                        time.sleep(1.5)
                        print("The audience decides to let you live.")

                        playerSurrender = True

                    else:
                        print()
                
                elif distance > 1:
                    print("Step Forward [1]")
                    attackChoice = int(input())
                    os.system('cls')

                    if attackChoice == 1:
                        print("You step towards your opponent")
                        distance -= 1
                    
                    else:
                        print()

    elif playerStun > 0:
        print("You are stunned!")
    
    if attackDamage > 0:
        if playerSurrenderDamageCheck == True:
            playerHitpoints -= attackDamage

        elif SpecializationPick.chosenCategory == 3:
            if SpecializationPick.chosenWeapon == 2:
                enemyHitpoints -= attackDamage
        
        else:
            enemyHitpoints -= attackDamage * enemyArmor
    
    else:
        print()
    if playerStun > 0:
        playerStun -= 1
    

def enemyCombat():
    global enemyStun
    global playerStun
    global distance
    global enemyArmor
    global playerArmor
    global playerHitpoints
    global enemyHitpoints
    global loopBreak
    attackDamage = 0

    if enemyStun == 0:
        accuracyCheck = random.randint(1, 100)
        if enemyWeapon == "Spear":
            if distance <= 3:
                attackChoice = random.randint(1, 3)
                
                if attackChoice == 1 and accuracyCheck >= 35:
                    attackRoll = random.randint(12, 16)
                    attackDamage = attackRoll * playerArmor
                    print("The opponent attacks you with their spear!")
                    print(colorama.Fore.RED + "They dealt:", attackDamage, "damage towards you!")
                
                elif attackChoice == 1 and accuracyCheck <= 34:
                    print("Your opponent misses!")
                
                elif attackChoice == 2:
                    if playerStun == 0:
                        stunChance = random.randint(1, 10)
                        if stunChance <= 4:
                            print("Your opponent swings their spear at your legs, knocking you over!")
                            playerStun += 2
                        if stunChance >= 5:
                                print("Your opponent swings their spear at your legs, but they miss!")
                
                elif attackChoice == 3:
                    print("Your opponent takes a step back!")
                    distance += 1
            
            elif distance >= 4:
                attackChoice = random.randint(1, 2)

                if attackChoice == 1 and accuracyCheck >= 40:
                    attackRoll = random.randint(8, 12)
                    attackDamage = attackRoll * playerArmor
                
                elif attackChoice == 1 and accuracyCheck <= 39:
                    print("Your opponent throws their spear at you and misses!")
                
                elif attackChoice == 2:
                    print("Your opponent steps forwards!")
                    distance -= 1


        elif enemyWeapon == "Dagger":
            if distance <= 1:
                attackChoice = random.randint(1, 3)
                
                if attackChoice == 1 and accuracyCheck >= 20:
                    if playerStun > 0:
                        attackRoll = random.randint(30, 40)
                        attackDamage = attackRoll * enemyArmor
                    else:
                        attackRoll = random.randint(2, 8)
                        attackDamage = attackRoll * enemyArmor
                    print("The opponent stabs you!")
                    print(colorama.Fore.RED + "They dealt:", attackDamage, "damage towards you!")
                
                elif attackChoice == 1 and accuracyCheck <= 19:
                    print("Your opponent misses!")
                
                elif attackChoice == 2:
                    if playerStun == 0:
                        stunChance = random.randint(1, 10)
                        if stunChance <= 4:
                            print("Your opponent grabs you, making you stunned!")
                            playerStun += 2
                        if stunChance >= 5:
                                print("Your opponent attempts to grab you, but they miss!")
                
                elif attackChoice == 3:
                    print("Your opponent takes a step back!")
                    distance += 1
            
            elif distance >= 2:
                attackChoice = random.randint(1, 2)

                if attackChoice == 1 and accuracyCheck >= 30:
                    attackRoll = random.randint(4, 8)
                    attackDamage = attackRoll * playerArmor
                
                elif attackChoice == 1 and accuracyCheck <= 29:
                    print("Your opponent throws their dagger at you and misses!")
                
                elif attackChoice == 2:
                    print("Your opponent steps forwards!")
                    distance -= 1
                        
        elif enemyWeapon == "Shortsword":
            if distance <= 2:
                attackChoice = random.randint(1, 3)

                if attackChoice == 1 and accuracyCheck >= 40:
                    attackRoll = random.randint(8, 12)
                    attackDamage = attackRoll * enemyArmor
                    print("Your opponent swings their sword you!")
                    print(colorama.Fore.RED + "They dealt:", attackDamage, "damage towards you!")

                elif attackChoice == 1 and accuracyCheck <= 39:
                    print("Your opponent swings their sword at you and miss!")
                
                elif attackChoice == 2:
                    if playerStun == 0:
                        stunChance = random.randint(1, 10)
                        if stunChance <= 4:
                            print("Your opponent bashes at you, making you stunned!")
                            playerStun += 2
                        if stunChance >= 5:
                                print("Your opponent attempts to bash you, but they miss!")

                elif attackChoice == 3:
                    print("Your opponent takes a step back!")
                    distance += 1
                
            elif distance >= 3:
                attackChoice = random.randint(1, 1)
                if attackChoice == 1:
                    print("Your opponent takes a step forward!")
                    distance -= 1

        elif enemyWeapon == "Longsword":
            if distance <= 2:
                attackChoice = random.randint(1, 3)

                if attackChoice == 1 and accuracyCheck >= 60:
                    attackRoll = random.randint(25, 35)
                    attackDamage = attackRoll * enemyArmor
                    print("Your opponent slowly swings their longsword at you!")
                    print(colorama.Fore.RED + "They dealt:", attackDamage, "damage towards you!")

                elif attackChoice == 1 and accuracyCheck <= 59:
                    print("Your opponent swings their longsword at you and miss!")
                    
                elif attackChoice == 2:
                    if playerStun == 0:
                        stunChance = random.randint(1, 10)
                        if stunChance <= 4:
                            print("Your opponent bashes at you, making you stunned!")
                            playerStun += 2
                        if stunChance >= 5:
                                print("Your opponent attempts to bash you, but they miss!")

                elif attackChoice == 3:
                    print("Your opponent takes a step back!")
                    distance += 1
                    
            elif distance >= 3:
                attackChoice = random.randint(1, 1)
                if attackChoice == 1:
                    print("Your opponent takes a step forward!")
                    distance -= 1
        
        elif enemyWeapon == "Mace":
            if distance <= 2:
                attackChoice = random.randint(1, 3)

                if attackChoice == 1 and accuracyCheck >= 45:
                    attackRoll = random.randint(8, 12)
                    attackDamage = attackRoll * enemyArmor
                    print("Your opponent swings their mace at you!")
                    print(colorama.Fore.RED + "They dealt:", attackDamage, "damage towards you!")
                    if playerStun == 0:
                        stunChance = random.randint(1, 10)
                        if stunChance <= 4:
                                print("Your opponent stunned you!")
                                playerStun += 1

                elif attackChoice == 1 and accuracyCheck <= 44:
                    print("Your opponent swings their mace at you and miss!")
                
                elif attackChoice == 2:
                    if playerStun == 0:
                        stunChance = random.randint(1, 10)
                        if stunChance <= 4:
                            print("Your opponent bashes at you, making you stunned!")
                            playerStun += 2
                        if stunChance >= 5:
                                print("Your opponent attempts to bash you, but they miss!")

                elif attackChoice == 3:
                    print("Your opponent takes a step back!")
                    distance += 1
                
            elif distance >= 3:
                attackChoice = random.randint(1, 1)
                if attackChoice == 1:
                    print("Your opponent takes a step forward!")
                    distance -= 1
        
        elif enemyWeapon == "Flail":
            if distance <= 2:
                attackChoice = random.randint(1, 3)

                if attackChoice == 1 and accuracyCheck >= 50:
                    attackRoll = random.randint(18, 22)
                    attackDamage = attackRoll * enemyArmor
                    print("Your opponent flings their flail at you!")
                    print(colorama.Fore.RED + "They dealt:", attackDamage, "damage towards you!")
                    if playerStun == 0:
                        stunChance = random.randint(1, 10)
                        if stunChance <= 4:
                                print("Your opponent stunned you!")
                                playerStun += 1

                elif attackChoice == 1 and accuracyCheck <= 49:
                    print("Your opponent swings their sword at you and miss!")
                
                elif attackChoice == 2:
                    if playerStun == 0:
                        stunChance = random.randint(1, 10)
                        if stunChance <= 4:
                            print("Your opponent bashes at you, making you stunned!")
                            playerStun += 2
                        if stunChance >= 5:
                                print("Your opponent attempts to bash you, but they miss!")

                elif attackChoice == 3:
                    print("Your opponent takes a step back!")
                    distance += 1
                
            elif distance >= 3:
                attackChoice = random.randint(1, 1)
                if attackChoice == 1:
                    print("Your opponent takes a step forward!")
                    distance -= 1

        elif enemyWeapon == "Trident":
            if distance <= 3:
                attackChoice = random.randint(1, 3)

                if attackChoice == 1 and accuracyCheck >= 50:
                    attackRoll = random.randint(16, 20)
                    attackDamage = attackRoll * enemyArmor
                    print("Your opponent thrusts their trident into you!")
                    print(colorama.Fore.RED + "They dealt:", attackDamage, "damage towards you!")

                elif attackChoice == 1 and accuracyCheck <= 49:
                    print("Your thrusts their trident at you and miss!")
                
                elif attackChoice == 2:
                    if playerStun == 0:
                        stunChance = random.randint(1, 10)
                        if stunChance <= 4:
                            print("Your opponent swings their trident at you, knocking you over!")
                            playerStun += 2
                        if stunChance >= 5:
                                print("Your opponent attempts to knock you over, but they miss!")

                elif attackChoice == 4:
                    print("Your opponent takes a step back!")
                    distance += 1
                
            elif distance >= 4:
                attackChoice = random.randint(1, 1)
                if attackChoice == 1:
                    print("Your opponent takes a step forward!")
                    distance -= 1
        
        elif enemyWeapon == "Fists":
            if distance <= 1:
                attackChoice = random.randint(1, 3)

                if attackChoice == 1 and accuracyCheck >= 10:
                    attackRoll = random.randint(1, 3)
                    attackDamage = attackRoll * enemyArmor
                    print("Your opponent punches you!")
                    print(colorama.Fore.RED + "They dealt:", attackDamage, "damage towards you!")

                elif attackChoice == 1 and accuracyCheck <= 9:
                    print("Your opponent attempts to punch you and miss!")
                
                elif attackChoice == 2:
                    if playerStun == 0:
                        stunChance = random.randint(1, 10)
                        if stunChance <= 4:
                            print("Your opponent bashes at you, making you stunned!")
                            playerStun += 2
                        if stunChance >= 5:
                                print("Your opponent attempts to bash you, but they miss!")

                elif attackChoice == 3:
                    print("Your opponent takes a step back!")
                    distance += 1
                
            elif distance >= 2:
                attackChoice = random.randint(1, 1)
                if attackChoice == 1:
                    print("Your opponent takes a step forward!")
                    distance -= 1
    elif enemyStun > 0:
        print("Your opponent is stunned!")

    if attackDamage > 0:
        if enemyWeapon == "Flail":
            playerHitpoints -= attackDamage
        
        else:
            playerHitpoints -= attackDamage
    
    else:
        print()
    if enemyStun > 0:
        enemyStun -= 1