from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def calc(num1, num2):
    return str(num1 + num2)


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_v = browser.find_element_by_css_selector("[id='num1']")
    num1 = int(num1_v.text)
    num2_v = browser.find_element_by_css_selector("[id='num2']")
    num2 = int(num2_v.text)
    result = calc(num1, num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)

    button = browser.find_element_by_css_selector('button')
    button.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
