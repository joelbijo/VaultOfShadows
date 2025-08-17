'''
This Python code simulates a dramatic interactive guessing game where 
the player tries to unlock a mythical ancient vault by guessing 
a secret number between 1 and 50 within 3 attempts. The game features 
atmospheric storytelling with curses and magical hints after incorrect guesses.
'''

import random as r
attempts = 3
def numberGuess():
    guess = r.randint(1,50)
    for i in range(attempts):
        secret = int(input(f"\nAttempt {i+1} of {attempts} - Enter your guess: "))
        if guess == secret:
            print("\n✨ With a regal thunder, the vault surrenders its secrets unto you.")
            print("The wealth of empires is yours, and your name shall be exalted in the annals of time.")
            break
        else:
            traps = [
            "Venomous snakes slither from the shadows, hissing at your foolishness.",
            "A volley of poisoned darts whizzes past your head, narrowly missing.",
            "An icy wind fills the chamber, sapping your strength..."
            ]
            print(f"⚠️ {traps[i]}")
        
            if guess < secret:
                print("🔮 A spirit whispers: 'Seek a greater number...'")
            else:
                print("🔮 A spirit whispers: 'The answer is smaller than your guess...'")

    else:
        print("\n💀 The vault slams shut! Shadows envelop you—cursed for all eternity...")
        print("You are doomed to rot in here for eternity and haunt the next adventurers...")
def main():
    print("\n\n\nA disembodied voice intones:")
    print("🏰 Welcome, brave adventurer!")
    print("You stand before a sealed ancient vault...")
    print("  'Only one who possesses both wisdom and luck will claim the ancient treasure.'")
    print("'Guess the secret key between 1 and 50.'")
    print("\nBut beware... you only have 3 chances!\n")
    numberGuess()

if __name__ == "__main__":
    main()  