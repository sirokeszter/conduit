from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
from selenium.webdriver.common.keys import Keys
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:1667/")
    # Cookie accept:
    button_accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()

    # Activate Sign in input field:
    login = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    login.click()


    # Fill input fields:
    def fill_login(mail, pw):
        email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
        password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
        button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

        email.send_keys(mail)
        password.send_keys(pw)
        button.click()


    fill_login("kiskacsa3@gmail.com", "Kiskacsa3$")

    time.sleep(2)
    new_article = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    time.sleep(2)
    article_title = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
    article_about = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
    article_content = driver.find_element_by_xpath('//*[@id="app"]//fieldset[3]/textarea')
    article_tag = driver.find_element_by_xpath('//*[@id="app"]//fieldset[4]//input')
    publish_button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

    with open('csvtext.csv',encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            article_title.send_keys(row[0])
            article_about.send_keys(row[1])
            article_content.send_keys(row[2])
            article_tag.send_keys(row[4])
            publish_button.click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
            time.sleep(1)

        # time.sleep(2)
        # new_article.click()
        # time.sleep(1)
        # article_title.send_keys(title)
        # time.sleep(1)
        # article_about.send_keys(about)
        # time.sleep(1)
        # article_content.send_keys(content)
        # time.sleep(1)
        # article_tag.send_keys(tag)
        # time.sleep(1)
        # publish_button.click()

    # # creating a loop to do the procedure and append failed cases to the list
    # with open('csvtext.csv') as csvfile:
    #     csvreader = csv.reader(csvfile, delimiter=',')
    #     for row in csvreader:
    #         time.sleep(2)
    #         new_article.click()
    #         write_new_article(row[0], row[1], row[2], row[3])


finally:
    pass
    # driver.close()