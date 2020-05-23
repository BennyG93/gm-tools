from selenium.webdriver.support.ui import Select

def gm_hire(driver, totalTurns, turmsInterval, location):
    switcher={
                'casino':'Go to Casino',
                'coffee':'Go to Coffee',
                'streets':'Go to the streets',
                'training':'Go to training rooms'
             }
    hireType = switcher.get(location,"Invalid hire location") # Select which hire button to press
    numberOfClicks = int(totalTurns/turmsInterval)
    driver.get("http://www.gangstermind.com/hire.php")
    i = 1
    while i < numberOfClicks+1:
        i += 1
        turnSelector = Select(driver.find_element_by_name('use_turns'))
        turnSelector.select_by_value(str(turmsInterval))
        hireButton = driver.find_element_by_xpath(f"//input[@name='hire_location'][@type='submit'][@value=\"{hireType}\"]")
        hireButton.click()
