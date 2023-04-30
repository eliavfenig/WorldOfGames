from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://127.0.0.1:5000"
def test_scores_service():
    my_driver = webdriver.Chrome()
    my_driver.get(url)
    try:
        score = my_driver.find_element(By.ID, 'score')
        score = int(score.text)
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except:
        return False


def main_function():
    if test_scores_service():
        return 0
    else:
        return -1


result = main_function()
print(result)
