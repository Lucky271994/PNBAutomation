import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Define desired capabilities
capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',  
    deviceName='D6HQXGN7BATODIPF',  # Replace with your actual device name/ID
    appPackage='com.pnb.android.staging',
    appActivity='com.pnb.android.ui.splash.SplashActivity',
    noReset='true',
    dontStopAppOnReset='true',
)

appium_server_url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
print("Session Started")

print("\n*******************  Cardless Withdrawal  *******************\n")

try:

    driver.implicitly_wait(15)

    # initialize Cardless Wothdrawal

    print("Wait Dashboard to load")  
    element = driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer') 

    driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"]').click()
    print("Tap Banking Services")

    driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"])[15]').click()
    print("Tap Cardless Withdrawal")

    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.pnb.android.staging:id/txtAmount"]').send_keys("100")
    print("Input Amount")
    
    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnContinue"]').click()
    print("Tap Continue")

    # Confirm Page

    print("Screen Validation")

    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.pnb.android.staging:id/toolbarTitle"]')
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.pnb.android.staging:id/lblSource"]')
    driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView')
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.pnb.android.staging:id/txtSourceAccountName"]')
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.pnb.android.staging:id/txtSourceAccountNumber"]')
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.pnb.android.staging:id/lblAmount"]')
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.pnb.android.staging:id/txtAmount"]')
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.pnb.android.staging:id/lblDisclaimer"]')
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.pnb.android.staging:id/txtDisclaimer"]')

    print("Screen Validation: Pass")

    time.sleep(10)
    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnContinue"]').click()
    print("Confirm and Tap Continue")

    # MFA Page
    driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.pnb.android.staging:id/map"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.ImageView')
    print("Wait for Map Location to load")

    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnAccept"]').click()
    print("MFA Accepted")

    driver.find_element(AppiumBy.XPATH,'//androidx.cardview.widget.CardView[@resource-id="com.pnb.android.staging:id/cvHome"]/android.widget.ImageView').click()
    print("Tap Back to Home")

    # Cancel Cardless Widrawal

    print("Wait Dashboard to load")  
    element = driver.find_element(AppiumBy.ID, 'com.pnb.android.staging:id/bankingServicesContainer') 

    driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"]').click()
    print("Tap Banking Services")

    driver.find_element(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/imgBankingServices"])[15]').click()
    print("Tap Cardless Withdrawal")

    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.pnb.android.staging:id/btnCancel"]').click()
    print("Tap Cancel")

    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="YES"]').click()
    print("Tap Yes")
    
    driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.pnb.android.staging:id/toolbarBack"]').click()
    print("Tap Back")

    driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView[@resource-id="com.pnb.android.staging:id/nestedScrollView"]/android.view.ViewGroup/android.widget.ImageView[1]').click()
    print("Tap Back to Home")

except Exception as e:
    print(f"An error occurred: FAILED TO EXECUTE {e}")
