import random
import colorama
import time

playerHitPoints = 100

basicEnemyAttack = ["punch", "kick", "tackle", "grab", "counter"]

def basicEnemyCombat():
    basicEnemyHitPoints = 75
    while playerHitPoints > 0 and basicEnemyHitPoints > 0:

        enemyChoice = random.choice(basicEnemyAttack)

        print("What do you attack with? a punch [1], kick [2], tackle [3], grab [4] or do you counter? [5]")
        playerAttackChoice = int(input())

    