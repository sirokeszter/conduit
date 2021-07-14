from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import csv

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:1667/#/")
    #Cookie accept:
    button_accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()
    from selenium.webdriver.common.action_chains import ActionChains

    # Activate Sign in input field
    login = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    mousehover = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    ActionChains(driver).move_to_element(mousehover).perform()
    time.sleep(3)
    actions = ActionChains(driver)
    actions.click(login)
    actions.perform()

    # Fill input fields:
    def fill_login(email, password):
        driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input').send_keys("email")
        driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input').send_keys("password")
        driver.find_element_by_xpath('//*[@id="app"]//form/button').click()

finally:
    pass
    # driver.close()
