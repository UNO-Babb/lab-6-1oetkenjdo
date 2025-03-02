#DiceRoll.py
#Name: Jacob Oetken
#Date: 03/02/2025
#Assignment: LAB 6


import random

def main():
  #Create an empty list with possible roll values
    rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
    for r in range(100):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        rolls[dice1 - 1] = rolls[dice1 - 1] + 1
        rolls[dice2 - 1] = rolls[dice2 - 1] + 1

  #find the sum total of the two dice
        total = dice1 + dice2
        rolls[total - 1] = rolls[total - 1] + 1
  #print statictics for dice rolls
    dice = 1
    for count in rolls:
        print(dice, ":", count)
        dice = dice + 1

if __name__ == '__main__':
  main()