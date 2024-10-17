import random
import colorama
import time
import SpecializationPick

def basicEnemyCombat(): #sorry about the lack of comments, basic system is "pick an attack, do damage unless stunned"
    basicEnemyAttack = ["punch", "tackle", "grab", "counter"]
    basicEnemyHitPoints = 75
    playerHitPoints = 100
    stunCountPlayer = 0
    stunCountEnemy = 0
    print("The first match is a basic showcase / bad tutorial, would you like to skip it?")
    print("Yes [1] or No [2]")
    SkipOrNot = int(input())
    if SkipOrNot == 2:
        while True:
            print("You have:", playerHitPoints, "HP left!")
            print("Your opponent has", basicEnemyHitPoints, "HP left!")
            enemyChoice = random.choice(basicEnemyAttack)

            print("What do you attack with? a punch [1], tackle [2], grab [3] or do you counter? [4]")
            playerAttackChoice = int(input())

            #Player attacks here.
            if stunCountPlayer == 0:
                if playerAttackChoice == 3:
                    if enemyChoice == "grab":
                        print("You try to grab your opponent, but they counter!")
                        selfDamage = random.randint(10, 15)
                        print("Your opponent dealt", selfDamage, "damage towards you!")

                    elif stunCountEnemy == 0:
                        stunCountEnemy += 2
                        print("You grab your opponent and stun them for one turn!")

                    else:
                        print("Your opponent is already stunned!")

                elif playerAttackChoice == 2:
                    damageAgainstEnemy = random.randint(8, 20)
                    selfDamage = random.randint(10, 15)

                    print("You tackle your opponent and take", selfDamage, "damage whilst dealing", damageAgainstEnemy, "!")

                    playerHitPoints -= selfDamage
                    basicEnemyHitPoints -= damageAgainstEnemy

                    
                else:
                    damageAgainstEnemy = random.randint(5, 15)

                    print("You punch your opponent and deal", damageAgainstEnemy, "damage towards them!")

                    basicEnemyHitPoints -= damageAgainstEnemy
            else:
                print("You are stunned!")



            #Enemy attacks here.
            if stunCountEnemy == 0:
                if enemyChoice == "grab":
                    if playerAttackChoice == 4:
                        print("Your opponents tries to grab you, but you counter!")
                        damageAgainstEnemy = random.randint(10, 15)
                        print("You dealt", damageAgainstEnemy, "damage towards them!")
                        basicEnemyHitPoints -= damageAgainstEnemy


                    elif stunCountPlayer == 0:
                        stunCountPlayer += 2
                        print("Your opponent has grabbed you! You lose your next turn.")

                    else:
                        print("Your opponent has already stunned you!")

                elif enemyChoice == "tackle":
                    damageAgainstEnemy = random.randint(10, 15)
                    selfDamage = random.randint(8, 20)

                    print("Your opponent tackles you and takes", damageAgainstEnemy, "damage whilst dealing", selfDamage, "!")

                    playerHitPoints -= selfDamage
                    basicEnemyHitPoints -= damageAgainstEnemy

                else:
                    selfDamage = random.randint(5, 15)

                    print("Your opponent punches you and deals", selfDamage, "towards you!")

                    playerHitPoints -= selfDamage
            else:
                print("Your opponent is stunned!")

            if playerHitPoints and basicEnemyHitPoints > 0:
                if stunCountEnemy > 0:
                    stunCountEnemy -= 1
                if stunCountPlayer > 0:
                    stunCountPlayer -= 1

            elif playerHitPoints <= 0:
                print("Your HP dropped to zero and you died. Last thing you heard is the jubilations of the spectators.")
                break

            elif basicEnemyHitPoints <= 0:
                print("Your opponents HP dropped to zero, and they fall. The spectators applause and jubilations echo")
                print("throughout the arena, you have won your first battle.")
                break
    else:
        print("Skipped.")


def weaponry():
    tester = SpecializationPick.specializationPick
    if tester == 1:
        print("test successful")