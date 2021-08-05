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
        time.sleep(6)

        # Activate Sign in input field:
        login = driver.find_element_by_xpath('//a[@href="#/login"]')
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
            feed_titles = driver.find_elements_by_tag_name('h1')
            for feed in feed_titles:
                feed_title_list.append(feed.text)
            try:
                page_count += 1
                driver.find_element_by_link_text(str(page_count)).click()
            except NoSuchElementException:
                # Stop loop if no more page available
                break

        print("The title-list of Global feeds: ", feed_title_list)
        print("Number of Global feeds: ", len(feed_title_list))

        # Writting to csv file:
        feed_count = 0
        with open('titles.csv', 'w', encoding='utf-8') as file:
            for title in feed_title_list:
                file.write(f'{feed_title_list}')
                feed_count += 1

        print(feed_count)

        # Comparing the number of the saved titles with number of the Global feed titles:
        assert int(len(feed_title_list)) == int(feed_count)

    finally:
        driver.close()
