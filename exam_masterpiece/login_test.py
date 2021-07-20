def test_login():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.common.exceptions import NoSuchElementException
    import time

    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    try:
        driver.get("http://localhost:1667/#/")
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

        username = "kiskacsa3"
        fill_login("kiskacsa3@gmail.com", "Kiskacsa3$")

        time.sleep(3)

        # Checking right up the user tag exist
        try:
            user_page= driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
            time.sleep(2)
            user_name = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/h4').text
            time.sleep(2)
            print(driver.current_url)
            if driver.current_url == f"http://localhost:1667/#/@{user_name}/" and user_name==username:
                print("Logged in with correct user name")
        except NoSuchElementException:
            print(False)


    finally:
        driver.close()
