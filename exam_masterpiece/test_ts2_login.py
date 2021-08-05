def test_login():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.action_chains import ActionChains
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
        time.sleep(3)
        mousehover = driver.find_element_by_xpath('//a[@href="#/login"]')
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

        username = "kiskakas1"
        fill_login("kiskakas1@gmail.com", "Kiskakas1$")

        time.sleep(3)

        # Checking right up the user tag exist
        try:
            user_page = driver.find_element_by_xpath(f'//a[@href="#/@{username}/"]')
            time.sleep(2)
            user_page.click()
            user_name = driver.find_element_by_tag_name('h4').text
            time.sleep(2)
            print(driver.current_url)
            if driver.current_url == f"http://localhost:1667/#/@{user_name}/" and user_name == username:
                print("Logged in with correct user name")
        except NoSuchElementException:
            print(False)


    finally:
        driver.close()
