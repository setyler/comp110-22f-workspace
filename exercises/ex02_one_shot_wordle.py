"""Exercise 2: One Shot Wordle."""
__author__ = "730946915"

secret_word: str = "python"
# can be changed to any word 
user_guess: str = input(f"What is your {str(len(secret_word))} -letter guess?")

WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# emojis!!

while len(str(user_guess)) != len(str(secret_word)):
    user_guess = input(f"That was not {str(len(secret_word))} letters! Try again.")
# accounting for guesses that don't work with the program 

index_of_guess: int = 0
result_of_guess: str = ""

while index_of_guess < len(str(secret_word)):
    if secret_word[index_of_guess] == user_guess[index_of_guess]: 
        result_of_guess = f"{result_of_guess}{GREEN_BOX}" 
    else:  # somewhat more consice with else as opposed to elif 
        character_exists = False 
        alternate_index: int = 0  # setting up test condition (lines 24 & 25)
        while character_exists == False and alternate_index <= len(secret_word):  # testing the test conditions to start the loop 
            if secret_word[alternate_index] == user_guess[index_of_guess]: 
                character_exists = True  # will produce a yellow box after the loop completes. only one (the first) case of a character existing will be found and used to change the output to a yellow box 
            else: 
                alternate_index += 1  # loop repeats for the next character if no match has been found 
        if character_exists == True:
            result_of_guess = f"{result_of_guess}{YELLOW_BOX}"
        else:
            result_of_guess = f"{result_of_guess}{WHITE_BOX}"  # occurs after every character has been checked and no matches found to produce a white box 
    index_of_guess = index_of_guess + 1  # original while loop restarts and program moves to next letter in guess 
print(result_of_guess)

if secret_word == user_guess: 
    print("Woo! You got it!") 
else:
    print("Not quite. Play again soon!")  # instead of try again soon I could replace this with an input box and terminate after a certain number of tries to more closely duplicate actual wordle