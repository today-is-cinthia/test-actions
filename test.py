from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest 
import os
import pathlib

# Configura opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecuta Chrome en modo headless (sin interfaz gráfica)
chrome_options.add_argument("--no-sandbox")  # Evita problemas de permisos en contenedores
chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemas de uso de memoria compartida en entornos con poco espacio

# Inicializa el ChromeDriver con las opciones
driver = webdriver.Chrome(options=chrome_options)

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


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
