# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")

first = int(two_digit_number[0])
second = int(two_digit_number[1])

print("your desired sum is: "+str(first+second))

# Write a program that calculates the Body Mass Index (BMI) 
# from a user's weight and height.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight/(height ** 2))

print("Your BMI is: " + str(bmi))

# Create a program using maths and f-Strings that tells us how many days, weeks,
# months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
age = input("Enter your age in years: ")
years_left = 90 - int(age)
days = years_left*365
weeks = years_left*52
months = years_left*12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")