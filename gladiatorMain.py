import time
import colorama
import random
import weaponSystem #This module contains all the gear and calculations for the gear. including player HP
import SpecializationPick

#TODO: Main combat system (attack, defend, player vs "npc")
#Lower priority TODO: Menu system (This file should contain menu system), colours, weather.

# enemyNameList = ["Greek Name", "Roman Name"]
# basicEnemyName = random.choice(enemyNameList)
# print(basicEnemyName)

print("Welcome to [Gladiator Game]! You are a gladiator. However, you have forgotten how you became one. ")
print("Your goal is to defeat as many enemies as you can, Unfortunately there is no end until you lose. \n You regain full HP each match.")
print()

time.sleep(3)
print("You get told about your first opponent, you are told he is just slightly weaker than you.")
print("You are both very similar and garaunteed to hit eachother when fighting. The first match is a fight to the death.")
time.sleep(3)

weaponSystem.basicEnemyCombat()

time.sleep(1.5)
print("Congrats on winning the first match.")

time.sleep(1)
print("Next you will choose your weapon specialisation. The weapon you specialise in will increase stats")
SpecializationPick.specializationPick()
weaponSystem.weaponry()