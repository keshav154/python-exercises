# GAME OF SNAKE WATER AND GUN
# User pley with computer and if condition satisfy he wins the game

import random
options = ["1", "2", "3"]
tries = int(input('How many times you want to play?'))
if tries < 1:
    print('Enter valid input')
else:
    compchoice = 0
    userchoice = 0
    i = 0
    w = 0
    l = 0
    while i < tries:
        userchoice = int(input('Choose between snake(1), water(2) or gun(3)'))
        compchoice = int(random.choice(options))
        if (userchoice == 1 and compchoice == 1) or (userchoice == 2 and compchoice == 2) or (userchoice == 3 and compchoice == 3):
            print('Its a tie')
        elif (userchoice == 1 and compchoice == 2) or (userchoice == 2 and compchoice == 3) or (userchoice == 3 and compchoice == 1):
            print('You win')
            w = w + 1
        elif (userchoice == 1 and compchoice == 3) or (userchoice == 2 and compchoice == 1) or (userchoice == 3 and compchoice == 1) or (userchoice == 3 and compchoice == 2):
            print('You loose')
            l = l + 1
        i = i + 1
        print('You have chances left = ', tries-i)
    if w > l:
        print('You win by points = ', w-l)
    else:
        print('You loose by points = ', l-w)
