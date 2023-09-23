import random

number = random.randint(0, 100)

print('Welcome to my number guessing game! You win when you get to 50 points You can start!\n')
points = 0

while True:
    try:  
        player_input = int(input('> '))
        if player_input < number:
            print('More\n')
        elif player_input > number:
            print('Less\n')
        else:
            print("You guessed! Let's change number!\n")
            number = random.randint(0, 100)
            points += 1 
            if points == 1:
                print(f"You get a point! You now are at {points} point!")
            else:
                print(f"You get a point! You now are at {points} points!")
    except ValueError:
        print("I'm pretty sure that isn't the number dude")

    if points == 50:
        print("GG, You win! See you next time!")