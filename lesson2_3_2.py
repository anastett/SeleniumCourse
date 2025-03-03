from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #поиск кнопки и нажатие на нее
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()

    #переключаемся на новую вкладку
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # поиск кодом нужного значения х
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    x = x_element.text
    # расчет значения, которое нужно вписать
    y = calc(x)
    # поиск окна, куда вписать ответ
    input_result = browser.find_element(By.CSS_SELECTOR, "#answer.form-control")
    # вписываем ответ
    input_result.send_keys(y)
    #ищем кнопку submit и нажимаем на нее
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.quit()

