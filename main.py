import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element(By.ID, 'book')
button.click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = str(math.log(abs(12*math.sin(int(x)))))

inp_element = browser.find_element(By.CSS_SELECTOR, 'input')
inp_element.send_keys(y)

sbm = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
sbm.click()


time.sleep(15)
browser.quit()