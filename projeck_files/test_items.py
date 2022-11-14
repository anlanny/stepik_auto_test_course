from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

# import time


def test_checking_contains_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    # time.sleep(30)
    assert WebDriverWait(browser, 5).until(method=expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, '.btn-add-to-basket')), message='No add to basket button')
