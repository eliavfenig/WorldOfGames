import random
import time
from Utils import screen_cleaner


def generate_sequence(difficulty):
    random_list = random.sample(range(0, 102), int(difficulty))
    # line_clear = '\x1b[2k'
    print(random_list, end='')
    time.sleep(2)
    screen_cleaner()
    return random_list


def get_list_from_user(difficulty):
    while True:
        user_list = input("enter the numbers you remember: ")
        # if not re.search("\D+", user_list):
        user_list = user_list.split(',')
        user_list2 = []
        for i in user_list:
            user_list2.append(int(i))
        if len(user_list2) != int(difficulty):
            print(f"your list must be {int(difficulty)} long")
        else:
            return user_list2


def is_list_equal(random_list, user_list):
    print(f'this is random list {random_list}')
    if random_list == user_list:
        return True
    else:
        return False


def play_memory(difficulty):
    random_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    is_winner_memory = is_list_equal(random_list, user_list)
    if is_winner_memory:
        print("congrats you won the memory game")
    else:
        print("you lost the memory game")
    return is_winner_memory
