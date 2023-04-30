import requests
import random


def get_money_interval(difficulty):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    ils_rate = data['rates']['ILS']
    dollar = random.randint(1, 100)
    nis = round((dollar * ils_rate), 2)
    difficulty = int(difficulty)
    print(nis)
    interval = (nis - (5 - difficulty), nis +(5 - difficulty))
    return interval, dollar


def get_guess_from_user(dollar):
    user_guess = float(input(f'try to convert {dollar} amount of dollar to ILS :'))
    return user_guess


def play_roulette(difficulty):
    interval, dollar = get_money_interval(difficulty)
    user_guess = get_guess_from_user(dollar)
    if interval[0] <= user_guess <= interval[1]:
        print(f'Congrats, you won the Currency game')
    else:
        print("You lost the game")

