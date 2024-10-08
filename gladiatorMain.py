import time
import colorama
import random
import weaponSystem #This module contains all the gear and calculations for the gear. including player HP

#TODO: Main combat system (attack, defend, player vs "npc")
#Lower priority TODO: Menu system (This file should contain menu system), colours, weather.

# enemyNameList = ["Greek Name", "Roman Name"]
# basicEnemyName = random.choice(enemyNameList)
# print(basicEnemyName)

print("Welcome to [Gladiator Game]! You are a gladiator. However, you have forgotten how you became one. ")
print("Your goal is to defeat as many enemies as you can, Unfortunately there is no end until you lose.")

weaponSystem.basicEnemyCombat()