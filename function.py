import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(chromeBrowser: webdriver.Chrome, dp_id, username, password):
    while (chromeBrowser.find_element(By.CLASS_NAME, "login-app--card").is_displayed() is False):
        chromeBrowser.refresh()
    chromeBrowser.find_element(By.ID, "username").clear()
    chromeBrowser.find_element(By.ID, "username").send_keys(username)
    time.sleep(1)
    chromeBrowser.find_element(By.ID, "password").clear()
    chromeBrowser.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)
    chromeBrowser.find_element(
        By.CLASS_NAME, "select2-selection__rendered").click()
    time.sleep(1)
    chromeBrowser.find_element(By.CLASS_NAME, "select2-search__field").clear()
    chromeBrowser.find_element(
        By.CLASS_NAME, "select2-search__field").send_keys(dp_id)
    time.sleep(1)
    chromeBrowser.find_element(
        By.CLASS_NAME, "select2-results__option--highlighted").click()
    time.sleep(1)
    chromeBrowser.find_element(
        By.XPATH, "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[4]/div/button").click()
    time.sleep(2)
    # WebDriverWait(chromeBrowser, 10).until(EC.url_changes(chromeBrowser.current_url))
    print('wait finish')
    # return chromeBrowser


def logout(chromeBrowser: webdriver.Chrome):
    chromeBrowser.find_element(By.CLASS_NAME, "header-menu__link").click()
    time.sleep(2)


def check_status(chromeBrowser: webdriver.Chrome):
    parent = chromeBrowser.find_element(By.CLASS_NAME, "user-profile-name")
    name = parent.find_element(By.TAG_NAME, 'span').text
    while name is None:
        chromeBrowser.refresh
    chromeBrowser.get('https://meroshare.cdsc.com.np/#/asba')
    time.sleep(1)
    chromeBrowser.find_element(By.XPATH, '''//*[@id="main"]/div/app-asba/div/div[1]/div/div/ul/li[3]/a''').click()
    time.sleep(1)
    Rank = input('Enter the rank:')
    chromeBrowser.find_element(By.XPATH, f'''//*[@id="main"]/div/app-asba/div/div[2]/app-share-list/div/div/div[2]/div[1]/div[{Rank}]/div/div[2]/div/div[3]/button''').click()
    time.sleep(2)
    status = chromeBrowser.find_element(By.XPATH, '''//*[@id="main"]/div/app-application-report/div/div[2]/div/div[3]/div/div[1]/div[7]/div/div/div[2]/div/label''').text
    
    # chromeBrowser.find_element()
    print(name,status)


# //*[@id="main"]/div/app-asba/div/div[2]/app-share-list/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div[3]/button
# //*[@id="main"]/div/app-asba/div/div[2]/app-share-list/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/button