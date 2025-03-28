from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # поиск кодом нужного значения х
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")

    # расчет значения, которое нужно вписать
    y = calc(x)
    # поиск окна, куда вписать ответ
    input_result = browser.find_element(By.ID, "answer")
    # вписываем ответ
    input_result.send_keys(y)
    # поиск кнопки чекбокса
    checkbox_point = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    # отмечаем чекбокс
    checkbox_point.click()
    # поиск нужного радиобатона
    radiobutton_point = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    # отмечаем радиобатон
    radiobutton_point.click()
    #ищем кнопку submit и нажимаем на нее
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


