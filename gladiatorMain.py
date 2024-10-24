import time
import colorama
import random
import playerCombat
import SpecializationPick
from colorama import init
import os

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
modeSelect = int(input())

os.system('cls')

playerCombat.difficultySelect()

os.system('cls')


if modeSelect == 1: #Endless mode.
    
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