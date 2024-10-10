from selenium.webdriver.common.by import By
import time
import math
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# link_start = "https://stepik.org/lesson/236895/step/1"
lesson_id_list = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]
ans = []

@pytest.mark.parametrize('lesson_id', lesson_id_list)
def test_auth_resolve(browser, lesson_id):

    # time.sleep(2)
    link_lesson = f'https://stepik.org/lesson/{lesson_id}/step/1'
    #  Go to lesson
    # link_lesson = f'https://stepik.org/lesson/236895/step/1'
    browser.get(link_lesson)
    time.sleep(5)
    # add the answer
    browser.find_element(By.CLASS_NAME, 'ember-text-area').clear()
    browser.find_element(By.CLASS_NAME, 'ember-text-area').send_keys(str(math.log(int(time.time()))))
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    time.sleep(2)
    elem = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    ans.append(elem)
    assert elem == 'Correct!'
    # time.sleep(10)
    # print('запуск теста')
    a = [t for t in ans if t != 'Correct!']
    print(*a)
'''
в таком виде он будет запускаться 2 раза и 2 раза авторизоваться. 
Можно сделать фикстуру, которая запустит браузер, авторизуется и потом поехали тесты на страницах.
'''


