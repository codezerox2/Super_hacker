############ Create a number guessing game
import random 

number = random.randint(1, 10)

while True:
    guess = int(input("type your guess 1 -->10 :"))
    if number == guess:
        print("congratulations!!")
        break
    else:
        print("wrong guess")

# ===================== without random

number = 3

while True:
    guess = int(input("type your guess 1 -->10 :"))
    if number == guess:
        print("congratulations!!")
        break
    else:
        print("wrong guess")