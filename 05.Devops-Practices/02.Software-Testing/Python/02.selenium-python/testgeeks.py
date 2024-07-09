from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# initialize and open the page.
service=Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://geeksforgeeks.org")

# Maximize the browser window
driver.maximize_window()
time.sleep(1)

# Find the dark mode toggle button by class name
dark_mode_button = driver.find_element(By.CLASS_NAME, "darkMode-wrap")
dark_mode_button.click()
time.sleep(2)

# Scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
# Scroll up
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(3)

# Find the search input field by its class name
search_input = driver.find_element(By.CLASS_NAME, "ant-input.ant-input-lg")
# Input "python" into the search input field
search_input.send_keys("python")

# Find the search button by its class name and click it
search_button = driver.find_element(By.CLASS_NAME, "ant-btn.ant-btn-default.ant-btn-lg.ant-input-search-button")
search_button.click()
time.sleep(5)

# Open the specified URL
url = "https://www.geeksforgeeks.org/about/contact-us/?ref=outindfooter"
driver.get(url)
select_box = driver.find_element(By.NAME, "feedback_select")

select_box = driver.find_element(By.NAME, "feedback_select")
# Select "Feedback" from the dropdown
select_box.send_keys("Feedback")
time.sleep(2)

# Input the email into the text field
email_field = driver.find_element(By.NAME, "email")
email = "example@example.com"  # Replace with the email you want to input
email_field.send_keys(email)
time.sleep(2)

# Input the phone number into the text field
phone_field = driver.find_element(By.NAME, "feedback_number")
phone_number = "+251912349219"
phone_field.send_keys(phone_number)
time.sleep(3)

# Input some feedback into the feedback area
feedback_area = driver.find_element(By.NAME, "feedback_area")
feedback = "This is an automated feedback message."
feedback_area.send_keys(feedback)
time.sleep(2)

# Navigate back to the main page
main_url = "https://www.geeksforgeeks.org/"
driver.get(main_url)
time.sleep(5)


# Handle any alerts that may appear
try:
    alert = driver.switch_to.alert
    alert.accept()  # You can use alert.dismiss() if you want to dismiss the alert
    print("Alert handled successfully.")
except:
    print("No alert found.")


# Validate page title and URL after navigating back to the main page
expected_main_title = "GeeksforGeeks | A computer science portal for geeks"
expected_main_url = "https://www.geeksforgeeks.org/"
actual_main_title = driver.title
actual_main_url = driver.current_url
assert actual_main_title == expected_main_title, f"Main page title doesn't match. Expected: {expected_main_title}, Actual: {actual_main_title}"
assert actual_main_url == expected_main_url, f"Main page URL doesn't match. Expected: {expected_main_url}, Actual: {actual_main_url}"

