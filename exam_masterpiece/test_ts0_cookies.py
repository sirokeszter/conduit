def test_cookies():
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
        time.sleep(10)
        # Cookie accept with click accept button:
        driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]').click()

        # Decline button:
        # button_decline=driver.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[1]/div)

        def check_non_exists_by_xpath(xpath):
            try:
                driver.find_element_by_xpath(xpath)
                time.sleep(2)
            except NoSuchElementException:
                return True
            return False

        time.sleep(6)
        check_non_exists_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]')
        time.sleep(2)

    finally:
        driver.close()