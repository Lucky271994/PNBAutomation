import time
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
    noReset='true',
    dontStopAppOnReset='true',
    newCommandTimeout= '300'

)

appium_server_url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
print("Session Started")

print("\n*******************  Checkbook Reorder with representative  *******************\n")

try:
    driver.implicitly_wait(10)
    print("Wait Dashboard to load")
    element = driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer')   

    driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"]').click()
    print("Tap Banking Services")

    driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"])[11]').click()
    print("Tap CheckBook Reorder")

    driver.find_element(AppiumBy.XPATH,'//androidx.cardview.widget.CardView[@resource-id="com.pnb.android.staging:id/checkingAccountContainer"]/android.view.ViewGroup').click()
    print("Select Checking Account")

    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.pnb.android.staging:id/checkBookQty"]').send_keys("1")
    print("Input Quantity")

    driver.find_element(AppiumBy.XPATH,'//android.widget.Switch[@resource-id="com.pnb.android.staging:id/switchAutorized"]').click()
    print("Switch Representative")

    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.pnb.android.staging:id/authorizeName"]').send_keys("Automation")
    print("Input Representative Name")

    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnContinue"]').click()
    print("Tap Continue")

    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="CONFIRM"]').click()
    print("Tap Confirm")

    #OTP Authentication
    otp_auth = simpledialog.askstring("Notice", "Enter your OTP:")
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtOTP"]').send_keys(otp_auth)
    print("Sendkey: OTP")

    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnConfirm"]').click()
    print("Tap Confirm")


    # Receipt Page
    driver.find_element(AppiumBy.XPATH, '//androidx.cardview.widget.CardView[@resource-id="com.pnb.android.staging:id/cvHome"]/android.widget.ImageView').click()
    print("Tap Back To Home")

except Exception as e:
    print(f"An error occurred: FAILED TO EXECUTE {e}")