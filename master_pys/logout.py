from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
from selenium.common.exceptions import NoSuchElementException

try:
    driver.get("http://localhost:1667/")

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
    def fill_login(mail, pw):
        email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
        password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
        button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

        email.send_keys(mail)
        password.send_keys(pw)
        button.click()

    username="kiskacsa3"
    fill_login("kiskacsa3@gmail.com", "Kiskacsa3$")

    # Activate Log out:
    time.sleep(3)
    logout = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]')
    mousehover = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
    ActionChains(driver).move_to_element(mousehover).perform()
    time.sleep(3)
    actions = ActionChains(driver)
    actions.click(logout)
    actions.perform()

    # Checking the disappered username:
    if logout:

    def test_element_does_not_exist(self):
        with self.assertRaises(NoSuchElementException):
            driver.find_element_by_xpath("log_out")
        return("User panel disappered.")

finally:
    pass
    # driver.close()