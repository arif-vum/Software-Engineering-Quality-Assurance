import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options  # Required import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDynamicControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configure headless properly
        options = Options()
        options.add_argument("-headless")  # The working argument for Firefox
        
        cls.driver = webdriver.Firefox(
            service=Service(),
            options=options
        )
        cls.driver.get("http://the-internet.herokuapp.com/dynamic_controls")
        print("\n🔥 Firefox running in TRUE headless mode")

    def test_1_checkbox_flow(self):
        print("\n✅ Test 1 - Testing checkbox removal/addition...")
        
        # Remove checkbox
        remove_btn = self.driver.find_element(By.XPATH, "//button[text()='Remove']")
        remove_btn.click()
        
        # Verify removal
        message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        assert "It's gone!" in message.text, "Removal message not displayed"
        print("✔ Checkbox successfully removed")
        
        # Add checkbox back
        add_btn = self.driver.find_element(By.XPATH, "//button[text()='Add']")
        add_btn.click()
        
        # Verify restoration
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkbox"))
        )
        message = self.driver.find_element(By.ID, "message")
        assert "It's back!" in message.text, "Restoration message not displayed"
        print("✔ Checkbox successfully restored")

    def test_2_input_flow(self):
        print("\n✅ Test 2 - Testing input enable/disable...")
        
        # Enable input
        enable_btn = self.driver.find_element(By.XPATH, "//button[text()='Enable']")
        enable_btn.click()
        
        # Verify enabling
        message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        input_field = self.driver.find_element(By.CSS_SELECTOR, "#input-example input")
        assert "It's enabled!" in message.text, "Enable message not displayed"
        assert input_field.is_enabled(), "Input field not actually enabled"
        input_field.send_keys("Test Input")
        print("✔ Input successfully enabled and text entered")
        
        # Disable input
        disable_btn = self.driver.find_element(By.XPATH, "//button[text()='Disable']")
        disable_btn.click()
        
        # Verify disabling
        message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        assert "It's disabled!" in message.text, "Disable message not displayed"
        assert not input_field.is_enabled(), "Input field not actually disabled"
        print("✔ Input successfully disabled")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("\n🔴 Browser closed - All tests completed successfully!")

if __name__ == "__main__":
    unittest.main()
