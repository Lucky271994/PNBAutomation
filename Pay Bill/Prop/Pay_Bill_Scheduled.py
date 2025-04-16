
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import tkinter as tk
from tkinter import simpledialog
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define desired capabilities
capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',  
    deviceName='D6HQXGN7BATODIPF',  # Replace with your actual device name/ID
    appPackage='com.pnb.android.staging',
    appActivity='com.pnb.android.ui.splash.SplashActivity',
    noReset='true',
    dontStopAppOnReset='true',
    newCommandTimeout= '300'

)

appium_server_url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
print(f"Session Capabilities: {driver.capabilities}")

print("\n*******************  Pay Bill Regular  *******************\n")

# Helper function to scroll using UiScrollable and find element without coordinates
def scroll_down_and_find_element(by, value, max_attempts=5):
    attempts = 0
    while attempts < max_attempts:
        try:
            # Attempt to find the element directly without scrolling
            element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((by, value))  # Wait for visibility, not just presence
            )
            print(f"Found element: Continue Execution")
            return element
        except Exception as e:
            print(f"Element not found in the visible area. Attempting to scroll down...")

            # Use UiScrollable to scroll down until the element is found
            try:
                # UiScrollable scroll command (scrollForward/scrollBackward)
                scroll_command = f'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_command)
                print(f"Scrolled down to find element")
            except Exception as swipe_error:
                print(f"Swipe failed: {str(swipe_error)}")

            attempts += 1

    print(f"Failed to find element: {value} after {max_attempts} attempts.")
    raise Exception(f"Failed to find element: {value} after {max_attempts} attempts.")

try:

    driver.implicitly_wait(10)

    # Initialize Testing
    element = scroll_down_and_find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')
    print("Wait for Dashboard")
   
    driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/navigation_bar_item_icon_view"])[4]').click()
    print("Tap Pay Bill")

    time.sleep(5)
    driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnConfigView"]').click()
    print("Tap Grid View")

    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtSearchBiller"]').click()
    print("Tap Search Biller")

    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtSearchBiller"]').send_keys("Globe")
    print("Sendkey: Biller")
    
    driver.find_element(AppiumBy.XPATH,'(//androidx.appcompat.widget.LinearLayoutCompat[@resource-id="com.pnb.android.staging:id/billerContainer"])[1]').click()
    print("Tap Searched Biller")

    # Input
    scroll_down_and_find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnContinue"]')
    
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtInputNumberField"]').send_keys("1082104221")
    print("Sendkey: Account Number")

    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtInputAmountField"]').send_keys("1.02")
    print("Sendkey: Amount")

    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtInputDateField"]').send_keys("03 Apr 2026")    
    print("Sendkey: Scheduled Date")

    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtInputTextField"]').send_keys("Automation")
    print("Sendkey: Purpose")

    scroll_down_and_find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnContinue"]').click()
    print("Tap Continue")

    # Confirm Page
    scroll_down_and_find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnConfirm"]').click()
    print("Tap Continue to confirm")

    # MFA Page
    driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.pnb.android.staging:id/map"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ImageView')

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnApprove"]').click()
    print("MFA Accept")

    # Receipt Page
    scroll_down_and_find_element(AppiumBy.XPATH, '//androidx.cardview.widget.CardView[@resource-id="com.pnb.android.staging:id/cvHome"]/android.widget.ImageView').click()
    print("Back to Home")

except Exception as e:
    print(f"An error occurred: FAILED TO EXECUTE: {str(e)}")

