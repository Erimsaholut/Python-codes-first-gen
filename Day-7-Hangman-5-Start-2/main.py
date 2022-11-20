#Step 5

import random
from hangman_art import stages , logo
from hangman_words import word_list
from replit import clear

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
used_letters = ""

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    
    if not guess in used_letters:
        used_letters += guess
        for position in range(word_length):
            letter = chosen_word[position]
            
            if letter == guess:
                display[position] = letter
    
        
        if guess not in chosen_word:
            print(f"The {guess} letter is not in word")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
        print(f"{' '.join(display)}")
    
        if "_" not in display:
            end_of_game = True
            print("You win.")
    
        print(stages[lives])
        print(f"Used letters {used_letters.split(' ')}")
    else:
        print(f"you already tryed {guess} .")
        print(f"{' '.join(display)}")
        print(stages[lives])
        print(f"Used letters {used_letters.split(' ')}")