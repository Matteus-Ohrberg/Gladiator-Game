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
global weaponSetMatches
global reloadTime
global blockingEnemy


enemyHitpoints = 100 # Set to 100 in order to prevent potential bugs (and to allow modification elsewhere.)
playerHitpoints = 100 # 100 by default.
stageCounter = 0 # To be modified in glad. main. Will also be used for unlocking more weapons.
distance = 10 # Distance 10 by default, will probably be modified per battle.
chosenWeapon = "Fists"
reloadTime = 0 # Reload time for the ranged weapons.
blockingEnemy = 1 # Used in damage calculation.




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
    accuracyCheck = random.randint(1, 100)

    if chosenWeapon == "Longbow":
        if distance > 3:
            print("Attack [1], Step back [2]")
            print()
            attackChoice = int(input())

            if attackChoice == 1 and accuracyCheck <= 65:
                attackDamage = random.randint(15, 25)

                print("You aim at your opponent while drawing your bow, shooting the arrow!")
                print("You deal", attackDamage, "to your opponent")
                
            elif attackChoice == 1 and accuracyCheck > 65:
                print("You missed your attack!")
                
            else:
                print("You go towards your opponent!")
                distance -= 1
        
        if distance <= 3:
            print("Attack [1], Block [2], Step forward [3]")
            attackChoice = int(input())

            if attackChoice == 1 and accuracyCheck <= 75:
                attackDamage = random.randint(6, 12)

                print("You stab your opponent!")
                print("You deal", attackDamage, "to your opponent")
                
            elif attackChoice == 1 and accuracyCheck > 65:
                print("You missed your attack!")
                
            else:
                print("You back away from your opponent!")
                distance += 1

    elif chosenWeapon == "Shortbow":
    
    elif chosenWeapon == "Crossbow":
    
    elif chosenWeapon == "Spear":
    
    elif chosenWeapon == "Trident":
    
    elif chosenWeapon == "Longsword":
    
    elif chosenWeapon == "Shortsword":
    
    elif chosenWeapon == "Dagger":
    
    elif chosenWeapon == "Fists":