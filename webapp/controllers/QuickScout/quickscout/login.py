def gm_login(driver, usermane, password):
    driver.get("http://www.gangstermind.com/")
    driver.find_element_by_id('loginForm')
    driver.find_element_by_name('user_name').send_keys(usermane)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('play').click()
