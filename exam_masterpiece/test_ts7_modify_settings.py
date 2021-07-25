def test_modify_settings():
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
        time.sleep(10)

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

        username="kiskakas1"
        fill_login("kiskakas1@gmail.com", "Kiskakas1$")

        time.sleep(5)

        user_page = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
        time.sleep(2)
        edit_profile = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]//a').click()
        time.sleep(3)

        def profile_edition(photo,username, bio,email,password):
            profile_photo = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
            profile_username = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
            profile_bio = driver.find_element_by_xpath('//*[@id="app"]//fieldset[3]/textarea')
            profile_email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[4]/input')
            profile_password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[5]/input')
            update_button=driver.find_element_by_xpath('//*[@id="app"]//fieldset/button')


            profile_photo.clear()
            profile_photo.send_keys(photo)
            profile_username.clear()
            profile_username.send_keys(username)
            profile_bio.clear()
            profile_bio.send_keys(bio)
            profile_email.clear()
            profile_email.send_keys(email)
            profile_password.clear()
            profile_password.send_keys(password)
            update_button.click()


        profile_edition("https://senior.hu/wp-content/uploads/2019/01/eltuntek-a-tyukok-6.jpg", "tyukocska1", "Anyám tyúkja", "tyukocska1@gmail.com", "Tyukocska1$")

        time.sleep(3)
        confirm_button = driver.find_element_by_xpath('/html/body/div[2]//button')
        ref_text = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]').text
        print(ref_text)
        # Checking correct alert messages
        assert ref_text == 'Update successful!'
        confirm_button.click()

        # Checking modified user name:
        time.sleep(5)
        user_page1 = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
        time.sleep(2)
        user_name = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/h4').text
        time.sleep(2)
        print(driver.current_url)
        if driver.current_url == f"http://localhost:1667/#/@{user_name}/" and user_name==username:
            print('The modified username is: ', f"{user_name}")

        # Checking login with modified data:
        logout = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]')
        logout.click()
        login = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
        time.sleep(2)
        login.click()
        time.sleep(2)
        fill_login("tyukocska1@gmail.com", "Tyukocska1$")
        time.sleep(3)
        confirm_button = driver.find_element_by_xpath('/html/body/div[2]//button')

        try:
            time.sleep(4)
            user_page = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').click()
            time.sleep(4)
            user_name = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/h4').text
            time.sleep(2)
            print(driver.current_url)
            if driver.current_url == f"http://localhost:1667/#/@{user_name}/" and user_name == username:
                print("Logged in with correct user name")
        except NoSuchElementException:
            print("Registration failed!")

    finally:
        driver.close()