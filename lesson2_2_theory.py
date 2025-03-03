from selenium import webdriver
from selenium.webdriver.common.by import By

import time
browser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")
#time.sleep(10)
#browser.execute_script("document.title='Script executing';alert('Robots at work');")
#time.sleep(10)

link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

#здесь футтер перекрывает нужный элемент, вылетит ошибка
#button = browser.find_element(By.TAG_NAME, "button")
#button.click()

# здесь мы просим проскроллить элемент дополнительно
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(5)


#отправка файла с учетом пути до него
import os
# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')
element.send_keys(file_path)