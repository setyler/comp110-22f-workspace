"""Exercise 2: One Shot Wordle"""
__author__ = "730946915"

secret_word: str = "python"
user_guess: str = input("What is your 6-letter guess?")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(user_guess) != 6:
    user_guess = input("That was not 6 letters! Try again.")

index_of_guess: int = 0
result_of_guess: str = ""

while index_of_guess < len(secret_word):
    if secret_word[index_of_guess] == user_guess[index_of_guess]:
        result_of_guess = f"{result_of_guess}{GREEN_BOX}" 
    elif secret_word[index_of_guess] != user_guess[index_of_guess]:
        character_exists = False
        alternate_index: int = 0
        while character_exists == False and alternate_index < len(secret_word):
            if secret_word[alternate_index] == user_guess[index_of_guess]:
                character_exists = True
            else: 
                alternate_index += 1 
        if character_exists == True:
            result_of_guess = f"{result_of_guess}{YELLOW_BOX}"
        else:
            result_of_guess = f"{result_of_guess}{WHITE_BOX}"
    index_of_guess = index_of_guess + 1 
print(result_of_guess)

if secret_word[0] == user_guess[0] and secret_word[1] == user_guess[1] and secret_word[2] == user_guess[2] and secret_word[3] == user_guess[3] and secret_word[4] == user_guess[4] and secret_word[5] == user_guess[5]:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")