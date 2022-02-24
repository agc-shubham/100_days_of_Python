# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# e.g. 86 is even because 86 ÷ 2 = 43
# 43 does not have any decimal places. Therefore the division is clean.
# e.g. 59 is odd because 59 ÷ 2 = 29.5
# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
# e.g.
# 6 ÷ 2 = 3 with no remainder.
number = int(input("Which number do you want to check? "))
if(number%2==0):
    print("This is an even number.")
else:
    print("This is an odd number.")

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight/(height ** 2)
bmi = round(bmi,2)

if(bmi<18.5):
    print(f"Your BMI is {bmi}, you are underweight.")
elif(bmi<25):
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif(bmi<30):
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif(bmi<35):
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February.
year = int(input("Enter the year you want to check: "))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"{year} is a Leap year")
        else:
            print(f"{year} is not a Leap year")
    else:
        print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")

# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
size = input("Enter the size of the pizza you want to order: S, M, L ")
bill = 0
if(size=="S"):
    bill +=15
elif(size=="M"):
    bill +=20
elif(size=="L"):
    bill +=25
isPepperoni = input("Do you want Pepperroni: y or n ")
if(isPepperoni=="y"):
    if(size=="S"):
        bill += 2
    else:
        bill += 3
isCheese = input("Do you want cheese: y or n ")
if(isCheese=="y"):
    bill +=1
print(f"Your total bill is {bill}")

# You are going to write a program that tests the compatibility between two people. 
# We're going to use the super scientific method recommended by BuzzFeed.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# This video gives you more details on this:
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

# e.g.
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times R occurs 1 time U occurs 2 times E occurs 2 times
# Total = 5
# L occurs 1 time O occurs 0 times V occurs 0 times E occurs 2 times
# Total = 3
# Love Score = 53
# Print: "Your score is 53."

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lname1 = name1.lower()
lname2 = name2.lower()
first = lname1.count('t')+lname1.count('r')+lname1.count('u')+lname1.count('e')+lname2.count('t')+lname2.count('r')+lname2.count('u')+lname2.count('e')
second = lname1.count('l')+lname1.count('o')+lname1.count('v')+lname1.count('e')+lname2.count('l')+lname2.count('o')+lname2.count('v')+lname2.count('e')
snum = str(first)+str(second)
inum = int(snum)
if(inum<10 or inum>90 ):
    print(f"Your score is {inum}, you go together like coke and mentos.")
elif(inum>40 and inum<50):
    print(f"Your score is {inum}, you are alright together.")
else:
    print(f"Your score is {inum}.")