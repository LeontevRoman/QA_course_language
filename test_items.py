import time

from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'


def test_user_language(browser):
    browser.get(link)
    time.sleep(1)

    buttons = browser.find_elements(by=By.CLASS_NAME, value='btn-add-to-basket')
    assert len(buttons) == 1, "WOW! It's selector not unique"
