from . import driver
from . import cookies

def gm_login(usermane, password):
    webdriver = driver.gm_driver(False, True)
    webdriver.get("http://www.gangstermind.com/")
    webdriver.find_element_by_id('loginForm')
    webdriver.find_element_by_name('user_name').send_keys(usermane)
    webdriver.find_element_by_name('password').send_keys(password)
    webdriver.find_element_by_name('play').click()
    webdriver.get("http://www.gangstermind.com/mainindex.php")
    # Save Cookies after logging in
    cookies.save_cookie(webdriver, 'gm_login_cookies.pkl')
