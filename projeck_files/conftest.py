import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Options_FX
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='ru, en')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    lang = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        print('\nstart Chrome browser for test..')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(7)
    elif browser_name == 'firefox':
        print('\nstart Firefox browser for test..')
        options = Options_FX()
        options.set_preference('intl.accept_languages', lang)
        browser = webdriver.Firefox(options=options)
        browser.implicitly_wait(7)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nquit browser..')
    browser.quit()
