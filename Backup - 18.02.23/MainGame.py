from Live import welcome, load_game
from GuessGame import generate_number, get_guess_from_user, play_guess
from MemoryGame import play_memory
from CurrencyRouletteGame import play_roulette

# global parameters for all games
welcome()
difficulty, game_type = load_game()

# memory game
if game_type == 1:
    play_memory(difficulty)

# guess game
elif game_type == 2:
    play_guess(difficulty)

# Currency Roulette Game
elif game_type == 3:
    play_roulette(difficulty)




