import time
import colorama
import random
import playerCombat
import SpecializationPick
from colorama import init
import os

init(autoreset=True)

SpecializationPick.specializationPicker()
while True:
    playerCombat.PlayerCombat()
    time.sleep(2)
    os.system('cls')

# while weaponSystem.loopBreak == False:
#     weaponSystem.PlayerCombat()
