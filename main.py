

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    "your at a crossroad. Where do you want to go? 'left' or 'right' ")
if choice1 == 'left':
    print("You're come to a lake. There is an island in the middle of the lake")
    choice2 = input("Type 'wait' to wait for a boat or 'swim' ")
    if choice2 == 'wait':
        print("You arrive at the island unharmed.")
        choice3 = input(
            "There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if choice3 == "red":
            print("Burned by fire. Game over")
        elif choice3 == "yellow":
            print("You win, you find treasure!")
        elif choice3 == "blue":
            print("Eaten by beast. Game over")
        else:
            print("Game over")
    else:
        print("Attacked by trout. Game over")
else:
    print("You fell into a hole. Game over.")
