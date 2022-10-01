"""A number guessing game."""
__author__ = "730496915"


points: int = 0


def main() -> None:
    """Main function for program."""
    THEE_NUMBER: int = 0
    user: str = ""
    greetings() 
    enter_game: int = 1
#    enter_game = input(f"To play the game, enter 1. To exit the game, enter 0.")
    while enter_game == 1:
        game_loop()
        enter_game = int(input(f"To play again, enter 1. To exit the game, enter 0."))
    game_over()


def greetings() -> None:
    """Retrieves username and explains rules."""
    global user 
    user = input(f"Enter your name to get started:")
    print(f"Welcome to the Number Game, {user}!")
    print("Game rules are simple. You are trying to guess a secret number between 1 and 100.")
    print("Game points track how many times you have guessed.")
    print("You can play an umlimited number of times. Good luck!")
    return None


def game_loop() -> None: 
    """Main game loop. One time through = one game played."""
    global THEE_NUMBER 
    global points 
    from random import randint
    THEE_NUMBER = randint(1, 100)
    guess: int = 0
    game_over: bool = False
    guess = int(input("I'm thinking of a number between 1 and 100. Enter your first guess."))
    while game_over == False:
        if test_guess(guess, THEE_NUMBER) == True:
            game_over = True
        if test_guess(guess, THEE_NUMBER) == False:
            if guess > THEE_NUMBER: 
                guess = int(input("You guessed too high! Guess again."))
            if guess < THEE_NUMBER: 
                guess = int(input("You guessed too low! Guess again."))
        points += 1
    if game_over == True: 
        print(f"Great Job, {user}! You now have {points} points.")
        return None

    
def test_guess(guess: int, correct: int) -> bool: 
    """Determines whether guess is correct."""
    if guess == correct:
        return True
    else:
        return False 


def game_over() -> None:
    """Print game over message."""
    global points 
    print(f"Thanks for playing, {user}! You scored {points}.")


if __name__ == "__main__":
    main()