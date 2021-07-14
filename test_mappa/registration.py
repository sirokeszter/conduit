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
    # Cookie accept:
    button_accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()
    from selenium.webdriver.common.action_chains import ActionChains

    # Activate Sign in input field
    sign_up = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]')
    mousehover = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a')
    ActionChains(driver).move_to_element(mousehover).perform()
    time.sleep(3)
    actions = ActionChains(driver)
    actions.click(sign_up)
    actions.perform()


    # Fill input fields:
    def fill_registration(user, mail, pw):
        username= driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
        email=driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
        password= driver.find_element_by_xpath('//*[@id="app"]//fieldset[3]/input')
        button= driver.find_element_by_xpath('//*[@id="app"]//form/button')

        username.send_keys(user)
        email.send_keys(mail)
        password.send_keys(pw)
        button.click()

    fill_registration("kiskacsa10","kiskacsa10@gmail.com", "Kiskacsa10$")

    # alert_button = driver.find_element_by_xpath('//div[4]/div/button').click()
    # print(alert_button.text)

    # Successfull login:
    # alert = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]')
    # ref_text = "Your registration was successful!"
    # assert (alert_window == ref_text)
    # print(alert_window.text)
    # time.sleep(2)
    # alert_window.accept()  megnézzük,miután megnyomtuk, eltűnik-e
    # time.sleep(1)

    # alert_window = driver.find_element_by_xpath('/html/body/div[2]/div').text
    # ref_text = "Your registration was successful!"
    # assert (alert_window == ref_text)
    # print(alert_window.text)
    # time.sleep(2)
    # alert_window.accept()

    # xpath of the panel(alert window): /html/body/div[2]/div
    # text check: /html/body/div[2]/div/div[3] -> <div class="swal-text" style="">Your registration was successful!</div> ugyanebben van egy okgomb,akit accept-elni kell

    # Checking right up the user tag exist
    # def check_exists_by_xpath(xpath):
    #     try:
    #         driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
    #     except NoSuchElementException:
    #         return False
    #     return True

    #
    # user_logged_in = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').text
    # assert user_logged_in.text == f"{'username'}"
    # # felső sarokban megjelenik a user
    # <a href="#/@kiskakas/" class="nav-link">kiskakas</a>
    # xpath: //*[@id="app"]/nav/div/ul/li[4]/a


finally:
    pass
    # driver.close()
