from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button2 = browser.find_element_by_css_selector("[id='book']")
    button2.click()


    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)
    browser.find_element_by_tag_name('body').send_keys(Keys.END) # page scroll down

    answer_field = browser.find_element_by_css_selector("[id='answer']")
    answer_field.send_keys(y)

    button3 = browser.find_element_by_css_selector("[id='solve']")
    button3.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

