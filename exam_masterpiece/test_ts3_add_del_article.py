def test_add_del_article():
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
        driver.get("http://localhost:1667/")
        time.sleep(6)

        # Sign in:
        login = driver.find_element_by_xpath('//a[@href="#/login"]')
        time.sleep(2)
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

        time.sleep(4)

        # Checking the whole number of global feed titles:
        global_feed_titles = driver.find_elements_by_tag_name('h1')

        new_article = driver.find_element_by_xpath('//a[@href="#/editor"]').click()
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
        write_new_article("Kakasmese", "Kakasról", "Egyszer volt", "kakas")

        # Checking the elements (title, about, tag) of the new article:
        time.sleep(4)
        my_articles = driver.find_element_by_xpath(f'//a[@href="#/@{username}/"]').click()
        time.sleep(2)

        feed_title_list = []
        feed_about_list = []
        feed_tag_list = []

        page_count = 1

        article_box = driver.find_elements_by_xpath('//*[@id="app"]//div[@class="article-preview"]')
        feed_titles = driver.find_elements_by_tag_name('h1')
        feed_abouts = driver.find_elements_by_tag_name('p')
        feed_tags = driver.find_elements_by_xpath('//*[@class="tag-pill tag-default"]')

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

        assert feed_title_list[-1] == 'Kakasmese'
        assert feed_about_list[-1] == 'Kakasról'
        assert feed_tag_list[-1] == 'kakas'

        # Testing feed delete function:
        time.sleep(4)
        my_articles1 = driver.find_element_by_xpath(f'//a[@href="#/@{username}/"]').click()
        time.sleep(3)
        feed_titles1 = driver.find_elements_by_tag_name('h1')
        feed_titles1[-1].click()
        time.sleep(1)
        del_btn = driver.find_element_by_xpath('//*[@id="app"]//button/span')
        time.sleep(2)
        del_btn.click()
        time.sleep(2)

        # Collect the new list after deleting:
        mod_feed_title_list = []
        feed_titles_mod = driver.find_elements_by_tag_name('h1')
        for title in feed_titles_mod:
            mod_feed_title_list.append(title.text)

        print(len(global_feed_titles))
        print(len(mod_feed_title_list))

        # Checking the deleted feed not exist with the len of original global_feed_title (before-after):
        assert int(len(global_feed_titles)) == int(len(mod_feed_title_list))

    finally:
        driver.close()
