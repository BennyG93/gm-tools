from selenium.webdriver.support.ui import Select
import time
from . import driver
from . import cookies

def gm_hire(totalTurns, turmsInterval, location, headless):
    #  Start selenium driver instance
    webdriver = driver.gm_driver(headless, False)
    switcher={
                'casino':0,
                'coffee':1,
                'streets':2,
                'training':3
             }
    hireType = switcher.get(location,"Invalid hire location") # Select which hire button to press
    numberOfClicks = int(totalTurns/turmsInterval)
    webdriver.get("http://www.gangstermind.com/")
    # Load login cookies to restore session
    cookies.load_cookie(webdriver, 'gm_login_cookies.pkl')
    # webdriver.get("http://www.gangstermind.com/hire.php")
    i = 1
    while i < numberOfClicks+1:
        i += 1
        webdriver.get("http://www.gangstermind.com/hire.php")
        turnSelector = Select(webdriver.find_element_by_name('use_turns'))
        turnSelector.select_by_value(str(turmsInterval))
        hireButtons = webdriver.find_elements_by_name('hire_location')
        clickButton = hireButtons[hireType]
        clickButton.click()

    webdriver.close()
