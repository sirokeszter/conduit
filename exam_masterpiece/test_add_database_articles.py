def test_add_database_articles():
    import pprint

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    import csv
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

        username= "kiskacsa3"
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
                article_tag.send_keys(row[3])
                publish_button.click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
                time.sleep(1)

        my_articles=driver.find_element_by_xpath('//*[@id="app"]//div[2]//div[1]/ul/li[1]/a').click()
        time.sleep(2)

        feed_title_list = []
        feed_about_list=[]
        feed_content_list=[]
        feed_tag_list=[]

        page_count = 1

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

            try:
                page_count += 1
                driver.find_element_by_link_text(str(page_count)).click()
            except NoSuchElementException:
                # Stop loop if no more page available
                break

        pprint.pprint(list(zip(feed_title_list[-2:], feed_about_list[-2:], feed_tag_list[-2:])))

        # Checking assertion in data

    finally:
        driver.close()