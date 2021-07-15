from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
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

    time.sleep(2)

    new_articel = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    time.sleep(2)


    def write_new_articel(title, about, content, tag):
        articel_title = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
        artical_about = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
        artical_content = driver.find_element_by_xpath('//*[@id="app"]//fieldset[3]/textarea')
        artical_tag = driver.find_element_by_xpath('//*[@id="app"]//fieldset[4]//input')
        publish_button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

        articel_title.send_keys(title)
        artical_about.send_keys(about)
        artical_content.send_keys(content)
        artical_tag.send_keys(tag)
        publish_button.click()

    write_new_articel("Valami", "Valamiről", "Valami a valamiről", "valami")

finally:
    pass
    # driver.close()
