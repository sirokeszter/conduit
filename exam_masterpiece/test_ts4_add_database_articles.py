def test_add_database_articles():
    import os
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    import csv
    import time
    from selenium.common.exceptions import NoSuchElementException

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    try:
        driver.get("http://localhost:1667/#")
        time.sleep(10)

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

        username = "kiskakas1"
        fill_login("kiskakas1@gmail.com", "Kiskakas1$")

        time.sleep(3)
        new_article = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
        time.sleep(2)
        article_title = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
        article_about = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
        article_content = driver.find_element_by_xpath('//*[@id="app"]//fieldset[3]/textarea')
        article_tag = driver.find_element_by_xpath('//*[@id="app"]//fieldset[4]//input')
        publish_button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

        # currentDir = os.getcwd()
        # currentFileCSV = currentDir + "//" + "test.csv"
        # csvFileObj = open(currentFileCSV)
        #sys.path.append(r'E:/conduit/exam_masterpiece')
        with open('E:/conduit/exam_masterpiece/test.csv', 'r', encoding='utf-8') as csvfile:
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
        user_feeds = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
        time.sleep(2)

        feed_title_list = []
        page_count = 1

        while True:
            time.sleep(2)
            feed_titles = driver.find_elements_by_xpath('//*[@id="app"]//div[2]//a/h1')
            for title in feed_titles:
                feed_title_list.append(title.text)

            try:
                page_count += 1
                driver.find_element_by_link_text(str(page_count)).click()
            except NoSuchElementException:
                # Stop loop if no more page available
                break

        print(feed_title_list)

        # Create a list from the feed's titles in csv:
        csv_title_count = 0
        with open('E:/conduit/exam_masterpiece/test.csv', 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                csv_title_count += 1

        print(csv_title_count)

        # Checking assertion by number of rows:
        assert csv_title_count == len(feed_title_list)

    finally:
        driver.close()
