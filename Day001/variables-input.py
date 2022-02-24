   #printing to console
#print the following statements
#Day 1 - Python Print Function
#The function is declared like this:
#print('what to print')
#code
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#debug these statements
# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")


print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.\nlike this")

# Write a program that prints the number of characters in a user's name.
# You might need to Google for a function that calculates the length of a string.
name = input("what is your name? \n")
print("Length of charaacters in your name = "+str(len(name)))

# Write a program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")
swap = a
a = b
b = swap
print("a: " + a)
print("b: " + b)