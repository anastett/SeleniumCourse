from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #задаем ожидание, пока не станет 100 долларов цена
    price = WebDriverWait(browser, 13).until(
        ec.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    #поиск кнопки и нажатие на нее
    button = browser.find_element(By.ID, "book")
    button.click()

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

