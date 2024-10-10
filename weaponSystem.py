import random
import colorama
import time

def basicEnemyCombat():
    basicEnemyAttack = ["punch", "tackle", "grab", "counter"]
    basicEnemyHitPoints = 75
    playerHitPoints = 100

    while True:
        print("You have:", playerHitPoints, "HP left!")
        print("Your opponent has", basicEnemyHitPoints, "HP left!")
        enemyChoice = random.choice(basicEnemyAttack)

        print("What do you attack with? a punch [1], tackle [2], grab [3] or do you counter? [4]")
        playerAttackChoice = int(input())

        if playerAttackChoice == 4 and enemyChoice == "grab": #TODO ADD A STUN MECHANIC
            print("You counter your opponent and no-one takes damage")
        
        #Player attacks here.
        if playerAttackChoice == 2:
            damageAgainstEnemy = random.randint(8, 20)
            selfDamage = random.randint(10, 15)

            print("You tackle your opponent and take", selfDamage, "damage whilst dealing", damageAgainstEnemy, "!")

            playerHitPoints -= selfDamage
            basicEnemyHitPoints -= damageAgainstEnemy

            
        else:
            damageAgainstEnemy = random.randint(5, 15)

            print("You punch your opponent and deal", damageAgainstEnemy, "damage towards them!")

            basicEnemyHitPoints -= damageAgainstEnemy



        #Enemy attacks here.
        if enemyChoice == "tackle":
            damageAgainstEnemy = random.randint(10, 15)
            selfDamage = random.randint(8, 20)

            print("Your opponent tackles you and takes", damageAgainstEnemy, "damage whilst dealing", selfDamage, "!")

            playerHitPoints -= selfDamage
            basicEnemyHitPoints -= damageAgainstEnemy

        else:
            selfDamage = random.randint(5, 15)

            print("Your opponent punches you and deals", selfDamage, "towards you!")

            playerHitPoints -= selfDamage