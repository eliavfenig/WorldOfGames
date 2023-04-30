def welcome():
    name = input("Please enter your name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    return


def load_game():
    i = 0
    while i < 1:
        game_input = int(input(f'''Please choose a game to play: \n
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n
        2. Guess Game - guess a number and see if you chose like the computer\n
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n'''))
        game_dict = {
            1: "memory_game",
            2: "guess_game",
            3: "currency_roulette"
        }
        game_chosen = game_dict.get(game_input)
        if game_chosen:
            i += 1
    i = 0
    while i < 1:
        difficulty = input("Please choose game difficulty from 1 to 5: ")
        difficulty_dict = {
            1: "very_easy",
            2: "easy",
            3: "normal",
            4: "hard",
            5: "very_hard"
        }
        difficulty_chosen = difficulty_dict.get(int(difficulty))
        if difficulty_chosen:
            i += 1
            return difficulty, game_input
    print(f"you have chosen to play {game_chosen} in difficulty level {difficulty_chosen}")



