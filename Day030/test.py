# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
    # raise TypeError("This is an error that I made up.")

#BMI Example

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]

# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#       fruit = fruits[index]
#       print(fruit + " pie")
#     except IndexError:
#       print("fruit" + " pie")
#     else:
#       print(fruit + " pie")

# make_pie(4)