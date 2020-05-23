import sys
import os
from selenium import webdriver

from . import login
from . import hire

def main(username, password, totalTurns, turmsInterval, location):
    if getattr(sys, 'frozen', False):
        chromedriver_folder = os.path.join(sys._MEIPASS, 'webapp/controllers/bin/chromedriver')
        print(chromedriver_folder)
        driver = webdriver.Chrome(chromedriver_folder)
    else:
        driver = webdriver.Chrome()

    login.gm_login(driver, username, password)
    hire.gm_hire(driver, totalTurns, turmsInterval, location)
