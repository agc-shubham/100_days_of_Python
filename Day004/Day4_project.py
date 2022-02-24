# Write a program to play rock, Paper, Scissors with computer
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
cChoice = random.randint(0,2)
choices = [rock,paper,scissors]
names = ["Rock","Paper","Scissors"]
ip = input("What do you choose, enter 0 for rock, 1 for paper, 2 for scissors: ")
ip = int(ip)
print(f"You Choose {names[ip]}\n{choices[ip]}")
print(f"Computer Choose {names[cChoice]}\n{choices[cChoice]}")
if(cChoice==0 ):
    if(ip==0):
        print("Draw")
    if(ip==1):
        print("You win")
    if(ip==2):
        print("You Lose")
if(cChoice==1):
    if(ip==0):
        print("You Lose")
    if(ip==1):
        print("Draw")
    if(ip==2):
        print("You Win")
if(cChoice==2 ):
    if(ip==0):
        print("You Win")
    if(ip==1):
        print("You Lose")
    if(ip==2):
        print("Draw")

