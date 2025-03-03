import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to the game!")
choice_list =[rock,paper,scissors]
user_choice=int(input("Please choose one of the following options: 0 for rock,1 for paper or 2 for scissors\n"))
print("Your choice:",choice_list[user_choice])
comp_choice = random.randint(0,2)
print("Computer choice:",choice_list[comp_choice])

if user_choice>=3 or user_choice<0:
    print("Invalid choice, please choose one of the following options: 0,1 or 2")
elif  user_choice==comp_choice:
    print("It's a tie!")

elif  (user_choice==0 and comp_choice==1)or(user_choice==1 and comp_choice==2)or(user_choice==2 and comp_choice==0):
    print("You Lost!")
elif  (user_choice==0 and comp_choice==3)or(user_choice==1 and comp_choice==0) or(user_choice==2 and comp_choice==1):
    print("You Win!")
print("GAME OVER!")

          
