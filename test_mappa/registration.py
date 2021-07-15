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

    fill_registration("kiskacsa24","kiskacsa24@gmail.com", "Kiskacsa24$")

    time.sleep(3)
    alert_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
    ref_text = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]').text
    print(ref_text)
    # Checking correct alert messages coming...
    alert_button.click()

    # Checking registrated user name:
    user_page=driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
    time.sleep(2)
    user_name=driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/h4').text
    time.sleep(2)
    print(driver.current_url)
    print(user_name)
    if driver.current_url== f"http://localhost:1667/#/@{user_name}/":
        print("Registrated with correct user name")


finally:
    pass
    # driver.close()
