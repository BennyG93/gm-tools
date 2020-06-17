from . import driver
from . import login
from . import hire

def main(username, password, totalTurns, turmsInterval, location, headless, detached):
    webdriver = driver.gm_driver(headless, detached)
    login.gm_login(username, password)
    hire.gm_hire(totalTurns, turmsInterval, location)
