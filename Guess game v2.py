from random import randint
x = randint(1, 10)
print("Welcome")
input ("Hit Enter to start")
print("The secret number is X (",x,")")
g = 0
while g != x:
    g = int (input ("Guess number 1-10: "))
    if g == x:
        print("You win!")
    else:
        if g < x:
            print("Too low")
        else:
            print("Too high")
print("GameOver")
