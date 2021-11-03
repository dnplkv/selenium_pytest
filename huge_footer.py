from selenium import webdriver
import time
import math

from selenium.webdriver.common.keys import Keys

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)
    browser.find_element_by_tag_name('body').send_keys(Keys.END)

    answer_field = browser.find_element_by_css_selector("[id='answer']")
    answer_field.send_keys(y)

    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option3 = browser.find_element_by_css_selector("[id='robotsRule']")
    option3.click()

    button = browser.find_element_by_css_selector('button')
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

