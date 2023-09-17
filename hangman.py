import random
while True:
    print("Welcome to my hangman!\nLet's play!\n")
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
    lives = 5
    print(f'{len(word_to_guess)} letters')
    guess = input('> ')
    if guess == word_to_guess:
        print("You got it! GG, let's change word!\n")
    else:
        lives -= 1
        print(f"Sorry to say but Wrong! You still have {lives} lives\n")