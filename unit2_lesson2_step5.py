from selenium import webdriver
import time

try:
    link = "https://SunInJuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
