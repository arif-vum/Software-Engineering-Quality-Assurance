from selenium import webdriver

# Set up Firefox options
options = webdriver.FirefoxOptions()

# Initialize the Firefox driver
driver = webdriver.Firefox(options=options)

# Open a webpage
driver.get("https://www.google.com/?hl=en-GB")

# Print the page title
print(driver.title)

# Keep the browser open for 10 seconds (for demonstration)
import time
time.sleep(10)

# Take a screenshot and save it to a file
screenshot_path = "screenshot_headless.png"
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved to: {screenshot_path}")

# Close the browser
driver.quit()
