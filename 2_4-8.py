from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from project_selenium import calc, alert_cod


def main():
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    try:
        browser.implicitly_wait(5)
        browser.get(link)
        button = browser.find_element(By.ID, 'book')
        WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
        button.click()
        x = browser.find_element(By.ID, 'input_value').text
        browser.find_element(By.ID, 'answer').send_keys(calc(x))
        browser.find_element(By.ID, 'solve').click()
        alert_cod(browser)

    finally:
        browser.quit()


if __name__ == '__main__':
    main()
