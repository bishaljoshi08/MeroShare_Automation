import time
import logging
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config import mult_bank_name, mult2_bank_name


#configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(message)s')

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def decorator_login_possible(func):
    def inner(*args, **kwargs):
        chromeBrowser = kwargs['chromeBrowser']
        while (chromeBrowser.find_element(By.CLASS_NAME, "login-app--card").is_displayed() is False):
            chromeBrowser.refresh()
        func(*args, **kwargs)
    return inner


def decorator_login_success(func):
    def inner(*args, **kwargs):
        chromeBrowser = kwargs['chromeBrowser']
        parent = chromeBrowser.find_element(By.CLASS_NAME, "user-profile-name")
        name = parent.find_element(By.TAG_NAME, 'span').text
        while name is None or chromeBrowser.find_element(By.XPATH, '''//*[@id="sideBar"]/nav/ul/li[8]/a''').is_displayed() is False:
            chromeBrowser.refresh()
        return func(name, *args, **kwargs)
    return inner


@decorator_login_possible
def login(chromeBrowser: webdriver.Chrome, dp_id, username, password):
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
    # print('wait finish')
    # return chromeBrowser


def logout(chromeBrowser: webdriver.Chrome):
    chromeBrowser.find_element(By.CLASS_NAME, "header-menu__link").click()
    time.sleep(2)


@decorator_login_success
def check_status(name, chromeBrowser: webdriver.Chrome):
    chromeBrowser.get('https://meroshare.cdsc.com.np/#/asba')
    time.sleep(1)
    chromeBrowser.find_element(
        By.XPATH, '''//*[@id="main"]/div/app-asba/div/div[1]/div/div/ul/li[3]/a''').click()
    time.sleep(1)
    Rank = 1
    chromeBrowser.find_element(
        By.XPATH, f'''//*[@id="main"]/div/app-asba/div/div[2]/app-share-list/div/div/div[2]/div[1]/div[{Rank}]/div/div[2]/div/div[3]/button''').click()
    time.sleep(2)
    status = chromeBrowser.find_element(
        By.XPATH, '''//*[@id="main"]/div/app-application-report/div/div[2]/div/div[3]/div/div[1]/div[7]/div/div/div[2]/div/label''').text
    company = chromeBrowser.find_element(
        By.XPATH, '''//*[@id="main"]/div/app-application-report/div/div[2]/div/div[1]/div/div/div/div/div/span[1]''').text
    # chromeBrowser.find_element()
    if status == 'Alloted':
        logger.debug(f'Congratulations {name}, You got the shares of {company}')
    elif status == 'Not Alloted':
        logger.debug(f'Try again {name}, You are not alloted the shares of {company}')
    else:
        logger.debug(f'Either result is not published or your application was not successful.')

@decorator_login_success
def check_IPO(name,chromeBrowser: webdriver.Chrome):
    chromeBrowser.get('https://meroshare.cdsc.com.np/#/asba')
    time.sleep(1)
    parent_div = chromeBrowser.find_element(By.XPATH, '''//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div''')
    child_div = parent_div.find_elements(By.XPATH, "./div")
    for i,each in enumerate(child_div):
        print("Enter the value {} for {}".format(i+1,each.text.partition('\n')[0]))
    list_rank = input("Enter your value: ")
    return list_rank

@decorator_login_success
def apply_shares(name, chromeBrowser: webdriver.Chrome, crn, pin,list_rank):
    chromeBrowser.get('https://meroshare.cdsc.com.np/#/asba')
    time.sleep(1)
    chromeBrowser.find_element(
        By.XPATH, f'''//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[{list_rank}]/div/div[2]/div/div[4]/button''').click()
        # By.XPATH, '''//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[2]/div/div[4]/button''').click()
    time.sleep(1)
    input = chromeBrowser.find_element(
        By.ID, '''selectBank''')
    input.click()
    input.send_keys(Keys.ARROW_DOWN)
    input.send_keys(Keys.ARROW_DOWN)
    if name in mult_bank_name:
        input.send_keys(Keys.ARROW_DOWN)
    if name in mult2_bank_name:
        input.send_keys(Keys.ARROW_DOWN)
        input.send_keys(Keys.ARROW_DOWN)
    input.send_keys(Keys.ENTER)
    time.sleep(1)
    
    # else:
    #     option = 1

    # chromeBrowser.find_element(
    #     By.XPATH, f'''//*[@id="selectBank"]/option[{option}]''').click()
    time.sleep(1)
    chromeBrowser.find_element(By.XPATH, '''//*[@id="appliedKitta"]''').send_keys(10)
    chromeBrowser.find_element(By.XPATH, '''//*[@id="crnNumber"]''').send_keys(crn)
    chromeBrowser.find_element(By.XPATH, '''//*[@id="disclaimer"]''').click()
    chromeBrowser.find_element(By.XPATH, '''//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]''').click()
    time.sleep(1)
    chromeBrowser.find_element(By.XPATH, '''//*[@id="transactionPIN"]''').send_keys(pin)
    chromeBrowser.find_element(By.XPATH, '''//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]''').click()
    time.sleep(2)
    status = chromeBrowser.find_element(By.XPATH, '''//*[@id="toast-container"]''').text
    logger.debug(f'{status} of {name}')
    '''
     * Description
     *
     * Parameters:
     *  - parameter_name - Description
     *
     * Returns:
     * Return description
    '''

    # company = chromeBrowser.find_element(
    #     By.XPATH, '''//*[@id="main"]/div/app-application-report/div/div[2]/div/div[1]/div/div/div/div/div/span[1]''').text
    # # chromeBrowser.find_element()
    # print(f'{name} ko heram hai aba')
    # if status == 'Alloted':
    #     print(f'Oh lucky person, paryo paryo {company} paryo')
    # elif status == 'Not Alloted':
    #     print(f'Luck nai chaina k parcha, {company} parena')
