import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle

def gm_driver(headless, detached):
    options = Options()
    if headless:
        options.headless = True
    else:
        options.headless = False

    if detached:
        options.add_experimental_option("detach", True)
    else:
        options.add_experimental_option("detach", False)

    if getattr(sys, 'frozen', False):
        chromedriver_folder = os.path.join(sys._MEIPASS, 'webapp/controllers/bin/chromedriver')
        driver = webdriver.Chrome(chromedriver_folder, chrome_options=options)
    else:
        driver = webdriver.Chrome(chrome_options=options)

    return driver
