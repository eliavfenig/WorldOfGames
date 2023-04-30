import os
from CurrencyRouletteGame import play_roulette
from GuessGame import play_guess
from MemoryGame import play_memory
from MainScores import app
from Score import add_score
from Utils import SCORES_FILE_NAME


def welcome():
    i = 0
    while i < 1:
        name = input("Please enter your name: ")
        if name:
            print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
            i += 1
    return name


def load_game(name):
    while True:
        # get the chosen game form the user
        i = 0
        while i < 1:
            game_input = (input(f'''Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back: 
            2. Guess Game - guess a number and see if you chose like the computer: 
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS: '''))
            if not game_input.isdigit():
                print("please enter one of the digits (1, 2, 3)")
                continue
            game_input = int(game_input)
            game_dict = {
                1: "memory game",
                2: "guess game",
                3: "currency roulette"
            }
            game_chosen = game_dict.get(game_input)
            if game_chosen:
                i += 1

        # get the difficulty level from the user
        i = 0
        while i < 1:
            difficulty = input("Please choose game difficulty from 1 to 5: ")
            if not difficulty.isdigit():
                print("please enter one of the digits (1, 2, 3, 4, 5)")
                continue
            difficulty = int(difficulty)
            difficulty_dict = {
                1: "very easy",
                2: "easy",
                3: "normal",
                4: "hard",
                5: "very hard"
            }
            difficulty_chosen = difficulty_dict.get(difficulty)
            if difficulty_chosen:
                i += 1
        print(f"you have chosen to play {game_chosen} in difficulty level {difficulty_chosen}")

        # playing the games
        current_score = "0"
        # memory game
        if game_input == 1:
            is_winner = play_memory(difficulty)
            if is_winner:
                current_score = add_score(difficulty)
        # guess game
        elif game_input == 2:
            is_winner = play_guess(difficulty)
            if is_winner:
                current_score = add_score(difficulty)
        # Currency Roulette Game
        elif game_input == 3:
            is_winner = play_roulette(difficulty)
            if is_winner:
                current_score = add_score(difficulty)

        # does the user want to play another game
        print()
        print(f'{name}, thank you for playing {game_chosen}')
        print()
        i = 0
        while i < 1:
            game_over = input(f'Do you want to play another game ? (y/n) ')
            if game_over.lower() == "n":
                app.run()
                # webbrowser.open('http://127.0.0.1:5000')
                os.remove(SCORES_FILE_NAME)
                return
            elif game_over.lower() == "y":
                print()
                if current_score:
                    print(f'Your current score is: {current_score}')
                i += 1
            else:
                print("Your choice could not be recognized , please choose either (y/n) ")
                continue







