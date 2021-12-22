import time
import math
import pytest
from selenium import webdriver

answer = math.log(int(time.time()))


@pytest.mark.parametrize('links', ['https://stepik.org/lesson/236895/step/1',
                                    'https://stepik.org/lesson/236896/step/1',
                                    'https://stepik.org/lesson/236897/step/1',
                                    'https://stepik.org/lesson/236898/step/1',
                                    'https://stepik.org/lesson/236899/step/1',
                                    'https://stepik.org/lesson/236903/step/1',
                                    'https://stepik.org/lesson/236904/step/1',
                                    'https://stepik.org/lesson/236905/step/1'])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, links):
        link = f"{links}"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")