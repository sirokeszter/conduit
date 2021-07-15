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

    fill_registration("kiskacsa5","kiskacsa5@gmail.com", "Kiskacsa5$")

    # time.sleep(3)
    # main_window = driver.window_handles[0]
    # alert_window=driver.find_element_by_xpath('/html/body/div[2]/div')
    # other_window = driver.switch_to.window('alert_window')
    # alert_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
    # ref_text = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]').text
    # print(ref_text)
    # alert_button.click()


    # Login alert:
    # alert = driver.switch_to.alert
    # ref_text = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]').text
    # time.sleep(2)
    # alert.accept()
    # time.sleep(1)
    # alert_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
    # print(ref_text.text)
    # alert_button.click()



    # xpath of the panel(alert window): /html/body/div[2]/div
    # text check: /html/body/div[2]/div/div[3] -> <div class="swal-text" style="">Your registration was successful!</div> ugyanebben van egy okgomb,akit accept-elni kell




finally:
    pass
    # driver.close()
