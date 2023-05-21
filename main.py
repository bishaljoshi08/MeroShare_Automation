# import required modules
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# importing the login credentials
from config import credentials

# importing login
from function import login, logout, check_status


# Driver Code
if __name__ == '__main__':

    # Set the path to the ChromeDriver executable
    chromedriver_path = 'chromedriver.exe'

    # Create a Service object
    service = Service(chromedriver_path)

    # Create Chrome options and set headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--log-level=3")


    # create object
    chromeBrowser = webdriver.Chrome(service=service, options=chrome_options)
    # open browser and navigate to meroshare
    chromeBrowser.get('https://meroshare.cdsc.com.np/#/login')

    max_attempts = 3
    for each_account in credentials:
        # storing the required parameters to login
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
                    print("Login attempt failed1. Retrying....")
            except:
                current_attempt += 1
                chromeBrowser.refresh()
                print("Login attempt failed. Retrying....")
        if current_attempt == max_attempts:
            print("Login failed")
            continue

        check_status(chromeBrowser=chromeBrowser)
        logout(chromeBrowser=chromeBrowser)

        # chromeBrowser.find_element("class", "select2-search__field").send_keys(dp_id)
        time.sleep(2)
