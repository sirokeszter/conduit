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
    driver.get("http://localhost:1667/#/")
    # Cookie accept:
    button_accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()
    from selenium.webdriver.common.action_chains import ActionChains

    # Activate Sign in input field:
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


    fill_login("kiskacsa5@gmail.com", "Kiskacsa5$")

    # Checking right up the user tag exist
    # def check_exists_by_xpath(xpath):
    #     try:
    #         driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
    #     except NoSuchElementException:
    #         return False
    #     return True

    # Check user name:
    # user_logged_in = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').text
    # assert user_logged_in.text == f"{'username'}"
    # # felső sarokban megjelenik a user
    # <a href="#/@kiskakas/" class="nav-link">kiskakas</a>
    # xpath: //*[@id="app"]/nav/div/ul/li[4]/a

finally:
    pass
    # driver.close()
