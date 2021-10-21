from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='treasure']")
    x = x_element.get_attribute('valuex')
    y = calc(x)

    answer_field = browser.find_element_by_css_selector("[id='answer']")
    answer_field.send_keys(y)

    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[id='peopleRule']")
    option2.click()
    option3 = browser.find_element_by_css_selector("[id='robotsRule']")
    option3.click()

    button = browser.find_element_by_css_selector('button')
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
