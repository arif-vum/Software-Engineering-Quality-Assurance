import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "http://www.python.org"


class TestSelenium(unittest.TestCase):

    def test_visit_webpage(self):
        "visit URL, get screenshot"
        driver = webdriver.Firefox()
        driver.get(URL)
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)
        about = driver.find_element(By.ID, "about")
        self.assertTrue(about)
        about.click()
        downloads = driver.find_element(By.XPATH, '//*[@id="downloads"]')
        downloads.click()
        driver.save_screenshot("downloads1.png")
        time.sleep(10)
        driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
