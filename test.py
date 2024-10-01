import os
import pathlib
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By  # Importar la clase By para los nuevos métodos

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "increase")  # Uso de By.ID
        increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "1")  # Uso de By.TAG_NAME

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element(By.ID, "decrease")  # Uso de By.ID
        decrease.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "-1")  # Uso de By.TAG_NAME

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "increase")  # Uso de By.ID
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "3")  # Uso de By.TAG_NAME

if __name__ == "__main__":
    unittest.main()
