## Steps for installing Selenium in Arch Linux

### 1. Install Firefox
Firefox is the browser we will automate. Install it using:

```bash
sudo pacman -S firefox
```

Check if Firefox is installed:

```bash
firefox --version
```

---

### 2. Install GeckoDriver
GeckoDriver is required for Selenium to control Firefox. Install it using:

```bash
sudo pacman -S geckodriver
```

If not available, install it from the AUR:

```bash
yay -S geckodriver
```

Verify the installation:

```bash
geckodriver --version
```

---

### 3. Install Selenium
Selenium is a Python library for browser automation. Install it using:

```bash
pip install selenium
```

---

### 4. Write the Python Script
Below is a simple Python script to open a webpage, print its title, and take a screenshot.

#### Script: `selenium_task.py`
```python
from selenium import webdriver

# Set up Firefox options
options = webdriver.FirefoxOptions()

# Initialize the Firefox driver
driver = webdriver.Firefox(options=options)

# Open a webpage
driver.get("https://www.google.com/?hl=en-GB&quot;)

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
```

---

### 5. Run the Script
Save the script as `selenium_task.py` and run it:

```bash
python selenium_task.py
```

---
