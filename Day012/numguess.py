import random
number =  random.randint(1,100)
level = input("Enter the level of game Hard or simple: ")
chance = 0
if level == 'hard':
    chance = 5
elif level == 'simple':
    chance = 10
print(chance)
while chance!=0:
    guess_number = int(input("Guess a number: "))
    if guess_number < number:
        print("Too Low, Choose a greater number")
    elif guess_number > number:
        print("Too High, Choose a lower number")
    else:
        print("You Won")
        print("Guessed number is equal to choosen number")
        break
    chance -=1
    print(f"Available number of choices: {chance}")
    