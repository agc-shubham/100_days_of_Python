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

dir1 = input("Do you want to go to: left or right: ")
dir1 = dir1.lower()
if(dir1=="right"):
    print("You fell into hole. Game over")
elif(dir1=="left"):
    print("You Survived")
    que1 = input("Do you want to: swim or wait: ")
    que1 = que1.lower()
    if(que1=="swim"):
        print("You were attacked by trout. Game over")
    elif(que1=="wait"):
        print("You Survived. You safely reached to an Island. There are three doors infront of you: Red, Yellow, Green")
        door = input("which door do you choose: ")
        door = door.lower()
        if(door=="red"):
            print("Burned by fire. Game over")
        elif(door=="yellow"):
            print("You Survived. You win ")
        elif(door=="green"):
            print("Eaten by Beasts. Game over")
        else:
            print("Game over")
