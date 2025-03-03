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
print("🏴‍☠️ Welcome, Captain Sparrow! Your mission is to find the legendary Black Pearl's hidden treasure! 🏝️\n")

choice1 = input("You're sailing the high seas when you reach a fork in the ocean. Do you go 'left' or 'right'? 🏴‍☠️\n").lower()

if choice1 == "left":
    choice2 = input("\nYou spot a mysterious island ahead. Do you 'swim' to shore or 'wait' for a rowboat? 🌊\n").lower()

    if choice2 == "wait":
        choice3 = input("\nYou safely reach the island and find an ancient cave with three doors. Which do you enter: 'red', 'blue', or 'yellow'? 🚪\n").lower()

        if choice3 == "yellow":
            print("\n🏆 Congratulations, Captain! You found the legendary treasure of the Black Pearl! 🎉💰")
        elif choice3 == "red":
            print("\n🔥 Oh no! The cave erupts in flames! You've been burned alive! ☠️ Game Over!")
        elif choice3 == "blue":
            print("\n🦑 A giant sea beast awaits inside! You're devoured instantly! ☠️ Game Over!")
        else:
            print("\n⚰️ The cave crumbles, trapping you forever in darkness! ☠️ Game Over!")

    else:
        print("\n🐊 You were attacked by sea monsters and dragged to the depths! ☠️ Game Over!")

else:
    print("\n🕳️ Your ship falls into a whirlpool and is lost forever! ☠️ Game Over!")

