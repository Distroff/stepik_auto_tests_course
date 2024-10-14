import time
from selenium.webdriver.common.by import By


def test_button_exists(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    buttons = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    time.sleep(7)
    assert buttons, 'The button is now found'
