import unittest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDynamicControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configure headless Firefox
        options = Options()
        options.add_argument("-headless")  # Uncomment for headless
        cls.driver = webdriver.Firefox(service=Service(), options=options)
        cls.driver.get("http://the-internet.herokuapp.com/dynamic_controls")
        
        # Create screenshots directory
        cls.screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(cls.screenshot_dir, exist_ok=True)
        print("\n🔥 Firefox initialized")

    def take_screenshot(self, name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        path = os.path.join(self.screenshot_dir, filename)
        self.driver.save_screenshot(path)
        print(f"📸 Screenshot saved: {filename}")

    def test_1_checkbox_flow(self):
        print("\n✅ Test 1 - Testing checkbox removal/addition...")
        
        # Remove checkbox
        remove_btn = self.driver.find_element(By.XPATH, "//button[text()='Remove']")
        remove_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        self.take_screenshot("checkbox_removed")  # Screenshot 1
        
        # Add checkbox back
        add_btn = self.driver.find_element(By.XPATH, "//button[text()='Add']")
        add_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkbox"))
        )
        self.take_screenshot("checkbox_restored")  # Screenshot 2

    def test_2_input_flow(self):
        print("\n✅ Test 2 - Testing input enable/disable...")
        
        # Enable input
        enable_btn = self.driver.find_element(By.XPATH, "//button[text()='Enable']")
        enable_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        self.take_screenshot("input_enabled")  # Screenshot 3
        
        # Disable input
        disable_btn = self.driver.find_element(By.XPATH, "//button[text()='Disable']")
        disable_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        self.take_screenshot("input_disabled")  # Screenshot 4

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("\n🔴 Browser closed")

if __name__ == "__main__":
    unittest.main()
