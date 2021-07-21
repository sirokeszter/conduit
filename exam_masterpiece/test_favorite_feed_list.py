def test_favorite_feed_list():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.common.exceptions import NoSuchElementException
    import time
    import csv

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    try:
        driver.get("http://localhost:1667/#/")
        # Cookie accept:
        button_accept = driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()

        # Activate Sign in input field:
        login = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
        time.sleep(3)
        login.click()


        # Fill input fields:
        def fill_login(mail, pw):
            email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
            password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
            button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

            email.send_keys(mail)
            password.send_keys(pw)
            button.click()

        username="kiskacsa3"
        fill_login("kiskacsa3@gmail.com", "Kiskacsa3$")

        time.sleep(3)
        like_btns=driver.find_elements_by_xpath('//*[@id="app"]//button/i')
        like_counters=driver.find_elements_by_xpath('//*[@id="app"]//button/span')
        for like in like_btns:
            if len(like_btns)< 3:
                like.click()
            else:
                break

        # for counter in like_counters[:3]:
        #     assert counter.text==1
        article_list=[]
        time.sleep(2)
        user_page = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
        time.sleep(2)
        favorite_article = driver.find_element_by_xpath('//*[@id="app"]//div[2]//ul/li[2]/a').click()
        time.sleep(2)
        articles = driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
        for article in articles:
            article_list.append(article.text)
        print(article_list)

        home=driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[1]/a').click()
        time.sleep(1)
        liked_list=[]
        global_feeds=driver.find_elements_by_xpath('//*[@id="app"]//a/h1')
        for liked_feed in global_feeds[:3]:
            liked_list.append(liked_feed.text)

        print(liked_list)
        # Checking identity of liked feeds fromglobal feeds and favorite feeds and the number of checked feeds:
        assert liked_list == article_list
        assert len(article_list) ==3

    finally:
        driver.close()