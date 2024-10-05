from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class testReg1(unittest.TestCase):
    def test_reg1(self):

        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            firstnm = browser.find_element(By.CSS_SELECTOR, '.first[required]')  # first_name
            lstnm = browser.find_element(By.CSS_SELECTOR, '.second[required]')  # last_name
            eml = browser.find_element(By.CSS_SELECTOR, '.third[required]') #   email
            firstnm.send_keys('Max')
            lstnm.send_keys('SQL')
            eml.send_keys('1@1.com')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Somthing wrong')

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_reg2(self):

        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            firstnm = browser.find_element(By.CSS_SELECTOR, '.first[required]')  # first_name
            lstnm = browser.find_element(By.CSS_SELECTOR, '.second[required]')  # last_name
            eml = browser.find_element(By.CSS_SELECTOR, '.third[required]')  # email
            firstnm.send_keys('Max')
            lstnm.send_keys('SQL')
            eml.send_keys('1@1.com')


            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Somthing wrong')

        finally:
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__=='__main__':
    unittest.main()