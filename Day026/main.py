''' 
# List comprehension
# Standard Format
# [new_item for item in list]

num = [1,2,3,4,5,6]

new_num = [n+1 for n in num]
print(new_num)

new_list = [2*n for n in range(1,6)]
print(new_list)

# Addition of conditionals
# [new_item for item in list if condition]
names = ['shubham','riya','annasha','shiv','sonu','shivansh']
new_names =  [name for name in names if len(name)>4]
print(new_names)

'''

# Excercise 1 creating square nums
'''
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
squared_numbers = [num*num for num in numbers]


#Write your code 👆 above:

print(squared_numbers)
'''
#Excercise 2 filtering even numbers

'''
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [num for num in numbers if num %2 == 0 ]

#Write your code 👆 above:

print(result)

'''

#Excercise 3 filtering even numbers
'''
list1 = []
list2 = []
with open('file1.txt','r') as f1:
    list1 =  f1.readlines()
    list1 = [int(num) for num in list1 ]
with open('file2.txt','r') as f2:
    list2 =  f2.readlines()
    list2 = [int(num) for num in list2 ]

common_list = []
print(list1)
print(list2)
common_list = [num for num in list1 if num in list2]
print(common_list)

'''
# Dictionary Comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
'''
import random
names = ['shubham','riya','annasha','shiv','sonu','shivansh']
student_scores = {name:random.randint(10,100) for name in names} 
passed_students = {name:score for (name,score) in student_scores.items() if score>34}
print(passed_students)
'''

#Excercise 4 counting the length of words
'''
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split(" ")
dict = {word:len(word) for word in words}
print(dict)

'''
#Excercise 5 converting a dictionary of celsius scale to farenheit scale

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day:temp*9/5 + 32 for (day,temp) in weather_c.items()}


print(weather_f)