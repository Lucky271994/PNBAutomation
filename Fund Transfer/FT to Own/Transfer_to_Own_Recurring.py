import time
from tkinter import simpledialog
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define desired capabilities
capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    deviceName='D6HQXGN7BATODIPF',
    appPackage='com.pnb.android.staging',
    appActivity='com.pnb.android.ui.splash.SplashActivity',
    noReset='true',
    newCommandTimeout= '300'

)

appium_server_url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
print("Session Started")

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

    print("\n*******************  Transfer to Own Recurring  *******************\n")

    driver.implicitly_wait(10)

    # Initialize Testing
    element = scroll_down_and_find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')
    print("Wait for Dashboard")

    driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/navigation_bar_item_icon_view"])[3]').click()
    print("Tap Transfer tab")

    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgOwnPNB"]').click()
    print("Tap Own PNB")

    driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.pnb.android.staging:id/destinationList"]').click()
    print("Select Destination")




    # Input Page
    btnContinue = scroll_down_and_find_element(AppiumBy.ID, "com.pnb.android.staging:id/btnContinue")

    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtAmount"]').send_keys("1.02")
    print("Send Key: 1.02")

    driver.find_element(AppiumBy.XPATH,'//android.widget.Switch[@resource-id="com.pnb.android.staging:id/switchRepeat"]').click()

    driver.find_element(AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.pnb.android.staging:id/txtFrequency"]').send_keys("Daily")

    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtStartDate"]').send_keys("05 Apr 2026")

    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtEndDate"]').send_keys("06 Apr 2026")

    btnContinue = scroll_down_and_find_element(AppiumBy.ID, "com.pnb.android.staging:id/btnContinue")

    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtPurpose"]').send_keys("Automation")
    print("Send Key: Automation")

    btnContinue.click()
    print("Tap Continue")


    # Confirm Page
    time.sleep(3)
    scroll_down_and_find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnContinue"]').click()
    print("Tap Continue to confirm")


    # MFA / OTP Auth
    otp_auth = simpledialog.askstring("Notice", "Enter your OTP:")

    if otp_auth:
        driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtOTP"]').send_keys(otp_auth)
        print("Sendkey: OTP")

        driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnConfirm"]').click()
        print("Tap Confirm")

    else:
        driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.pnb.android.staging:id/map"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ImageView').click()
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnAccept"]').click()
        print("MFA Accepted")



# Receipt Page
    scroll_down_and_find_element(AppiumBy.XPATH, '//androidx.cardview.widget.CardView[@resource-id="com.pnb.android.staging:id/cvHome"]')
    time.sleep(3)
    print("Tap back to Home")
    driver.find_element(AppiumBy.XPATH, '//androidx.cardview.widget.CardView[@resource-id="com.pnb.android.staging:id/cvHome"]/android.widget.ImageView').click()
  

except Exception as e:
    print(f"An error occurred: FAILED TO EXECUTE: {str(e)}")
