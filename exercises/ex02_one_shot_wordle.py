"""Exercise 2: One Shot Wordle."""
__author__ = "730496915"

secret_word: str = "python"
# default word for autograder. can be changed and pragrom will work the same.
user_guess: str = input(f"What is your {str(len(secret_word))}-letter guess?")
# adjusts to number of letters in the secret word. 

WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# emojis!!

while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {str(len(secret_word))} letters! Try again.")
# prevents early termination for invalid guesses.

i: int = 0 
result: str = "" 
# defining variables 

while i < len(secret_word): 
    # < instead of <= because index starts at 0. 
    if secret_word[i] == user_guess[i]: 
        result = f"{result}{GREEN_BOX}"
        # if the guess is right everything in the following else block gets skipped.
    else: 
        character_exists: bool = False
        i_2: int = 0
        # these have to be inside of this code block so they get reset every time around. 
        while i_2 < len(user_guess) and not character_exists:
            if user_guess[i] == secret_word[i_2]:
                character_exists = True 
            i_2 += 1 
            # this loop repeats until the guess is matched to every letter in the secret word OR a match is found. Only one/the first match is needed to turn the emoji yellow. 
        if character_exists:
            result = f"{result}{YELLOW_BOX}"
        else:
            result = f"{result}{WHITE_BOX}"
        # after exiting the while loop these conditions get tested and the result of the guessed letter (yellow or white) is added to the final output/result.
    i += 1 
    # moving on to the next letter in the guess and starting from the top. 

print(result)
# code is finished running! 6 emoji squares print.

if secret_word == user_guess: 
    print("Woo! You got it!") 
else:
    print("Not quite. Play again soon!")
# could edit to request another input and run the whole thing again until the guess is correct or until 6 guesses have been made to be more similar to Wordle.