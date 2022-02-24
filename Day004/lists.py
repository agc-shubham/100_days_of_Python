# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma: ")
names = namesAsCSV.split(", ")
length = len(names)
rand_index = random.randint(0,(length-1))
print(f"{names[rand_index]} will pay the bill.")

# You are going to write a program which will mark a spot with an X.

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
row = int(position[0])
coloumn = int(position[1])
map[row][coloumn] = "X"
print(f"{row1}\n{row2}\n{row3}")