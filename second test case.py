from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open Web Browser(Chrome)
driver = webdriver.Chrome()

# Step 2: Open YouTube
driver.get("https://www.youtube.com/")

# Step 3: Enter search query
search_input = driver.find_element(By.NAME, "search_query")
search_input.send_keys("selenium tutorial")

# Step 4: Click search button
search_button = driver.find_element(By.ID, "search-icon-legacy")
search_button.click()

# Step 5: Click on the first video in the search results
video_link = driver.find_element(By.ID, "video-title")
video_link.click()

# Step 6: Wait for the video to load
wait = WebDriverWait(driver, 10)
video_player = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".html5-main-video")))

# Step 7: Check if "Skip Ad" button is present and click on it if available
try:
    skip_ad_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-ad-skip-button")))
    skip_ad_button.click()
except:
    pass

# Step 8: Play the video
driver.execute_script("arguments[0].play();", video_player)

# Step 9: Wait for the video to finish
wait.until(EC.staleness_of(video_player))

# Step 10: Close the browser
driver.quit()