import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    browser.get('https://stepik.org')
    # time.sleep(100)
    link_auth = browser.find_element(By.CLASS_NAME, 'navbar__auth_login').get_attribute('href')
    browser.get(link_auth)
    time.sleep(5)
    browser.find_element(By.ID, "id_login_email").send_keys('****')
    browser.find_element(By.ID, "id_login_password").send_keys('****')
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
    print('ну, что авторизовались?')
    time.sleep(5)

    yield browser
    print("\nquit browser..")
    browser.quit()
