from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest


class TestElements(unittest.TestCase):
    def test_elements1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        element_one = browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]")
        element_one.send_keys("word one")
        element_two = browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]")
        element_two.send_keys("word two")
        element_three = browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]")
        element_three.send_keys("word three")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Texts should be equal")

    def test_elements2(self):
        link = "https://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        element_one = browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]")
        element_one.send_keys("word one")
        element_two = browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]")
        element_two.send_keys("word two")
        element_three = browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]")
        element_three.send_keys("word three")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Texts should be equal")

if __name__ == "__main__":
    pytest.main()

