import threading
import webbrowser

from flask import Flask, render_template
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from os.path import exists

app = Flask(__name__)


@app.route('/')
def score_server():
    score = False
    if exists(SCORES_FILE_NAME):
        file = open(SCORES_FILE_NAME, 'r')
        score = file.read()
    if score:
        return render_template('current_score.html', SCORE=score)
    else:
        return render_template('error_page.html', ERROR=BAD_RETURN_CODE)


if __name__ == '__main__':
    # url = "http://127.0.0.1:5000"
    # threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    app.run()
