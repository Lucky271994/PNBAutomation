import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define desired capabilities
capabilities = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'D6HQXGN7BATODIPF',  # Replace with your actual device name/ID
    'appPackage': 'com.pnb.android.staging',
    'appActivity': 'com.pnb.android.ui.splash.SplashActivity',
    'noReset': 'true',
    'dontStopAppOnReset': 'true',
    'newCommandTimeout': '300'
}

appium_server_url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
print("Session Started")

print("\n*******************  Add/Remove Services  *******************\n")

def long_press_element(by, value, duration=2000, max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
        try:
            # Wait for element to be visible before interacting
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((by, value))
            )
            print(f"Found element: Performing long press")
            
            # Create an ActionChains object for W3C Actions
            actions = ActionChains(driver)
            actions.click_and_hold(element).pause(duration / 1000.0).release().perform()
            return element
        except Exception as e:
            print(f"Element not found or error: {str(e)}")
            attempts += 1
            print(f"Retrying... Attempt {attempts} of {max_attempts}")

    print(f"Failed to find or perform action on element: {value} after {max_attempts} attempts.")
    raise Exception(f"Failed to find element: {value} after {max_attempts} attempts.")

try:
    driver.implicitly_wait(10)
    print("Wait Dashboard to load")
    element = driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')   

    # Add Services
    print("Add Service 1")
    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence1"])[2]').click()
    print("Tap Add Services")

    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"])[1]').click()
    print("Tap Services to add")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ADD"]').click()
    print("Tap Add")

    # Add Services
    print("Add Service 2")
    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence2"])[2]').click()
    print("Tap Add Services")

    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"])[1]').click()
    print("Tap Services to add")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ADD"]').click()
    print("Tap Add")

    # Add Services
    print("Add Service 3")
    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence3"])[2]').click()
    print("Tap Add Services")

    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"])[1]').click()
    print("Tap Services to add")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ADD"]').click()
    print("Tap Add")

  # Add Services
    print("Add Service 4")
    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence4"])[2]').click()
    print("Tap Add Services")

    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"])[1]').click()
    print("Tap Services to add")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ADD"]').click()
    print("Tap Add")

    # Add Services
    print("Add Service 5")
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence5"]').click()
    print("Tap Add Services")

    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"])[1]').click()
    print("Tap Services to add")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ADD"]').click()
    print("Tap Add")

    # Add Services
    print("Add Service 6")
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence6"]').click()
    print("Tap Add Services")

    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"])[1]').click()
    print("Tap Services to add")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ADD"]').click()
    print("Tap Add")

    # Add Services
    print("Add Service 7")
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence7"]').click()
    print("Tap Add Services")

    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"])[1]').click()
    print("Tap Services to add")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ADD"]').click()
    print("Tap Add")







    # Remove Banking Services
    print("Wait Dashboard to load")
    driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')

    # Perform the long press
    long_press_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence1"])[2]')
    print("Long Tap on Banking Service")

    # Remove the service
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnCloseSequence1"]').click()
    print("Tap X to Remove 1")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="DELETE"]').click()
    print("Tap Delete")

    # Remove Banking Services
    print("Wait Dashboard to load")
    driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')

    # Perform the long press
    long_press_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence2"])[2]')
    print("Long Tap on Banking Service")

    # Remove the service
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnCloseSequence2"]').click()
    print("Tap X to Remove 1")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="DELETE"]').click()
    print("Tap Delete")

    # Remove Banking Services
    print("Wait Dashboard to load")
    driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')

    # Perform the long press
    long_press_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence3"])[2]')
    print("Long Tap on Banking Service")

    # Remove the service
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnCloseSequence3"]').click()
    print("Tap X to Remove 1")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="DELETE"]').click()
    print("Tap Delete")

        # Remove Banking Services
    print("Wait Dashboard to load")
    driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')

    # Perform the long press
    long_press_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence4"])[2]')
    print("Long Tap on Banking Service")

    # Remove the service
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnCloseSequence4"]').click()
    print("Tap X to Remove 1")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="DELETE"]').click()
    print("Tap Delete")

        # Remove Banking Services
    print("Wait Dashboard to load")
    driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')

    # Perform the long press
    long_press_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence5"]')
    print("Long Tap on Banking Service")

    # Remove the service
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnCloseSequence5"]').click()
    print("Tap X to Remove 1")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="DELETE"]').click()
    print("Tap Delete")

        # Remove Banking Services
    print("Wait Dashboard to load")
    driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')

    # Perform the long press
    long_press_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence6"]')
    print("Long Tap on Banking Service")

    # Remove the service
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnCloseSequence6"]').click()
    print("Tap X to Remove 1")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="DELETE"]').click()
    print("Tap Delete")

        # Remove Banking Services
    print("Wait Dashboard to load")
    driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')

    # Perform the long press
    long_press_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnSequence7"]')
    print("Long Tap on Banking Service")

    # Remove the service
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnCloseSequence7"]').click()
    print("Tap X to Remove 1")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="DELETE"]').click()
    print("Tap Delete")



except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()
