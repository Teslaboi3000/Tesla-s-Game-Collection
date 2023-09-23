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
print("Welcome to my hangman!\nLet's play!\n")
while True: 
    lives = 5
    first_letter = word_to_guess[0]
    last_letter = word_to_guess[-1]
    print(f'{len(word_to_guess)} letters')
    print(f"The first letter of the word is {first_letter} and the last letter is {last_letter}\n")
    guess = input('> ')
    if guess == word_to_guess:
        print("You got it! GG, let's change word!\n")
        word_to_guess = random.choice(words)
    else:
        lives -= 1
        print(f"Sorry to say but Wrong! You still have {lives} lives\n")