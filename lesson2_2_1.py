from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # поиск кодом нужного значения х
    x_element = browser.find_element(By.CSS_SELECTOR,"#num1.nowrap")
    x = int(x_element.text)
    y_element = browser.find_element(By.CSS_SELECTOR,"#num2.nowrap")
    y = int(y_element.text)
    # расчет значения, которое нужно вписать

    result_sum = y+x
    sum_text = str(result_sum)

    # поиск ответа среди списка
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum_text)  # ищем элемент с текстом "Python"

    #ищем кнопку submit и нажимаем на нее
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()





