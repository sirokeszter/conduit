def test_paging_feedlist():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.common.exceptions import NoSuchElementException
    import time

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    try:
        driver.get("http://localhost:1667/#/")

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


        fill_login("kiskakas1@gmail.com", "Kiskakas1$")

        time.sleep(3)
        feed_title_list = []
        page_count = 1

        while True:
            time.sleep(2)
            feed_titles = driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
            for feed in feed_titles:
                feed_title_list.append(feed.text)
            try:
                page_count += 1
                driver.find_element_by_link_text(str(page_count)).click()
            # driver.find_element_by_xpath('//*[@id="app"]//nav/ul/li[%]/a')
            except NoSuchElementException:
                # Stop loop if no more page available
                break

        print("The title-list of Global feeds: ", feed_title_list)
        print("Number of Global feeds: ", len(feed_title_list))

        # Writting to csv file:
        with open('titles.csv', 'w', encoding='utf-8') as file:
            file.write(f'{feed_title_list}')

        # Count the number of the saved titles in the csv file:
        csv_title_list = []
        with open('titles.csv', 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                csv_title_list.append(row)

        # print(len(csv_title_list))

        # Comparing the number of the saved titles with number of the Global feed titles:
        assert int(len(feed_title_list)) == int(len(csv_title_list))



    finally:
        driver.close()
