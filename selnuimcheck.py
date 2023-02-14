from selenium import webdriver
from selenium.webdriver.common.by import By

# Instantiate a new browser instance
browser = webdriver.Chrome()

# Navigate to the web page
browser.get("https://liad07.github.io/selnuimdetector/")

# Get the text of the web page and print it
page_text = browser.find_element(By.TAG_NAME,"body").text
print(page_text)

# Close the browser
browser.quit()
