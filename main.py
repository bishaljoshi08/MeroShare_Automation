# import required modules
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 


# Driver Code
if __name__ == '__main__':

    # create object
    chromeBrowser = webdriver.Chrome( executable_path='chromedriver.exe')

    # open browser and navigate to meroshare
    chromeBrowser.get('https://meroshare.cdsc.com.np/#/login')

    # storing the required parameters to login
    dp_id = ''
    username = ''
    password = ''


    # passing the value to the form to login 
    chromeBrowser.find_element(By.ID, "username").send_keys(username)
    time.sleep(1)
    chromeBrowser.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)
    chromeBrowser.find_element(By.CLASS_NAME, "select2-selection__rendered").click()
    time.sleep(1)
    chromeBrowser.find_element(By.CLASS_NAME, "select2-search__field").send_keys(dp_id)
    time.sleep(1)
    chromeBrowser.find_element(By.CLASS_NAME, "select2-results__option--highlighted").click()
    time.sleep(1)
    chromeBrowser.find_element(By.XPATH, "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[4]/div/button").click()
    
    # chromeBrowser.find_element("class", "select2-search__field").send_keys(dp_id)
    time.sleep(2)