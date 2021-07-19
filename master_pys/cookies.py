from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
import csv

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:1667/")
    button_accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()
    # Decline button:
    # button_decline=driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[1]/div)

    # panel= driver.find_element_by_id("cookie-policy-panel")
    # if panel.is_displayed():
    #     raise Exception("Cookie panel should not be found")
    def test_element_does_not_exist(self):
        with self.assertRaises(NoSuchElementException):
            driver.find_element_by_id("cookie-policy-panel")

    print("Cookie panel disappered.")

finally:
    driver.close()
