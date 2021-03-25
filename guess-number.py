# Ask user to guess a number having 9 attempts left 

n = 18
attempts = 0
while attempts <=9:
    inp = int(input("Enter your guess"))
    if inp > n:
        print("your guess is greater than the number")
    elif inp < n:
        print("your guess is less than the number")
    elif inp == n:
        print("your guess is correct and nummber is", n)
        break
    print(9-attempts, "number of guesses left")
    attempts = attempts + 1
if(attempts > 9):
    print("game over man")
