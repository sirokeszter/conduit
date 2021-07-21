import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

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

    username= "kiskakas1"
    fill_login("kiskakas1@gmail.com", "Kiskakas1$")
    time.sleep(2)

    # Write new article
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
            article_tag.send_keys(row[3])
            publish_button.click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
            time.sleep(1)

    # Comparing the imported data from csv with the new posts' data:
    my_articles=driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
    time.sleep(2)

    feed_title_list = []
    feed_about_list=[]
    feed_content_list=[]
    feed_tag_list=[]

    page_count = 1

    # def write_feed_data(title, about, tag):
    #     return(feed_data_list)
    #     # feed_titles = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/h1')
    #     # feed_abouts = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/p')
    #     # feed_tags = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/div/a')
    #     # read_more_btn = driver.find_elements_by_xpath('//*[@id="app"]//a/span')
    #     # feed_contents = driver.find_elements_by_xpath('//*[@id="app"]/div//p')
    #
    # feed_data_list=[]
    # my_feeds=driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a')
    # for write_feed_data in range(len(my_feeds)):
    #     feed_data_list.append(write_feed_data)

    while True:
        time.sleep(2)
        feed_titles = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/h1')
        feed_abouts = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/p')
        feed_tags = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/div/a')
        for title in feed_titles:
            feed_title_list.append(title.text)
        for about in (feed_abouts):
            feed_about_list.append(about.text)
        for tag in feed_tags:
            feed_tag_list.append(tag.text)

        # read_more_btns = driver.find_elements_by_xpath('//*[@id="app"]//a/span')
        # for rm_btn in read_more_btns:
        #     rm_btn.click()
        #     time.sleep(2)
        #     feed_content = driver.find_element_by_xpath('//*[@id="app"]//p')
        #     feed_content_list.append(feed_content.text)
        #     time.sleep(2)
        #     feed_author = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/a').click()
        #     break
        # while True:
        #     my_feeds = driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[1]/a')
        #     read_more_btns = driver.find_elements_by_xpath('//*[@id="app"]//a/span')
        #     for i in range(len(my_feeds)):
        #         for rm_btn in read_more_btns:
        #             rm_btn.click()
        #             time.sleep(2)
        #             feed_content = driver.find_element_by_xpath('//*[@id="app"]//p')
        #             feed_content_list.append(feed_content.text)
        #             time.sleep(2)
        #             feed_author = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/a').click()
        #     try:
        #         len(my_feeds)[i] += 1
        #     except NoSuchElementException:
        #         # Stop loop if no more page available
        #         break
        try:
            page_count += 1
            driver.find_element_by_link_text(str(page_count)).click()
        except NoSuchElementException:
            # Stop loop if no more page available
            break

    pprint.pprint(list(zip(feed_title_list[-2:], feed_about_list[-2:], feed_content_list[-2:], feed_tag_list[-2:])))

    # Checking assertion in data

finally:
    pass
    # driver.close()