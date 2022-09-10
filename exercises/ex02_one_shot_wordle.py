"""Exercise 2: One Shot Wordle."""
__author__ = "730496915"

secret_word: str = "python"
user_guess: str = input(f"What is your {str(len(secret_word))}-letter guess?")

WHITE_BOX: str = "\U00002B1C" 
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {str(len(secret_word))} letters! Try again.")

g: int = 0
result: str = ""

while g < 6 and secret_word != user_guess:
    i: int = 0
    while i < len(secret_word): 
        if secret_word[i] == user_guess[i]: 
            result = f"{result}{GREEN_BOX}"
        else: 
            character_exists: bool = False
            i_2: int = 0
            while i_2 < len(user_guess) and not character_exists:
                if user_guess[i] == secret_word[i_2]:
                    character_exists = True 
                i_2 += 1 
            if character_exists:
                result = f"{result}{YELLOW_BOX}"
            else:
                result = f"{result}{WHITE_BOX}"
        i += 1 
    print(result)
    user_guess = input(print(f"Not quite. Guess again!"))
    g += 1
print(result)
print("Woo! You got it!")