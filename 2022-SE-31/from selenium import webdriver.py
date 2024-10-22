from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import capsolver
import time
import requests
import base64
import json

# Replace with your CAPTCHA API key
CAPTCHA_API_KEY = 'CAP-E566FA9080CBE68130FF01DB1166C469'


# Step 1: Set up the Chrome driver
def fill_form_and_solve_captcha():
    
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_argument("start-maximized")
    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")
    options.add_argument("window-size=1920x1080")



    s = Service(executable_path="C:\\Windows\\chromedriver.exe")

    # Set up Chrome WebDriver using WebDriver Manager
    driver = webdriver.Chrome(service=s,options=options)
    # driver = webdriver.Chrome()


    # Navigate to the website form
    driver.get("https://www.g4k.go.kr/en/main.do")
    
    
    goForLogin = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "login"))
        )
    goForLogin.click()

    label = driver.find_element(By.CSS_SELECTOR, "label[for='chkAll']")
    label.click()

    # Step 2: Fill out form details
    name_input = driver.find_element(By.ID, "mberNm")
    name_input.send_keys("Akram")

    email_input = driver.find_element(By.ID, "emailId")
    email_input.send_keys("akram")

    mail_service_provider = driver.find_element(By.ID, "emailChoise")
    mail_service_provider.click()
    select_mail_provider = driver.find_element(By.XPATH, "//option[text()='gmail.com']")
    select_mail_provider.click()

    # Step 2.3: Select country code by scrolling (e.g., select by visible text)
    country_dropdown = driver.find_element(By.ID, "mberTelFg")
    country_dropdown.click()
    option = driver.find_element(By.XPATH, "//option[text()='Nepal(977)']")
    option.click()

    # Step 2.4: Place the number
    phone_input = driver.find_element(By.ID, "smsNo")
    phone_input.send_keys("1234567890")

    # Wait for the page to load
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "captchaSms")))

    # Step 4: Download the CAPTCHA image
    captcha_img = driver.find_element(By.ID, "captchaSms")
    captcha_url = captcha_img.get_attribute('src')

    # Download the CAPTCHA image
    print("This line is running")
    captcha_response = requests.get(f'https://consul.mofa.go.kr/{captcha_url}')

    
    with open("captcha_image.png", 'wb') as file:
        file.write(captcha_response.content)

    
    # Step 5: Solve the CAPTCHA using the CapSolver API
    captcha_solution = solve_captcha('captcha_image.png')
    print("This line is running")

    # Step 6: Enter CAPTCHA and Submit the Form
    captcha_input = driver.find_element(By.NAME, 'captchaInput')
    captcha_input.send_keys(captcha_solution)

    # Step 3: Accept Terms and Conditions
    # driver.find_element(By.XPATH, "//label[@for='agreeAll']").click()
    # driver.find_element(By.XPATH, "//label[@for='termsCheck']").click()
    # driver.find_element(By.XPATH, "//label[@for='personalInfoCheck']").click()
   



    # Step 5: Handle CAPTCHA
    captcha_img = driver.find_element(By.ID, "captchaSms")
    captcha_url = captcha_img.get_attribute('src')

    # Download the CAPTCHA image
    # captcha_response = requests.get(f'https://consul.mofa.go.kr/{captcha_url}')
    # with open("captcha_image.png", 'wb') as file:
    #     file.write(captcha_response.content)

    # # Solve the CAPTCHA using the CapSolver API
    # captcha_solution = solve_captcha('captcha_image.png')

    # # Step 6: Enter CAPTCHA and Submit the Form
    # captcha_input = driver.find_element(By.NAME, 'captchaInput')
    # captcha_input.send_keys(captcha_solution)

    # Click 'Send Verification Number'
    driver.find_element(By.XPATH, "//button[text()='Send Verification Number']").click()

    get_code_button = driver.find_element(By.ID, "crtfKeyNoBtn")
    get_code_button.click()
    
    print("Form submitted successfully!")
    time.sleep(5)
    driver.quit()


# def solve_captcha(image_path):
#     # This function uses the CapSolver API to solve the CAPTCHA
#     url = "https://api.capsolver.com/solve"
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     payload = {
#         "clientKey": CAPTCHA_API_KEY,
#         "task": {
#             "type": "ImageToTextTask",
#             "body": image_path  # Captcha image
#         }
#     }

#     response = requests.post(url, json=payload, headers=headers)
#     result = response.json()

#     if 'solution' in result and 'text' in result['solution']:
#         return result['solution']['text']
#     else:
#         raise Exception("Captcha could not be solved.")



def solve_captcha(image_path):
    # This function uses the CapSolver API to solve the CAPTCHA
    url = "https://api.capsolver.com/createTask"
    headers = {
        'Content-Type': 'application/json'
    }
    print('Line 1 inside solve capcha running')
    # Read the image file and encode it as base64
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    print('Line 2 inside solve capcha running')

    payload = {
        "clientKey": CAPTCHA_API_KEY,
        "task": {
            "type": "ImageToTextTask",
            "body": image_data  # Base64-encoded image data
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    # Check for successful response
    try:
        result = response.json()
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON response: {e}\nResponse text: {response.text}")

    # Handle response from API
    if 'solution' in result and 'text' in result['solution']:
        return result['solution']['text']
    else:
        raise Exception(f"Captcha could not be solved. API Response: {result}")


# Execute the automation
fill_form_and_solve_captcha()