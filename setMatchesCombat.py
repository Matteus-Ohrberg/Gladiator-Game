import colorama
from colorama import init
import os
import time
import playerCombat
import random

init(autoreset=True)

global playerHitpoints # I realised in the middle of making this game that using so many global variables is
global stageCounter # making the code hard to read.
global enemyHitpoints # There is also a higher than likely chance that I am using the global declaration wrong.
global distance # It works however, which is nice.
global stunPlayer
global stunEnemy
global weaponSetMatches # I do not remember why I added this.
global reloadTime
global blockingEnemy
global onePunchMan


enemyHitpoints = 100 # Set to 100 in order to prevent potential bugs (and to allow modification elsewhere.)
playerHitpoints = 100 # 100 by default.
stageCounter = 0 # To be modified in glad. main. Will also be used for unlocking more weapons.
distance = 10 # Distance 10 by default, will probably be modified per battle.
chosenWeapon = "Fists"
reloadTime = 0 # Reload time for the ranged weapons.
blockingEnemy = 1 # Used in damage calculation.
onePunchMan = 1 # I trained every day for 3 years, I became so strong I went bald.

# stunPlayer = 0 # Will probably be used.




def weaponPickSetMatches(): # Basically specializationPick module but modified for setmatches mode
    global chosenWeapon
    while True:
        os.system('cls')
        print("Pick a weapon for your next battle.")
        print("You are able to back out of menus by typing a number that isn't listed.")
        print()
        print("Ranged [1], Long Melee [2], Medium Melee [3], Short Melee [4]")
        categoryPick = int(input())

        if categoryPick == 1:
            os.system('cls')
            print("Longbow [1], Shortbow [2], Crossbow [3]")
            print("If you get in melee range of your opponent, you will use a dagger for combat.")
            print()
            weaponPick = int(input())

            if weaponPick == 1:
                os.system('cls')
                print("Longbow:")
                print(colorama.Fore.GREEN + "Usable at a long distance")
                print("Reload time:", colorama.Fore.YELLOW + "1 round")
                print(colorama.Fore.GREEN + "High damage")
                print(colorama.Fore.YELLOW + "Normal Accuracy")
                print("Confirm weapon? Yes [1], No [2]")

                confirmation = int(input())
                if confirmation == 1:
                    chosenWeapon = "Longbow"
                    os.system('cls')
                    break
                
                else:
                    continue
            
            elif weaponPick == 2:
                os.system('cls')
                print("Shortbow:")
                print(colorama.Fore.GREEN + "Usable at a long distance")
                print("Reload time:", colorama.Fore.YELLOW + "0 rounds")
                print(colorama.Fore.YELLOW + "Normal damage")
                print(colorama.Fore.YELLOW + "Normal Accuracy")
                print("Confirm weapon? Yes [1], No [2]")

                confirmation = int(input())
                if confirmation == 1:
                    chosenWeapon = "Shortbow"
                    os.system('cls')
                    break

                else:
                    continue
            
            elif weaponPick == 3:
                os.system('cls')
                print("Crossbow:")
                print(colorama.Fore.GREEN + "Usable at a long distance")
                print("Reload time:", colorama.Fore.RED + "3 rounds")
                print(colorama.Fore.GREEN + "Very High damage")
                print(colorama.Fore.GREEN + "High accuracy")
                print("Confirm weapon? Yes [1], No [2]")

                confirmation = int(input())
                if confirmation == 1:
                    chosenWeapon = "Crossbow"
                    os.system('cls')
                    break

                else:
                    continue
            
            else:
                continue

######################################### shitty separator

        elif categoryPick == 2:
            os.system('cls')
            print("Spear [1], Trident [2]")
            print()
            weaponPick = int(input())

            if weaponPick == 1:
                os.system('cls')
                print("Spear:")
                print(colorama.Fore.GREEN + "High Range and throwable")
                print(colorama.Fore.YELLOW + "Normal accuracy")
                print(colorama.Fore.YELLOW + "Normal damage")
                print("Confirm weapon? Yes [1], No [2]")

                confirmation = int(input())
                if confirmation == 1:
                    chosenWeapon = "Spear"
                    os.system('cls')
                    break
                
                else:
                    continue
            
            elif weaponPick == 2:
                os.system('cls')
                print("Trident:")
                print(colorama.Fore.GREEN + "High Range")
                print(colorama.Fore.YELLOW + "Normal accuracy")
                print(colorama.Fore.GREEN + "High damage")
                print("Confirm weapon? Yes [1], No [2]")

                confirmation = int(input())
                if confirmation == 1:
                    chosenWeapon = "Trident"
                    os.system('cls')
                    break

                else:
                    continue
            
            else:
                continue
        
