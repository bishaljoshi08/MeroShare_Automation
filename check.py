# import required modules
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

# importing the login credentials
from config import credentials

# importing functions
from function import login, logout, check_status


# Driver Code
if __name__ == '__main__':

    # Set the path to the ChromeDriver executable
    chromedriver_path = 'chromedriver.exe'

    # Create a Service object
    service = Service(chromedriver_path)

    # create object
    chromeBrowser = webdriver.Chrome(service=service)

    # open browser and navigate to meroshare
    chromeBrowser.get('https://meroshare.cdsc.com.np/#/login')

    for each_account in credentials:
        # storing the required parameters to login
        dp_id = each_account['dp_id']
        username = each_account['username']
        password = each_account['password']
        login(chromeBrowser=chromeBrowser, dp_id=dp_id,
              username=username, password=password)
        check_status(chromeBrowser=chromeBrowser)
        logout(chromeBrowser=chromeBrowser)

        # chromeBrowser.find_element("class", "select2-search__field").send_keys(dp_id)
        time.sleep(2)
