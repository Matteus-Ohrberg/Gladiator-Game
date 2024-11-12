import time
import colorama
import random
import playerCombat # For all things combat. And endless mode
import SetMatches # for set matches, also, I accidentally capitalised the S in set
import SpecializationPick # Originally this module was created to keep playerCombat short in length, it did not work.
from colorama import init
import os

import SetMatches # Enemy ""AI"" in this module for set matches.
import setMatchesCombat # Better combat made for set matches mode.

init(autoreset=True)

os.system('cls')

print("Welcome to [GAME NAME]! Please select a gamemode and difficulty")
print(colorama.Fore.CYAN + "PLEASE NOTE: USE ONLY NUMBERS WHEN SELECTING ANYTHING, THE GAME WILL STOP WORKING IF YOU USE LETTERS")
input("Press enter to continue.")


os.system('cls')

print("Select a gamemode: Endless [1], set-matches [2]")
print("Endless is a mode that will not end until you lose, HP is reset every round.")
print("Endless increases enemy HP per round, increasing until it becomes impossible to win.")
print()
print("Set-matches is 10 matches in increasing difficulty.")
print("Set-matches is also a tiny bit more fleshed out, albeit basically the same.")
modeSelect = int(input())

os.system('cls')


if modeSelect == 1: #Endless mode.

    playerCombat.difficultySelect()
    os.system('cls')
    print("Select your equipment specialization.") #Starts with allowing player to select weapon and armor
    print()
    input("Press enter to continue")
    SpecializationPick.specializationPicker()
    playerCombat.armorPicker()
    os.system('cls')

    roundCount = 1
    playerCombat.playerSurrenderDamageCheck = False

    while True: #While loop that starts with setting player HP to 100 and enemy to 25 times the round number, divided in half

        if playerCombat.playerHitpoints <= 0:
            break

        playerCombat.playerHitpoints = 100
        playerCombat.enemyHitpoints = 25 * (roundCount / 2)
        print(colorama.Fore.GREEN + "Round:", roundCount)
        playerCombat.enemyChoiceFunc()
        playerCombat.playerSurrender = False

        while True: #While loop to print enemy and player hp, combat for both player and enemy and a check at the end for if hp is below zero

            print("You have:", playerCombat.playerHitpoints, "HP left")
            print("Your opponent has:", playerCombat.enemyHitpoints, "HP left")

            playerCombat.PlayerCombat()
            if playerCombat.playerSurrender == True:
                    os.system('cls')
                    print("You surrendered.")
                    break       
            elif playerCombat.playerSurrenderDamageCheck == False:
                playerCombat.enemyCombat()
           
            input("Press enter to continue")
            os.system('cls')


            if playerCombat.playerHitpoints <= 0:

                print("As your enemy hits you, you fall to the ground.")
                time.sleep(1)
                print("The skies begin to blacken.")
                time.sleep(1)
                print("And you die.")
                time.sleep(2)
                print(colorama.Fore.RED + "Player HP hit zero! You lose!")
                print(colorama.Fore.YELLOW + "Round reached:", roundCount)
                break

            elif playerCombat.enemyHitpoints <= 0:
                print("You hit your opponent a final time, they proceed to fall.")
                time.sleep(1)
                print(colorama.Fore.GREEN + "Opponent HP hit zero! You win!")
                roundCount += 1
                break




elif modeSelect == 2: #Premade battles, with heavy inspiration from media I enjoy.
     
    print("Select your weapon")
    input("Enter to continue")
    os.system('cls')
    setMatchesCombat.weaponPickSetMatches()

    print("...")
    time.sleep(2)
    print("Something catches your attention.")
    time.sleep(1)
    print("It is a slightly damaged poster...")
    print("It reads the following:")
    print()
    time.sleep(1)
    print("LOOKING FOR FIGHTERS TO FIGHT IN THE ARENA")
    print("REWARD FOR FIGHTING IS GREAT! HONOUR AND GOLD! MOSTLY GOLD HOWEVER.")
    print("Are you interested? If so head to...")
    time.sleep(5)
    os.system('cls')

    print("You exit the building, having just joined the so-called 'arena' ")
    print("You were given a handful of images of the opponents you were fighting, aswell as having your own picture taken.")
    print()
    print("The first opponent is a humanoid cat named Alexios, they're mostly dark grey with some green markings on their head.")
    time.sleep(4)
    os.system('cls')

    print("A few days later . . .")
    time.sleep(3)
    os.system('cls')

    print("You step into the arena, seeing your opponent on the other side of it.")
    time.sleep(3)
    print("An announcer yells out for the fight to begin.")
    time.sleep(3)


    setMatchesCombat.playerHitpoints = 100
    setMatchesCombat.enemyHitpoints = 60
    while True:
        os.system('cls')
        print("You have:", setMatchesCombat.playerHitpoints, "HP Remaining!")
        print("Alexios has:", setMatchesCombat.enemyHitpoints, "HP Remaining!")
        print()

        if setMatchesCombat.playerHitpoints > 0 and setMatchesCombat.reloadTime == 0: # if playerHP is above 0 and reload 0 do combat.
            setMatchesCombat.playerSetCombat()
            input("Enter to continue")
        
        elif setMatchesCombat.playerHitpoints > 0 and setMatchesCombat.reloadTime > 0:
            print("You are reloading your", setMatchesCombat.chosenWeapon, "!")
            setMatchesCombat.reloadTime -= 1
            time.sleep(1)

        else: # If playerHP is not above 0, do death.
            print("You fall over, your eyes quicky darkening. The last thing you hear is the announcer calling out Alexios win.")
            time.sleep(3)
            print("You lose! Restart the game to try again.")
            time.sleep(86400) # To make the player restart the game, or wait 24 hours.
        

        if setMatchesCombat.enemyHitpoints > 0: # Same as above
            SetMatches.alexiosOmorfan()
            input("Enter to continue")

        else:
            print("Alexios falls over, and the announcer proclaims your victory")
            time.sleep(2)
            os.system('cls')
            break

    print("You head home, having killed someone and feeling barely any remorse because you have yet to process this fact.")
    time.sleep(2)
    print("You reluctantly head back to the arena the following week for the next fight.")
    time.sleep(2)
    print("Your opponent this time is ") # I've got no idea. I plan on having the final fight be basically just Ainz from Overlord.