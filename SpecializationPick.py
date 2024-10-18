import colorama
import time
from colorama import init
import os

init(autoreset=True)

def specializationPicker():
    global chosenCategory #This was my solution, make 2 variables global in order to use it in other files
    global chosenWeapon   #By doing this, I will not have to call upon a function each time I want to check stats.
    HasWeaponBeenPicked = False

    while HasWeaponBeenPicked == False: #While loop to allow stat showcase and confirmation of weapon pick.
        os.system('cls')
        print("Remember: You cannot change weapon until the dev adds a way!")
        print("Categories: Spears [1], Blades [2], Blunt Weaponry [3], Other [4]")
        categoryChoicePick = int(input())

        if categoryChoicePick == 1: #Would probably be better if I used str instead of int. Though typos may break the code.
            os.system('cls')
            print("Weapons: Spear [1], Trident [2]")
            weaponChoicePick = int(input())

            if weaponChoicePick == 1:
                os.system('cls')
                print("Spear: a wood rod with a top made of metal. Optimal for stabbing at a distance and throwing.")
                print()
                print(colorama.Fore.GREEN + "Normal increase in accuracy")
                print(colorama.Fore.GREEN + "Normal increase in damage")
                print(colorama.Fore.GREEN + "Great increase in range")
                print(colorama.Fore.GREEN + "Throwable")
                print("Equip this weapon? Yes [1] or No [2]")
                weaponConfirm = int(input())

                if weaponConfirm == 1:
                    chosenCategory = 1
                    chosenWeapon = 1
                    HasWeaponBeenPicked = not HasWeaponBeenPicked
            
            elif weaponChoicePick == 2:
                os.system('cls')
                print("Trident: Traditionally used for hunting fish, a trident will do more damage at the cost of accuracy and throwing.")
                print()
                print(colorama.Fore.RED + "Small decrease in accuracy")
                print(colorama.Fore.GREEN + "Great increase in damage")
                print(colorama.Fore.GREEN + "Great increase in range")
                print("Equip this weapon? Yes [1] or No [2]")
                weaponConfirm = int(input())

                if weaponConfirm == 1:
                    chosenCategory = 1
                    chosenWeapon = 2
                    HasWeaponBeenPicked = not HasWeaponBeenPicked
        
######################################################################################### Unpleasant, seperates categories neatly.
        elif categoryChoicePick == 2:
            os.system('cls')
            print("Weapons: Longsword [1], Shortsword [2], Dagger [3]")
            weaponChoicePick = int(input())

            if weaponChoicePick == 1:
                os.system('cls')
                print("Longsword: A heavy two handed sword that will devastate enemies in exchange for your shield.")
                print()
                print(colorama.Fore.LIGHTBLUE_EX + "Normal Accuracy")
                print(colorama.Fore.GREEN + "Massive increase in damage")
                print(colorama.Fore.GREEN + "Normal increase in range")
                print(colorama.Fore.RED + "No shield")
                print("Equip this weapon? Yes [1] or No [2]")
                weaponConfirm = int(input())

                if weaponConfirm == 1:
                    chosenCategory = 2
                    chosenWeapon = 1
                    HasWeaponBeenPicked = not HasWeaponBeenPicked
            
            elif weaponChoicePick == 2:
                os.system('cls')
                print("Shortsword: A trusty ol' sword. Reliable and unexceptional.")
                print()
                print(colorama.Fore.LIGHTBLUE_EX + "Normal accuracy")
                print(colorama.Fore.LIGHTBLUE_EX + "Normal damage")
                print(colorama.Fore.LIGHTBLUE_EX + "Normal range")
                print("Equip this weapon? Yes [1] or No [2]")
                weaponConfirm = int(input())

                if weaponConfirm == 1:
                    chosenCategory = 2
                    chosenWeapon = 2
                    HasWeaponBeenPicked = not HasWeaponBeenPicked
            
            elif weaponChoicePick == 3:
                os.system('cls')
                print("Dagger: This weapon has a low range putting you in harms way but will do immense damage on stunned enemies.")
                print()
                print(colorama.Fore.GREEN + "High increase in accuracy")
                print(colorama.Fore.RED + "Low damage,", colorama.Fore.YELLOW + "massive damage on stunned enemies")
                print(colorama.Fore.RED + "Low range")
                print(colorama.Fore.GREEN + "Throwable, low damage.")
                print("Equip this weapon? Yes [1] or No [2]")
                weaponConfirm = int(input())

                if weaponConfirm == 1:
                    chosenCategory = 2
                    chosenWeapon = 3
                    HasWeaponBeenPicked = not HasWeaponBeenPicked

######################################################################################### Unpleasant, seperates categories neatly.
        elif categoryChoicePick == 3:
            os.system('cls')
            print("Weapons: Mace [1], Flail [2]")
            weaponChoicePick = int(input())

            if weaponChoicePick == 1:
                os.system('cls')
                print("Mace: This weapon puts all the force of a hit on a concentrated spot which could cause an enemy to be stunned!")
                print()
                print(colorama.Fore.RED + "Small decrease in accuracy")
                print(colorama.Fore.GREEN + "High increase in damage")
                print(colorama.Fore.LIGHTBLUE_EX + "Normal range")
                print(colorama.Fore.YELLOW + "Chance to stun enemies!")
                print("Equip this weapon? Yes [1] or No [2]")
                weaponConfirm = int(input())

                if weaponConfirm == 1:
                    chosenCategory = 3
                    chosenWeapon = 1
                    HasWeaponBeenPicked = not HasWeaponBeenPicked
            
            elif weaponChoicePick == 2:
                os.system('cls')
                print("Flail: A side-grade of the mace, this one trades in more accuracy in exchange for bypassing shields!")
                print()
                print(colorama.Fore.RED + "Medium decrease in accuracy")
                print(colorama.Fore.GREEN + "High increase in damage")
                print(colorama.Fore.LIGHTBLUE_EX + "Normal range")
                print(colorama.Fore.YELLOW+ "Bypasses shield, may stun enemy!")
                print("Equip this weapon? Yes [1] or No [2]")
                weaponConfirm = int(input())

                if weaponConfirm == 1:
                    chosenCategory = 3
                    chosenWeapon = 2
                    HasWeaponBeenPicked = not HasWeaponBeenPicked
            
######################################################################################### Unpleasant, seperates categories neatly.
        elif categoryChoicePick == 4:
            os.system('cls')
            print("Weapons: Fists [1]")
            weaponChoicePick = int(input())

            if weaponChoicePick == 1:
                os.system('cls')
                print("Fists: Beat someone to death using your fists, gain glory and trauma.")
                print()
                print(colorama.Fore.GREEN + "Massive increase in accuracy")
                print(colorama.Fore.RED + "Massive decrease in damage")
                print(colorama.Fore.RED + "Small decrease in range")
                print(colorama.Fore.YELLOW + "If you surrender, the audience WILL grant you mercy")
                print("Equip this weapon? Yes [1] or No [2]")
                weaponConfirm = int(input())

                if weaponConfirm == 1:
                    chosenCategory = 4
                    chosenWeapon = 1
                    HasWeaponBeenPicked = not HasWeaponBeenPicked