import pickle
from pathlib import Path

def save_cookie(driver, file):
    gm_tools_dir = "/tmp/gm-tools/"
    Path(gm_tools_dir).mkdir(parents=True, exist_ok=True) # Ensure gm-tools dir is created
    full_path = gm_tools_dir + file # Combine gm-tools dir with cookies file
    with open(full_path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler) # Dump all selenium cookies with pickle

def load_cookie(driver, file):
    gm_tools_dir = "/tmp/gm-tools/"
    full_path = gm_tools_dir + file
    with open(full_path, 'rb') as cookiesfile: # Loop over each cookie and load into selenium
        cookies = pickle.load(cookiesfile)
        #  Deletes all cookies
        driver.delete_all_cookies()
        # Load login session cookies
        for cookie in cookies:
            driver.add_cookie(cookie)
