"""Wordle!!!"""
__author__ = "730496915"

def contains_char(string: str, character: str) -> bool:
    """Searches secret word for character and reuturns boolean"""
    assert len(character) == 1 
    i_1 = 0
    while i_1 < len(string):
        if str(string[i_1]) == str(character):
            return True 
        i_1 += 1 
    return False 

def emojified(guess: str, secret_word: str) -> str:
    "Compares secret word to user guess and returns emoji boxes."
    assert len(guess) == len(secret_word)
    i_2 = 0 
    result: str = ""
    WHITE_BOX: str = "\U00002B1C" 
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while i_2 < len(secret_word): 
        if str(secret_word[i_2]) == str(guess[i_2]): 
            result += f"{GREEN_BOX}"
        else:
            if contains_char(secret_word, str(guess[i_2])):
                result += f"{YELLOW_BOX}"
            else:
                result += f"{WHITE_BOX}"
        i_2 += 1 
    return result

def input_guess(expected_length: int) -> str:
    user_guess: str = input(f"Enter a {expected_length} character word:")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again:")
    return user_guess 

def main() -> None:
    """The entrypoin of the program and the main game loop."""
    secret_word: str = "codes"
    user_guess: str = ""
    secret_length: int = len(secret_word)
    i_game: int = 1
    game_won: bool = False 
    while i_game < 7 and game_won == False:
        print(f"=== Turn {i_game}/6 ===")
        user_guess = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            game_won = True 
        i_game += 1 
    if game_won == True:
        print(f"You won in {i_game}/6 turns!")
    else:
        print(f"X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()