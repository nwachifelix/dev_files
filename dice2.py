from random import randint


diceinput = input()
diceroll = randint(1,6)

while diceroll == 6:
    print('Move to the  next stage. ')
if diceroll == 2:
        print('Roll again. ')
if diceroll == 3:
    print('Roll again. ')
if diceroll == 4:
    print('Roll again. ')
if diceroll == 5:
    print('Roll again. ')
if diceroll == 1:
    print('Drop the dice. ')
    
