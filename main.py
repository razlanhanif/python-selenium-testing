from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Open Web Browser(Chrome)
driver = webdriver.Chrome()

# Step 2: Open URL https://opensource-demo.orangehrmlive.com/
driver.get("https://salesdemo.klinify.com/#/")

# Step 3: Enter username
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("testings")

# Step 4: Enter password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("testings")

# Step 5: Click on login
login_button = driver.find_element(By.TAG_NAME, "button")
login_button.click()

# Step 6: Capture title of the home page (actual title)
actual_title = driver.title

# Step 7: Verify title of the page: ORangeHRM (expected)
expected_title = "Klinify"
if actual_title == expected_title:
    print("Title verification passed!")
else:
    print(f"Title verification failed! Expected: {expected_title}, Actual: {actual_title}")

# Step 8: Close browser
driver.quit()
