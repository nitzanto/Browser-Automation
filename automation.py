from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Setting up the Chrome driver service and also the options
service = Service(executable_path='./chromedriver')
chrome_opts = Options()
chrome_opts.add_experimental_option("detach", True)  # Keeping the instance open to see the results
chrome_browser = webdriver.Chrome(service=service, options=chrome_opts)

# Maximize window and open demo page
chrome_browser.maximize_window()
chrome_browser.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')

# Checking if the page title contains expected text using an assertion
assert 'Selenium Easy Demo' in chrome_browser.title

# Finding the button element by class name and get button text
button = chrome_browser.find_elements(By.CLASS_NAME, 'btn-primary')
button_text = button[0].text

# Checking if the page source contains expected text using an assertion
assert 'Show Message' in chrome_browser.page_source
print(button_text)

# Find input element by ID and send some text as input
user_message = chrome_browser.find_elements(By.ID, 'user-message')
user_message[0].clear()  # To clear the input of there's any
user_message[0].send_keys('Testing automation :)')

# Click the button to send the message
button[0].click()

# Wait for output message to appear and get its text
output_message = chrome_browser.find_elements(By.ID, 'display')

# Print the output message and check if it contains expected text using an assertion
print(f'The output of what you entered was: {output_message[0].text}')
assert 'Testing automation :)' in output_message[0].text

print('All done!')
