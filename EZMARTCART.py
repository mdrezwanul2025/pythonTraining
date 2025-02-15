from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # Import the Service class

# Path to your WebDriver executable (e.g., chromedriver)
driver_path = r"C:\Users\mdrez\OneDrive\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Create a Service object and pass it to the WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Navigate to the URL
url = "https://ezmartcart.company.site/"
driver.get(url)

# Give the page some time to load (optional)
driver.implicitly_wait(10)  # 10 seconds

# Find the element by XPath and click it
xpath = '/html/body/div[3]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/a[1]/div[3]'
element = driver.find_element(By.XPATH, xpath)
element.click()

# You can add more interactions here...
xpath = '/html/body/div[3]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/a[1]/div[3]'
element = driver.find_element(By.XPATH, xpath)
element.click()
# Close the browser (optional)
driver.quit()
