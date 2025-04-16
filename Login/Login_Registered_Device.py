from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import tkinter as tk
from tkinter import simpledialog


# Define desired capabilities
capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',  
    deviceName='D6HQXGN7BATODIPF',  # Replace with your actual device name/ID
    appPackage='com.pnb.android.staging',
    appActivity='com.pnb.android.ui.splash.SplashActivity',
    noReset='false',
    dontStopAppOnReset='true',
)

appium_server_url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
print("Session Started")

print("\n*******************  Login Registed Device  *******************\n")

# Without Splash Screen
try:
    driver.implicitly_wait(10)
    print("Wait Dashboard to load")
    element = driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')   
    print("Tap Home Module")
    element = driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/navigation_bar_item_icon_view"])[1]').click()
except Exception:
        pass  # Proceed 

# With Splash Screen
try:
    driver.implicitly_wait(5)   
    element = driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/txtClose')
    element.click()
except Exception:
        pass  # Proceed if the element is not found

try:
    # Initialize Testing

    print("Select Password Authernication")
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.pnb.android.staging:id/design_bottom_sheet"]/androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat[3]/androidx.cardview.widget.CardView/android.widget.ImageView').click()
   
    print("SendKey: Password")

    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring("Notice", "Enter your password:")

    element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtPassword"]').send_keys(user_input)

    print('Tap Unmask Password')
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Show password"]').click()

    print('Tap Confirm CTA')
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="CONFIRM"]').click()    

    print("Validate Logout CTA Exist")
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/btnLogout"]')

except Exception as e:
    print(f"An error occurred: FAILED TO EXECUTE {e}")