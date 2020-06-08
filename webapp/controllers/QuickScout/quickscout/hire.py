from selenium.webdriver.support.ui import Select

def gm_hire(driver, totalTurns, turmsInterval, location):
    switcher={
                'casino':0,
                'coffee':1,
                'streets':2,
                'training':3
             }
    hireType = switcher.get(location,"Invalid hire location") # Select which hire button to press
    numberOfClicks = int(totalTurns/turmsInterval)
    driver.get("http://www.gangstermind.com/hire.php")
    i = 1
    while i < numberOfClicks+1:
        i += 1
        turnSelector = Select(driver.find_element_by_name('use_turns'))
        turnSelector.select_by_value(str(turmsInterval))
        hireButtons = driver.find_elements_by_name('hire_location')
        clickButton = hireButtons[hireType]
        clickButton.click()
