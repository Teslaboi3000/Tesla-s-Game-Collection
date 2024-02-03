import random

print("Welcome to my Rock Paper Scissors game!\nLet's play! If you want to exit just write 'exit'\n")

while True:
    player_choice = input('> ').lower()
    responses = ['Rock\n', 'Paper\n', 'Scissors\n']
    response = random.choice(responses)
    print(response)

    if player_choice == 'rock' and response == responses[0] or player_choice == 'paper' and response == responses[1] or player_choice == 'scissors' and response == responses[2]:
        print('Draw!\n')
    elif player_choice == 'rock' and response == responses[2] or player_choice == 'paper' and response == responses[0] or player_choice == 'scissors' and response == responses[1]:
        print('You Win!\n')
    elif player_choice == 'rock' and response == responses[1] or player_choice == 'paper' and response == responses[2] or player_choice == 'scissors' and response == responses[0]:
        print('You Lose!\n')
    elif player_choice == 'exit':
        exit()
    else:
        print("You can't do that!")