############################################################ Shitty separator.

        elif categoryPick == 3:
            os.system('cls')
            print("Longsword [1], Shortsword [2]")
            print()
            weaponPick = int(input())

            if weaponPick == 1:
                os.system('cls')
                print("Longsword:")
                print(colorama.Fore.YELLOW + "Normal range")
                print(colorama.Fore.RED + "Low accuracy")
                print(colorama.Fore.GREEN + "High damage")
                print("Confirm weapon? Yes [1], No [2]")

                confirmation = int(input())
                if confirmation == 1:
                    chosenWeapon = "Longsword"
                    os.system('cls')
                    break
                
                else:
                    continue
            
            elif weaponPick == 2:
                os.system('cls')
                print("Shortsword:")
                print(colorama.Fore.YELLOW + "Normal range")
                print(colorama.Fore.YELLOW + "Normal accuracy")
                print(colorama.Fore.YELLOW + "Normal damage")
                print("Confirm weapon? Yes [1], No [2]")

                confirmation = int(input())
                if confirmation == 1:
                    chosenWeapon = "Shortsword"
                    os.system('cls')
                    break

                else:
                    continue
            
            else:
                continue

#####################################################

        elif categoryPick == 4:
            os.system('cls')
            print("Dagger [1], Fists [2]")
            print()
            weaponPick = int(input())

            if weaponPick == 1:
                os.system('cls')
                print("Dagger:")
                print(colorama.Fore.RED + "Low range")
                print(colorama.Fore.GREEN + "High accuracy")
                print(colorama.Fore.YELLOW + "Normal damage")
                print("Confirm weapon? Yes [1], No [2]")

                confirmation = int(input())
                if confirmation == 1:
                    chosenWeapon = "Dagger"
                    os.system('cls')
                    break
                
                else:
                    continue
            
            elif weaponPick == 2:
                os.system('cls')
                print("Fists:")
                print(colorama.Fore.RED + "Low range")
                print(colorama.Fore.GREEN + "Very high accuracy")
                print(colorama.Fore.RED + "Very low damage")
                print("Confirm weapon? Yes [1], No [2]")

                confirmation = int(input())
                if confirmation == 1:
                    chosenWeapon = "Fists"
                    os.system('cls')
                    break

                else:
                    continue
            
            else:
                continue

