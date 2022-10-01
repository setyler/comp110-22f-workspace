"""A number guessing game."""
__author__ = "730496915"


points: int = 0
player: str = ""
THEE_NUMBER: int = 0 
user: str = ""


def main() -> None:
    """Main function for program."""
    greet() 
    enter_game: int = 1
    while enter_game == 1:
        game_loop()
        enter_game = int(input("To play again, enter 1. To exit the game, enter 0."))
    game_over()


def greet() -> None:
    """Retrieves username and explains rules."""
    global player 
    player = input(f"Enter your name to get started:")
    print(f"Welcome to the Number Game, {player}!")
    print("Game rules are simple. You are trying to guess a secret number between 1 and 100.")
    print("Game points track how many times you have guessed.")
    print("You can play an umlimited number of times. Good luck!")


def game_loop() -> None: 
    """Main game loop. One time through = one game played."""
    global points 
    from random import randint
    THEE_NUMBER = randint(1, 100)
    guess: int = 0
    game: bool = False
    guess = int(input("I'm thinking of a number between 1 and 100. Enter your first guess."))
    while game:
        if test_guess(guess, THEE_NUMBER):
            game = False
        if not test_guess(guess, THEE_NUMBER):
            if guess > THEE_NUMBER: 
                guess = int(input("You guessed too high! Guess again."))
            if guess < THEE_NUMBER: 
                guess = int(input("You guessed too low! Guess again."))
        points += 1
    if game_over: 
        print(f"Great Job, {player}! You now have {points} points.")

    
def test_guess(guess: int, correct: int) -> bool: 
    """Determines whether guess is correct."""
    if guess == correct:
        return True
    else:
        return False 


def game_over() -> None:
    """Print game over message."""
    global points 
    print(f"Thanks for playing, {player}! You scored {points}.")


if __name__ == "__main__":
    main()