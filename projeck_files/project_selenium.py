import time

import math

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def alert_print_cod(web_element):
    return print(web_element.switch_to.alert.text.split(': ')[1])


def main():

    link = "http://suninjuly.github.io/get_attribute.html"
    browse = webdriver.Chrome()

    try:
        browse.get(link)
        x = browse.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex")
        browse.find_element(By.CSS_SELECTOR, ".form-group #answer").send_keys(calc(x))
        browse.find_element(By.CSS_SELECTOR, ".check-input#robotCheckbox").click()
        browse.find_element(By.CSS_SELECTOR, ".check-input#robotsRule").click()
        browse.find_element(By.CSS_SELECTOR, '.btn-default').click()
    finally:
        time.sleep(30)
        browse.quit()


if __name__ == "__main__":
    main()
