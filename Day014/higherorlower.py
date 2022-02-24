from data import data
from art import logo, vs
import random
rnum2 = random.randint(0,49)

score = 0
while(True):
    print(logo)
    rnum1 = rnum2
    rnum2 = random.randint(0,49)
    if(score):
        print(f"You are right, Final score is {score}")
    print(f"Compare A:{data[rnum1]['name']}, a {data[rnum1]['description']}, from {data[rnum1]['country']}")
    print(vs)
    print(f"Compare B:{data[rnum2]['name']}, a {data[rnum2]['description']}, from {data[rnum2]['country']}")
    inp = input("Who has more followers A or B? Type A or B: ")
    if(data[rnum1]['follower_count']>data[rnum2]['follower_count'] and inp == 'A'):
        print('You won')
        score +=1
        #print(f'{data[rnum1]["follower_count"]} {data[rnum2]["follower_count"]}')
    elif(data[rnum1]['follower_count']<data[rnum2]['follower_count'] and inp == 'B'):
        print('You won')
        score +=1
        #print(f'{data[rnum1]["follower_count"]} {data[rnum2]["follower_count"]}')
    else:
        print(f"You are right, Final score is {score}")
        print('You lost')
        #print(f'{data[rnum1]["follower_count"]} {data[rnum2]["follower_count"]}')
        break