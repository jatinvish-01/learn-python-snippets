# Create a random number      

import random 

num = random.randint(1, 21)

tries = 0

while True:
      guess = int(input("Enter your guess btw 1 - 20: "))

      if num == guess:
            tries +=1
            print(f"You Won.. you guessed the number {tries} tries")
            break

      elif num < guess:
            print("Go a litle lower")
            tries +=1

      elif num > guess:
            print("Go a litle higher")
            tries +=1

      else:
            tries +=1
            print("You Loos..!!") 
