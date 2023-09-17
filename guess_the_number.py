import random

number = random.randint(0, 100)

print('Welcome to my number guessing game! You can start!\n')

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
    except ValueError:
        print("I'm pretty sure that isn't the number dude")