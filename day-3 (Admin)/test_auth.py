import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

# Website that needs login
BASE_URL = "https://the-internet.herokuapp.com/basic_auth"
CORRECT_CREDENTIALS = "admin:admin"
INCORRECT_CREDENTIALS = "wrong:wrong"

class BasicAuthTest(unittest.TestCase):
    
    def setUp(self):
        """Start the browser in hidden mode."""
        options = Options()
        options.headless = True  # Run in the background
        
        self.driver = webdriver.Firefox(options=options)
        
    def test_correct_credentials(self):
        """✅ test_correct_credentials"""
        self.driver.get(f"https://{CORRECT_CREDENTIALS}@the-internet.herokuapp.com/basic_auth")
        self.assertIn("Congratulations!", self.driver.page_source)  # Check success message
    
    def test_missing_credentials(self):
        """❌ test_missing_credentials"""
        self.driver.get(BASE_URL)
        try:
            alert = Alert(self.driver)
            print("Alert found")
            alert.dismiss()
        except NoAlertPresentException:
            print("No alert found")
            raise

        page_title = self.driver.title
        
        print(f"Page Title: {page_title}")  # Optional: see the title of the page
        
        # Check that the page title is not 'The Internet' (or another expected title)
        self.assertNotEqual(page_title, "The Internet")
        
        # Ensure that the success message is not present
        self.assertNotIn("Congratulations!", self.driver.page_source)
    
    def test_incorrect_credentials(self):
        """❌ test_incorrect_credentials"""
        self.driver.get(f"https://{INCORRECT_CREDENTIALS}@the-internet.herokuapp.com/basic_auth")


        try:
            alert = Alert(self.driver)
            print("Alert found")
            alert.dismiss()
        except NoAlertPresentException:
            print("No alert found")
            raise


        page_title = self.driver.title
        print(f"Page Title: {page_title}")  # Optional: see the title of the page
        
        # Check that the page title is not 'The Internet'
        self.assertNotEqual(page_title, "The Internet")
        
        # Ensure that the success message is not present
        self.assertNotIn("Congratulations!", self.driver.page_source)
    
    def tearDown(self):
        """Close the browser."""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
    # unittest.main(verbosity=2, defaultTest="BasicAuthTest.test_incorrect_credentials")
