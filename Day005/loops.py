# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
student_heights = input("Input a list of student heights ").split(",")
sum = 0
count = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  count += 1
  sum += student_heights[n]
Avg = round(sum/count)
print(sum)
print(count)
print(f"Average Height of the class = {Avg} ") 

# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# The highest score in the class is: x

student_scores = input("Input a list of student scores ").split(",")
max = 0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if(student_scores[n]>max):
      max = student_scores[n]
print(student_scores)
print(f"The highest score in the class is: {max} ")

# You are going to write a program that calculates the sum of all the 
# even numbers from 1 to 100, including 1 and 100.
# e.g. 2 + 4 + 6 + 8 +10 ... + 98 + 100
sum = 0
for i in range(0,101,2):
    sum +=i
print(f"Sum of even numbers from 1 to 100: {sum}")     

# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
for i in range(1,100):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0 ):
        print("Fizz")
    else:
        print(i)