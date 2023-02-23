import random


def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty))
    return int(secret_number)


def get_guess_from_user(difficulty):
    while True:
        user_guess = input(f"Please guess a number between 1 to {difficulty}: ")
        if not user_guess.isdigit():
            continue
        user_guess = int(user_guess)
        i = 0
        while i < 1:
            if user_guess >= 1 or user_guess <= int(difficulty):
                i += 1
            else:
                print("the number you chose are not in the range, try again")
        return int(user_guess)


def compare_guess_2_random(user_guess, secret):
    if user_guess == secret:
        print("You won !!!")
        return True
    else:
        print(f'You lost !!!\n the correct answer is: {secret}')
        return False


def play_guess(difficulty):
    secret = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    is_winner = compare_guess_2_random(user_guess, secret)
    return is_winner



