# Prime numbers are numbers that can only be cleanly divided by itself and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
import math
def prime_checker(number):
    c = 0
    root = math.sqrt(number)
    for i in range(2,int(root+1)):
        if(number%i==0):
            c+=1
    if(c!=0):
        print(f"{number} isn't a prime number")
    else:
        print(f"{number} is a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)