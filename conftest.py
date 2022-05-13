import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Default language EN")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    print("\n[+] Start chrome browser for test.. Please wait..")
    time.sleep(2)

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\n[!] Quit browser. Test end!")
    browser.quit()
