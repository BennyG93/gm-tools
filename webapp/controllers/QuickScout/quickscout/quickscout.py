import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from . import login
from . import hire

def main(username, password, totalTurns, turmsInterval, location, headless):
    options = Options()
    options.headless = headless

    if getattr(sys, 'frozen', False):
        chromedriver_folder = os.path.join(sys._MEIPASS, 'webapp/controllers/bin/chromedriver')
        driver = webdriver.Chrome(chromedriver_folder, chrome_options=options)
    else:
        driver = webdriver.Chrome(chrome_options=options)

    login.gm_login(driver, username, password)
    hire.gm_hire(driver, totalTurns, turmsInterval, location)
