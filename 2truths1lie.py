import random

print("Welcome to Tesla's Two Trurhs One Lie Game!\nYou can start writing your messages and ill guess what is the lie!\nYou will write 3 messages, let's start!")
while True:    
    message1 = input("Write here the first message: ")
    message2 = input("Second message: ")
    message3 = input("And the third message: ")
    messages = [message1, message2, message3]
    lie = random.choice(messages)
    is_lie_correct = input(f"I think the lie is {lie}. Am I correct? ").lower()
    if is_lie_correct == "yes":
        win_messages = ["Nice I got it!\n", "GG I guessed it!\n", "I'm so lucky! I got it!\n", "No way! I still can't believe it! I got it!\n", "If you lied I'm so angry with you! If not I got it nice\n"]
        print(random.choice(win_messages))
    elif is_lie_correct == "no":
        loose_messages = ["Damn, ill have more luck next time!", "OH I GOT I- oh I din't lol", "Crap I got it wrong, maybe next time"]
        print(random.choice(loose_messages))
    else:
        is_lie_correct = input("I din't understand, did I win? ").lower()
        if is_lie_correct == "yes":
            win_messages = ["Nice I got it!\n", "GG I guessed it!\n", "I'm so lucky! I got it!\n", "No way! I still can't believe it! I got it!\n", "If you lied I'm so angry with you! If not I got it nice\n"]
            print(random.choice(win_messages))
        elif is_lie_correct == "no":
            loose_messages = ["Damn, ill have more luck next time!\n", "OH I GOT I- oh I din't lol\n", "Crap I got it wrong, maybe next time\n"]
            print(random.choice(loose_messages))
    want_to_replay = input("Wanna play again? ")
    if want_to_replay == "yes":
        print("Ok, let's play again!")
    elif want_to_replay == "no":
        print("Oki, see you next time!")
        exit()
        