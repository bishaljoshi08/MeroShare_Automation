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
    chromeBrowser.find_element(By.ID, "password").clear()
    chromeBrowser.find_element(By.ID, "password").send_keys(password)
    chromeBrowser.find_element(
        By.CLASS_NAME, "select2-selection__rendered").click()
    chromeBrowser.find_element(By.CLASS_NAME, "select2-search__field").clear()
    chromeBrowser.find_element(
        By.CLASS_NAME, "select2-search__field").send_keys(dp_id)
    chromeBrowser.find_element(
        By.CLASS_NAME, "select2-results__option--highlighted").click()
    chromeBrowser.find_element(
        By.XPATH, "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[4]/div/button").click()
    WebDriverWait(chromeBrowser, 30).until(
        EC.presence_of_element_located((By.ID, "sideBar")) 
        )
    # WebDriverWait(chromeBrowser, 10).until(EC.url_changes(chromeBrowser.current_url))
    # print('wait finish')
    # return chromeBrowser


def logout(chromeBrowser: webdriver.Chrome):
    chromeBrowser.find_element(By.CLASS_NAME, "header-menu__link").click()
    


@decorator_login_success
def check_status(name, chromeBrowser: webdriver.Chrome):
    chromeBrowser.get('https://meroshare.cdsc.com.np/#/asba')
    WebDriverWait(chromeBrowser, 15).until(
        EC.presence_of_element_located((By.XPATH, '''//*[@id="main"]/div/app-asba/div/div[1]/div/div/ul/li[3]/a''')) 
        )
    chromeBrowser.find_element(
        By.XPATH, '''//*[@id="main"]/div/app-asba/div/div[1]/div/div/ul/li[3]/a''').click()
    WebDriverWait(chromeBrowser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "company-list")) 
        )
    Rank = 2
    chromeBrowser.find_element(
        By.XPATH, f'''//*[@id="main"]/div/app-asba/div/div[2]/app-share-list/div/div/div[2]/div[1]/div[{Rank}]/div/div[2]/div/div[3]/button''').click()
    
    time.sleep(2)
    status = chromeBrowser.find_element(
        By.XPATH, '''//*[@id="main"]/div/app-application-report/div/div[2]/div/div[3]/div/div[1]/div[7]/div/div/div[2]/div/label''').text
    print(status)
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
    WebDriverWait(chromeBrowser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "company-list")) 
        )
    parent_div = chromeBrowser.find_element(By.XPATH, '''//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div''')
    child_div = parent_div.find_elements(By.XPATH, "./div")
    for i,each in enumerate(child_div):
        print("Enter the value {} for {}".format(i+1,each.text.partition('\n')[0]))
    list_rank = input("Enter your value: ")
    return list_rank

@decorator_login_success
def apply_shares(name, chromeBrowser: webdriver.Chrome, each_account,list_rank):
    crn = each_account['crn']
    pin = each_account['pin']
    chromeBrowser.get('https://meroshare.cdsc.com.np/#/asba')
    
    WebDriverWait(chromeBrowser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "company-list")) 
        )

    chromeBrowser.find_element(
        By.XPATH, f'''//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[{list_rank}]/div/div[2]/div/div[4]/button''').click()
        # By.XPATH, '''//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[2]/div/div[4]/button''').click()
    WebDriverWait(chromeBrowser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "card__company-list")) 
        )
    
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
    
    # else:
    #     option = 1

    # chromeBrowser.find_element(
    #     By.XPATH, f'''//*[@id="selectBank"]/option[{option}]''').click()
    chromeBrowser.find_element(By.NAME, "appliedKitta").send_keys(10)
    chromeBrowser.find_element(By.NAME, "crnNumber").send_keys(crn)
    chromeBrowser.find_element(By.ID, "disclaimer").click()
    WebDriverWait(chromeBrowser, 15).until(
        EC.presence_of_element_located((By.XPATH, '''//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]'''))
        )
    chromeBrowser.find_element(By.XPATH, '''//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]''').click()
    WebDriverWait(chromeBrowser, 15).until(
        EC.presence_of_element_located((By.ID, "transactionPIN"))
        )
    chromeBrowser.find_element(By.ID, "transactionPIN").send_keys(pin)
    chromeBrowser.find_element(By.XPATH, '''//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]''').click()
    WebDriverWait(chromeBrowser, 15).until(
        EC.presence_of_element_located((By.ID, "toast-container"))
        )
    status = chromeBrowser.find_element(By.ID, "toast-container").text
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

def limit_login(each_account, chromeBrowser, max_attempts=3):
    dp_id = each_account['dp_id']
    username = each_account['username']
    password = each_account['password']
    current_attempt = 0
    while current_attempt < max_attempts:
        try:
            # chromeBrowser =
            login(chromeBrowser=chromeBrowser, dp_id=dp_id,
                    username=username, password=password)
            if chromeBrowser.current_url == 'https://meroshare.cdsc.com.np/#/dashboard':
                break
            else:
                current_attempt += 1
                chromeBrowser.refresh()
                logger.error(f"Login attempt failed for {username}. Retrying....")
        except:
            current_attempt += 1
            chromeBrowser.refresh()
            logger.error(f"Login attempt failed for {username}. Retrying....")
    if current_attempt == max_attempts:
        logger.warning(f"Login failed for {username}. Moving on to next one.")
        
