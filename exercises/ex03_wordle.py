"""Wordle!"""
__author__ = "730496915"


def contains_char(string: str, character: str) -> bool:
    """Searches secret word for character and reuturns boolean."""
    assert len(character) == 1 
    i_1 = 0
    # possible future edit: use just i for every function because they are each in own frame and not in globals. by the time I relized this I was in too deep.
    while i_1 < len(string):
        if str(string[i_1]) == str(character):
            return True 
        i_1 += 1 
    return False 


def emojified(guess: str, secret_word: str) -> str:
    """Compares secret word to user guess and returns emoji boxes."""
    assert len(guess) == len(secret_word)
    i_2 = 0 
    result: str = ""
    WHITE_BOX: str = "\U00002B1C" 
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # print out emojis 
    while i_2 < len(secret_word): 
        # using len function to account for any secret word used
        if str(secret_word[i_2]) == str(guess[i_2]): 
            result += f"{GREEN_BOX}"
            # correct letter leads to concatenating green box emoji 
        else:
            if contains_char(secret_word, str(guess[i_2])):
                result += f"{YELLOW_BOX}"
                # letter is in secret word but not in the some place as in the guessed word 
            else:
                result += f"{WHITE_BOX}"
                # letter guessed is incorrect 
        i_2 += 1 
    return result


def input_guess(expected_length: int) -> str:
    """Handles getting a valid guess from user."""
    user_guess: str = input(f"Enter a {expected_length} character word:")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again:")
    return user_guess 
    # this function is solely used to account for user error 


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    secret_word: str = "codes"
    # can be changed to any word of any length 
    user_guess: str = ""
    i_game: int = 1
    # starting at 1 so the first game index isn't equal to 0 
    game_won: bool = False
    # i originally though i also needed to define a variable for secret length here but that is all taken care of in the input_guess function 
    while i_game < 7 and not game_won:
        print(f"=== Turn {i_game}/6 ===")
        user_guess = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            game_won = True 
        else:
            i_game += 1 
    if game_won:
        print(f"You won in {i_game}/6 turns!")
        # final value of i_game is total number of games played 
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
# extra code that we do not yet understand 
# but are grateful for because it makes playing the game easier 


# current autograder isdues:
# --game not winnable with secret "codes"
# --game not winnable after multiple guesses