# import required modules
import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# importing the login credentials
from config import credentials

# importing login
from function import apply_shares, check_IPO, check_status, limit_login, login, logout

# Driver Code
if __name__ == "__main__":
    # Set the path to the ChromeDriver executable
    chromedriver_path = "chromedriver.exe"

    # Create a Service object
    service = Service(chromedriver_path)

    # # Create Chrome options and set headless mode
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-logging")
    # chrome_options.add_argument("--log-level=3")

    # create object
    chromeBrowser = webdriver.Chrome(service=service, options=chrome_options)
    # open browser and navigate to meroshare
    chromeBrowser.get("https://meroshare.cdsc.com.np/#/login")

    # configure logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    formatter = logging.Formatter("%(asctime)s : %(name)s : %(message)s")

    file_handler = logging.FileHandler("login.log")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    apply = False

    for i, each_account in enumerate(credentials):
        # storing the required parameters to login
        limit_login(each_account=each_account, chromeBrowser=chromeBrowser)
        if apply:
            if i == 0:
                list_rank = check_IPO(chromeBrowser=chromeBrowser)

            print(list_rank)
            apply_shares(
                chromeBrowser=chromeBrowser,
                each_account=each_account,
                list_rank=list_rank,
            )
        else:
            check_status(chromeBrowser=chromeBrowser)

        logout(chromeBrowser=chromeBrowser)

        # chromeBrowser.find_element("class", "select2-search__field").send_keys(dp_id)
        time.sleep(2)
