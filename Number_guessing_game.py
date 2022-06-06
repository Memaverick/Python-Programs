'''Guessing games'''
import random
number = random.randrange(1,10)
player_name = input("Hello! What's your name?")
num_of_gusses = 0
print("Hello", player_name,"!", "I am guessing a number between 1 to 10")

while num_of_gusses < 5:
    guess = int(input())
    num_of_gusses += 1
    if guess < number:
        print("OOPS! You guessed a lower number")
    if guess > number:
        print("OOPS! You guessed a higher number")
    if guess == number:
        break
if guess == number:
    print("YAY! You guessed the right one")
else:
    print("Oh No! You didn't guessed the number")
    print("The number is",str(number))