def playerSetCombat():
    global chosenWeapon
    global enemyHitpoints
    global blockingEnemy
    global distance
    global reloadTime
    global onePunchMan
    accuracyCheck = random.randint(1, 100) # Accuracy checks for attacks.

    if chosenWeapon == "Longbow": # If you read this, you should probably understand the rest of the weapons.
        if reloadTime == 0: # Applies to bows only, if this is higher than 0 then tell player they're reloading
            if distance > 3: # if distance is more than 3, do the stuff below
                print("You are:", distance * 2, "meters away from your opponent! (Longbow active)")
                print("Attack [1], Step back [2]")
                print()
                attackChoice = int(input()) # Asks user for a choice

                if attackChoice == 1 and accuracyCheck <= 65: # If player has chosen to attack and accuracyCheck is 65 or below
                    attackDamage = random.randint(15, 25) # Do the following amount of damage

                    print("You aim at your opponent while drawing your bow, shooting the arrow!")
                    print("You deal", attackDamage, "to your opponent")
                    reloadTime += 1 # If player attacks, add +1 to reload time.
                    
                elif attackChoice == 1 and accuracyCheck > 65:
                    print("You missed your attack!")
                    reloadTime += 1 # As above.
                    
                else:
                    print("You go towards your opponent!")
                    distance -= 1
            
            elif distance <= 3:
                print("You are:", distance * 2, "meters away from your opponent! (Dagger active)")
                print("Attack [1], Block [2], Step forward [3]")
                print()
                attackChoice = int(input())

                if attackChoice == 1 and accuracyCheck <= 75:
                    attackDamage = random.randint(6, 12)

                    print("You stab your opponent!")
                    print("You deal", attackDamage, "to your opponent")
                    
                elif attackChoice == 1 and accuracyCheck > 75:
                    print("You missed your attack!")

                elif attackChoice == 2:
                    print("You block your opponents attack!")
                    blockingEnemy = 0.2 # Blocking is set to 0.2, reducing damage taken by 80% for the next attack by enemy.
                    
                else:
                    print("You back away from your opponent!")
                    distance += 1
        
        else:
            print("You are readying your longbow for the next shot!", reloadTime, "turns left!") 


    elif chosenWeapon == "Shortbow":
        if reloadTime == 0:
            if distance > 3:
                print("You are:", distance * 2, "meters away from your opponent! (Shortbow active)")
                print("Attack [1], Step back [2]")
                print()
                attackChoice = int(input())

                if attackChoice == 1 and accuracyCheck <= 65:
                    attackDamage = random.randint(10, 18)

                    print("You aim at your opponent while drawing your bow, shooting the arrow!")
                    print("You deal", attackDamage, "to your opponent")
                    
                elif attackChoice == 1 and accuracyCheck > 65:
                    print("You missed your attack!")
                    
                else:
                    print("You go towards your opponent!")
                    distance -= 1
            
            if distance <= 3:
                print("You are:", distance * 2, "meters away from your opponent! (Dagger active)")
                print("Attack [1], Block [2], Step forward [3]")
                print()
                attackChoice = int(input())

                if attackChoice == 1 and accuracyCheck <= 75:
                    attackDamage = random.randint(6, 12)

                    print("You stab your opponent!")
                    print("You deal", attackDamage, "to your opponent")
                    
                elif attackChoice == 1 and accuracyCheck > 75:
                    print("You missed your attack!")

                elif attackChoice == 2:
                    print("You block your opponents attack!")
                    blockingEnemy = 0.2
                    
                else:
                    print("You back away from your opponent!")
                    distance += 1
        
        else:
            print("You are readying your shortbow for the next shot!", reloadTime, "turns left!")
    

    elif chosenWeapon == "Crossbow":
        if reloadTime == 0:
            if distance > 3:
                print("You are:", distance * 2, "meters away from your opponent! (Crossbow active)")
                print("Attack [1], Step back [2]")
                print()
                attackChoice = int(input())

                if attackChoice == 1 and accuracyCheck <= 75:
                    attackDamage = random.randint(20, 32)

                    print("You aim at your opponent and shoot the arrow!")
                    print("You deal", attackDamage, "to your opponent")
                    reloadTime += 2
                    
                elif attackChoice == 1 and accuracyCheck > 75:
                    print("You missed your attack!")
                    reloadTime += 2
                    
                else:
                    print("You go towards your opponent!")
                    distance -= 1
            
            elif distance <= 3:
                print("You are:", distance * 2, "meters away from your opponent! (Dagger active)")
                print("Attack [1], Block [2], Step forward [3]")
                print()
                attackChoice = int(input())

                if attackChoice == 1 and accuracyCheck <= 75:
                    attackDamage = random.randint(6, 12)

                    print("You stab your opponent!")
                    print("You deal", attackDamage, "to your opponent")
                    
                elif attackChoice == 1 and accuracyCheck > 75:
                    print("You missed your attack!")

                elif attackChoice == 2:
                    print("You block your opponents attack!")
                    blockingEnemy = 0.2
                    
                else:
                    print("You back away from your opponent!")
                    distance += 1
        
        else:
            print("You are readying your shortbow for the next shot!", reloadTime, "turns left!")


    elif chosenWeapon == "Spear":
        if distance <= 3: # Reversed from bows. If distance is equal to or less than 3, print normal "menu"
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Attack [1], Block [2] Step back [3]")
            print()
            attackChoice = int(input())

            if attackChoice == 1 and accuracyCheck <= 65:
                attackDamage = random.randint(10, 18)

                print("You stab at your opponent!")
                print("You deal", attackDamage, "to your opponent")
                    
            elif attackChoice == 1 and accuracyCheck > 65:
                print("You missed your attack!")

            elif attackChoice == 2:
                print("You block your opponents attack!")
                blockingEnemy = 0.2
                    
            else:
                print("You back away from your opponent!")
                distance += 1
            
        elif distance > 3:
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Throw [1], Step forward [2]")
            print()
            attackChoice = int(input())

            if attackChoice == 1 and accuracyCheck <= 65:
                attackDamage = random.randint(10, 18)

                print("You throw your spear at the opponent!") # No reload times on spears, Though that might be unwise.
                print("You deal", attackDamage, "to your opponent")
                    
            elif attackChoice == 1 and accuracyCheck > 65:
                print("You missed your attack!")
                    
            else:
                print("You step towards your opponent!")
                distance -= 1

    
    elif chosenWeapon == "Trident":
        if distance <= 3:
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Attack [1], Block [2] Step back [3]")
            print()
            attackChoice = int(input())

            if attackChoice == 1 and accuracyCheck <= 65:
                attackDamage = random.randint(20, 25)

                print("You stab at your opponent!")
                print("You deal", attackDamage, "to your opponent")
                    
            elif attackChoice == 1 and accuracyCheck > 65:
                print("You missed your attack!")

            elif attackChoice == 2:
                print("You block your opponents attack!")
                blockingEnemy = 0.2
                    
            else:
                print("You back away from your opponent!")
                distance += 1
            
        elif distance > 3:
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Step forward [1]")
            print()
            attackChoice = int(input())

            print("You step towards your opponent")
            distance -= 1
           
    
    elif chosenWeapon == "Longsword":
        if distance <= 2:
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Attack [1], Block [2] Step back [3]")
            print()
            attackChoice = int(input())

            if attackChoice == 1 and accuracyCheck <= 55:
                attackDamage = random.randint(23, 28)

                print("You swing at your opponent!")
                print("You deal", attackDamage, "to your opponent")
                    
            elif attackChoice == 1 and accuracyCheck > 55:
                print("You missed your attack!")

            elif attackChoice == 2:
                print("You block your opponents attack!")
                blockingEnemy = 0.2
                    
            else:
                print("You back away from your opponent!")
                distance += 1
            
        elif distance > 2:
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Step forward [1]")
            print()
            attackChoice = int(input())

            print("You step towards your opponent")
            distance -= 1
    

    elif chosenWeapon == "Shortsword":
        if distance <= 2:
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Attack [1], Block [2] Step back [3]")
            print()
            attackChoice = int(input())

            if attackChoice == 1 and accuracyCheck <= 65:
                attackDamage = random.randint(10, 18)

                print("You swing at your opponent!")
                print("You deal", attackDamage, "to your opponent")
                    
            elif attackChoice == 1 and accuracyCheck > 65:
                print("You missed your attack!")

            elif attackChoice == 2:
                print("You block your opponents attack!")
                blockingEnemy = 0.2
                    
            else:
                print("You back away from your opponent!")
                distance += 1
            
        elif distance > 2:
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Step forward [1]")
            print()
            attackChoice = int(input())

            print("You step towards your opponent")
            distance -= 1

    
    elif chosenWeapon == "Dagger":
        if distance <= 2:
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Attack [1], Block [2] Step back [3]")
            print()
            attackChoice = int(input())

            if attackChoice == 1 and accuracyCheck <= 90:
                attackDamage = random.randint(10, 18)

                print("You stab your opponent!")
                print("You deal", attackDamage, "to your opponent")
                    
            elif attackChoice == 1 and accuracyCheck > 90:
                print("You missed your attack!")

            elif attackChoice == 2:
                print("You block your opponents attack!")
                blockingEnemy = 0.2
                    
            else:
                print("You back away from your opponent!")
                distance += 1
            
        elif distance > 2:
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Step forward [1]")
            print()
            attackChoice = int(input())

            print("You step towards your opponent")
            distance -= 1
    
    elif chosenWeapon == "Fists":
        if distance <= 1:
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Punch [1], Block [2] ,Step back [3]")
            print()
            attackChoice = int(input())

            if attackChoice == 1 and accuracyCheck <= 99:
                attackDamage = random.randint(3, 7)

                print("You punch at your opponent!")
                print("You deal", attackDamage ** onePunchMan, "to your opponent")
                onePunchMan += 0.3 # In order to make fists viable, I have made them exponentially better. Difficult early match.
                    
            elif attackChoice == 1 and accuracyCheck > 99:
                print("You missed your attack!")

            elif attackChoice == 2:
                print("You block your opponents attack!")
                blockingEnemy = 0.2
                    
            else:
                print("You back away from your opponent!")
                distance += 1
            
        elif distance > 1:
            print("You are:", distance * 2, "meters away from your opponent!")
            print("Step forward [1]")
            print()
            attackChoice = int(input())

            print("You step towards your opponent")
            distance -= 1
    

    enemyHitpoints -= attackDamage ** onePunchMan # This calculation wont interfere normal damage calculations, as oPM is set to 1.