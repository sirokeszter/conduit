def test_registration():
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
        driver.get("http://localhost:1667/")
        time.sleep(6)

        # Activate Sign up input field
        sign_up = driver.find_element_by_xpath('//a[@href="#/register"]')
        time.sleep(5)
        mousehover = driver.find_element_by_xpath('//a[@href="#/register"]')
        ActionChains(driver).move_to_element(mousehover).perform()
        time.sleep(3)
        actions = ActionChains(driver)
        actions.click(sign_up)
        actions.perform()

        # Fill input fields:
        def fill_registration(user, mail, pw):
            username = driver.find_element_by_xpath('//*[@id="app"]//fieldset[1]/input')
            email = driver.find_element_by_xpath('//*[@id="app"]//fieldset[2]/input')
            password = driver.find_element_by_xpath('//*[@id="app"]//fieldset[3]/input')
            button = driver.find_element_by_xpath('//*[@id="app"]//form/button')

            username.send_keys(user)
            email.send_keys(mail)
            password.send_keys(pw)
            button.click()

        # Registration with correct, non-existing data:
        fill_registration("kiskakas1", "kiskakas1@gmail.com", "Kiskakas1$")
        time.sleep(3)

        alert_button = driver.find_element_by_xpath('//button[text()="OK"]')
        ref_text1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]').text
        sub_ref_text1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]').text

        # Checking correct alert messages
        assert ref_text1 == 'Welcome!'
        assert sub_ref_text1 == 'Your registration was successful!'
        alert_button.click()

        # Checking registrated user name:
        time.sleep(4)
        usern = "kiskakas1"
        user_page = driver.find_element_by_xpath(f'//a[@href="#/@{usern}/"]')
        time.sleep(2)
        user_page.click()
        time.sleep(4)
        user_name = driver.find_element_by_tag_name('h4').text
        time.sleep(2)
        print(driver.current_url)
        print(user_name)
        assert driver.current_url == f"http://localhost:1667/#/@{user_name}/"

        # Logout ckecking
        time.sleep(3)
        logout = driver.find_element_by_class_name('ion-android-exit')
        logout.click()

        def test_element_does_not_exist(self):
            with self.assertRaises(NoSuchElementException):
                driver.find_element_by_xpath("log_out")
            return ("User panel disappered.")

        # Registration with correct, existing data:
        time.sleep(5)
        sign_up.click()
        time.sleep(3)
        fill_registration("kiskakas1", "kiskakas1@gmail.com", "Kiskakas1$")
        time.sleep(3)

        ref_text2 = driver.find_element_by_class_name('swal-title')
        sub_ref_text2 = driver.find_element_by_class_name('swal-text')
        alert_button = driver.find_element_by_xpath('//button[text()="OK"]')

        # Checking correct alert messages
        assert ref_text2.text == 'Registration failed!'
        assert sub_ref_text2.text == 'Email already taken.'
        alert_button.click()

        # Registration with unformal email:
        time.sleep(3)
        fill_registration("kiskakas2", "kiskakas2", "Kiskakas2$")
        time.sleep(5)

        # Checking correct alert messages # újra kellett definuálnom a ref-text-eket és a buttont, mert nem ismerte fel őket
        ref_text3 = driver.find_element_by_class_name('swal-title')
        sub_ref_text3 = driver.find_element_by_class_name('swal-text')
        alert_button = driver.find_element_by_xpath('//button[text()="OK"]')
        assert ref_text3.text == 'Registration failed!'
        assert sub_ref_text3.text == 'Email must be a valid email.'
        alert_button.click()

        # Registration with unformal password:
        time.sleep(3)
        fill_registration("kiskakas2", "kiskakas2@gmail.com", "kiskakas")
        time.sleep(3)

        # Checking correct alert messages
        ref_text4 = driver.find_element_by_class_name('swal-title')
        sub_ref_text4 = driver.find_element_by_class_name('swal-text')
        alert_button = driver.find_element_by_xpath('//button[text()="OK"]')
        assert ref_text4.text == 'Registration failed!'
        assert sub_ref_text4.text == 'Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.'
        alert_button.click()

    finally:
        driver.close()
