# Guess Numbers!
import random
print("Welcome to Guess Numbers!\nIf you don't know how to play don't worry the game is simple.\nJust write your guess for the number.Its will be between 1 and 100\nGood luck!")

number = random.randint(1,99)
hak = int(input("How many guess you want? (1 [if you believe yourself ;D ] /5/10...)"))
guess = hak
times = 0

while guess > 0:

    guess -= 1
    times += 1
    guess_it = int(input("Write your guess: "))

    if guess_it == number:
        print(f"(✯◡✯) 𓃚 Congratulations you guessed it in the your {times}. guess! Your point is: {100 - (100/hak) * (times - 1) } out of 100 𓃚 (✯◡✯)")
        break
    elif guess_it > number:
        print("Down ")
    else:
        print("Up ")

    if guess == 0:
        print(f"(⁎˃ᆺ˂) Game Over, You Lose!  The number was: {number}  Try again! (⁎˃ᆺ˂)")
        break

