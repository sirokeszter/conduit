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


    username = "lovacska1"
    fill_login("lovacska1@gmail.com", "Lovacska1$")

    time.sleep(2)

    new_article = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    time.sleep(2)


    def write_new_article(title, about, content, tag):
        article_title = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
        article_about = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
        article_content = driver.find_element_by_xpath('//*[@id="app"]//fieldset[3]/textarea')
        article_tag = driver.find_element_by_xpath('//*[@id="app"]//fieldset[4]//input')
        publish_button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

        article_title.send_keys(title)
        article_about.send_keys(about)
        article_content.send_keys(content)
        article_tag.send_keys(tag)
        publish_button.click()

    # Write a new article:
    write_new_article("Valami", "Valamiről", "Valami a valamiről", "valami")

    # checking the elements of the new article:
    time.sleep(1)
    my_articles = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
    time.sleep(2)

    feed_title_list = []
    feed_about_list = []
    feed_content_list = []
    feed_tag_list = []

    page_count = 1

    article_box = driver.find_elements_by_xpath('//*[@id="app"]//div[@class="article-preview"]')
    feed_titles = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/h1')
    feed_abouts = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/p')
    read_more_btns = driver.find_elements_by_xpath('//*[@id="app"]//a/span')
    feed_contents = driver.find_element_by_xpath('//*[@id="app"]/div//p')
    feed_tags = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/div/a')

    time.sleep(2)
    for article in article_box:
        for title in feed_titles:
            feed_title_list.append(title.text)
        for about in feed_abouts:
            feed_about_list.append(about.text)
        for tag in feed_tags:
            feed_tag_list.append(tag.text)

        try:
            page_count += 1
            driver.find_element_by_link_text(str(page_count)).click()
        except NoSuchElementException:
            # Stop loop if no more page available
            break

    print(feed_title_list[-1:], feed_about_list[-1:], feed_tag_list[-1:])

    assert feed_title_list[-1] == 'Valami'
    assert feed_about_list[-1] == 'Valamiről'
    assert feed_tag_list[-1] == 'valami'

    #Testing feed delete function:
    time.sleep(1)
    my_articles1 = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
    feed_titles1 = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/h1')
    feed_titles1[-1].click()
    time.sleep(1)
    del_btn=driver.find_element_by_xpath('//*[@id="app"]//button/span').click()
    time.sleep(1)


finally:
    driver.close()
