import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class CurrencyConverterTest(unittest.TestCase):

    def setUp(self):
        # Set up WebDriver
        self.driver = webdriver.Firefox()
        self.driver.get("https://duckduckgo.com")

    def test_currency_conversion(self):
        """Test conversion of 1 BGN to USD using DuckDuckGo"""
        # Search for the currency conversion
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys("1 BGN to USD")
        search_box.send_keys(Keys.RETURN)

        # Wait for the page to load and show results
        time.sleep(2)

        try:
            # Locate the exchange rate result
            rate_element = self.driver.find_element(By.XPATH, '//div[@class="result__body"]//span')
            exchange_rate = rate_element.text
            print(f"Exchange rate: 1 BGN = {exchange_rate} USD")
        except Exception as e:
            print(f"Error: Unable to retrieve exchange rate. {e}")
        
        # Save a screenshot for reference
        self.driver.save_screenshot("currency_conversion_result.png")
        
        # Wait a bit before closing
        time.sleep(5)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
