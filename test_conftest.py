from selenium.webdriver.common.by import By
import time
import time
import math
import pytest

answer = math.log(int(time.time()))

link_start = "https://stepik.org/lesson/236895/step/1"
lesson_id_list = [236895, 236896, 236897, 236898, 236899, 236903, 236904,236905]


@pytest.mark.parametrize('lesson_id', lesson_id_list)
def test_auth_resolve(browser, lesson_id):
    browser.get(link_start)

    link_auth = browser.find_element(By.ID, 'ember458').get_attribute('href')
    browser.get(link_auth)

    browser.find_element(By.ID, "id_login_email").send_keys('m****@mail.ru')
    browser.find_element(By.ID, "id_login_password").send_keys('y*a')
    browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()


    link_lesson = f'https://stepik.org/lesson/{lesson_id}/step/1'

'''
в таком виде он будет запускаться 2 раза и 2 раза авторизоваться. 
Можно сделать фикстуру, которая запустит браузер, авторизуется и потом поехали тесты на страницах.
'''


