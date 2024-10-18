import colorama
import time

# def lägg_ihop_tal ():
#     summa = 10 + 20
#     return summa

# min_nya_summa = lägg_ihop_tal()
# print(min_nya_summa)

def specializationPick():
    time.sleep(1.5)
    global weapon

    print("You can choose from the following categories' weapons (Stat changes will be previewed):")
    while True: #The code below asks the user to pick a category of weapons, then a weapon. The stats of the picked weapon
                #Will then be previewed before the player makes a choice.

        print("Spears [1]")
        print("Blades [2]")
        print("Blunt Weaponry [3]")
        print("Other [4]")
        CategoryChoice = int(input())

        if CategoryChoice == 1:
            print("Spear [1]")
            print("Trident [2]")
            WeaponChoiceCat = int(input())

            if WeaponChoiceCat == 1:
                print("stats")

                print("Pick this weapon? Yes [1] or No [2]")
                confirm = int(input())
                if confirm == 1:
                    weapon = "Spear"
                    return weapon
                else:
                    continue

            elif WeaponChoiceCat == 2:
                print("stats")
                
                print("Pick this weapon? Yes [1] or No [2]")
                confirm = int(input())
                if confirm == 1:
                    weapon = "Trident"
                    return weapon

        
        elif CategoryChoice == 2:
            print("Longsword [1]")
            print("Shortsword [2]")
            print("Dagger [3]")
            WeaponChoiceCat = int(input())

            if WeaponChoiceCat == 1:
                print("stats")

            elif WeaponChoiceCat == 2:
                print("stats")

            elif WeaponChoiceCat == 3:
                print("stats")


        elif CategoryChoice == 3:
            print("Mace [1]")
            WeaponChoiceCat = int(input())

            if WeaponChoiceCat == 1:
                print("stats")


        elif CategoryChoice == 4:
            print("Fists [1]")
            WeaponChoiceCat = int(input())

            if WeaponChoiceCat == 1:
                print("stats")