from Utils import SCORES_FILE_NAME
from os.path import exists


def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    print(f'You won {POINTS_OF_WINNING} in this game')
    content = None
    if exists(SCORES_FILE_NAME):
        file = open(SCORES_FILE_NAME, 'r')
        content = file.read()
        file.close()
    if content:
        current_score = int(content) + POINTS_OF_WINNING
    else:
        current_score = POINTS_OF_WINNING
    file = open(SCORES_FILE_NAME, 'w')
    file.write(str(current_score))
    file.close()
    return current_score
