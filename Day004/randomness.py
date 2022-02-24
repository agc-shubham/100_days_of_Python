# we are going to write a virtual coin toss program. 
# It will randomly tell the user "Heads" or "Tails".
# Seed is to be provided by user
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

bin = random.randint(0,1)

print(bin)
if(bin==0):
    print("Tails.")
else:
    print("Heads.")