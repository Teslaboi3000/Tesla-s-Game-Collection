import random

words = [
    "cat",
    "dog",
    "hat",
    "rug",
    "ball",
    "car",
    "sun",
    "moon",
    "tree",
    "house",
    "bird",
    "fish",
    "table",
    "chair",
    "book",
    "window",
    "door",
    "flower",
    "apple",
    "banana",
    "orange",
    "milk",
    "water",
    "bread",
    "elephant",
    "giraffe",
    "hippopotamus",
    "rhinoceros",
    "lion",
    "tiger",
    "zebra",
    "kangaroo",
    "koala",
    "crocodile",
    "alligator",
    "snake",
    "computer",
    "telephone",
    "television",
    "airplane",
    "train",
    "boat",
    "bus",
    "robot",
    "dinosaur",
    "pizza",
    "ice cream",
    "chocolate",
]

word_to_guess = random.choice(words)
revealed_word = [word_to_guess[0]] + ["_"] * (len(word_to_guess) - 2) + [word_to_guess[-1]]
lives = 5

print("Welcome to my Hangman game! Write exit to stop playing.\nLet's play!\n")

while True: 
    print(f'{len(word_to_guess)} letters')
    print(f"The word so far is {''.join(revealed_word)}\n")
    guess = input('> ')
    if guess == word_to_guess:
        print("You got it! GG, let's change word!\n")
        word_to_guess = random.choice(words)
        revealed_word = [word_to_guess[0]] + ["_"] * (len(word_to_guess) - 2) + [word_to_guess[-1]]
        lives = 5
    elif guess == 'exit':
        exit()
    else:
        lives -= 1
        if lives > 0:
            for i in range(1, len(word_to_guess) - 1):
                if revealed_word[i] == "_":
                    revealed_word[i] = word_to_guess[i]
                    break
            print(f"Sorry to say but Wrong! You still have {lives} lives\n")
        else:
            print("Game over! You've run out of lives.\n")
            break
