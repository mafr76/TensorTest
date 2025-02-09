import time
from pydoc import pager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()

try:
    # Открываем страницу
    url = ('https://sbis.ru/')
    driver.get(url)
    time.sleep(2)
    link_text = driver.find_element(By.LINK_TEXT, "Контакты")
    link = link_text.get_attribute("href")
    driver.get(link)
    time.sleep(2)
    banner = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div/a')
    banner.click()
    time.sleep(2)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    try:
        element1 = driver.find_element(By.XPATH, '//*[text()="Сила в людях"]')
        print(element1.text)
    except Exception as err:
        print(repr(err))
    try:
        element2 = element1.find_element(By.XPATH, './/ancestor::div/p/a[contains(text(), "Подробнее")]')
        link = element2.get_attribute("href")
        time.sleep(2)
        driver.get(link)
    except Exception as err:
        print(repr(err))



finally:
    input('Press Enter to close browser...')
    driver.quit()  # Закрываем браузер

