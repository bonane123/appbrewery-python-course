#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.

print(
    "Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100."
)
level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
player_number = 0
computer_number = 0
is_guessed = False

if level == 'easy':
    level = 10
elif level == 'hard':
    level = 5


def computer_guess():
    computer_number = random.randint(1, 100)
    return computer_number


computer_result = computer_guess()
while level and not is_guessed:

    def guess(level):
        print(f'You have {level} attempts to guess the number')
        player_number = int(input('Make a guess: '))
        return player_number, level

    def guess_decision(computer_result, player_result, is_guessed):
        result_note = ''

        if computer_result < player_result:
            result_note = 'Too high. \nGuess again.'
        elif computer_result > player_result:
            result_note = 'Too low. \nGuess again.'
        else:
            result_note = f'{computer_result} You win the game. \nGuess again'
            is_guessed = True

        return result_note, is_guessed

    if not is_guessed:

        player_result, level_result = guess(level)
        result_note, is_guessed = guess_decision(computer_result,
                                                 player_result, is_guessed)
        print(result_note)
    level -= 1
    if level == 0:
        print('You are out of trial. You lose')

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
