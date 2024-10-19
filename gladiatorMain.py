import time
import colorama
import random
import playerCombat
import SpecializationPick
from colorama import init
import os

init(autoreset=True)

os.system('cls')

playerCombat.difficultySelect()

playerCombat.enemyChoiceFunc()
SpecializationPick.specializationPicker()

playerCombat.playerHitpoints = 100
playerCombat.enemyHitpoints = 100

while True:
    print("Player HP:", playerCombat.playerHitpoints)
    print("Enemy HP:", playerCombat.enemyHitpoints)
    playerCombat.PlayerCombat()
    playerCombat.enemyCombat()
    input("Enter to continue")
    os.system('cls')