from appium import webdriver
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
import openpyxl

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

print("\n*******************  ---------------- *******************\n")

# Create an Excel workbook and sheet
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Extracted Elements"
sheet.append(["Text", "Generated XPath"])  # Header row

try:
    # Wait for the app to load
    driver.implicitly_wait(10)

    # Locate all elements that have text attributes
    elements_with_text = driver.find_elements(By.XPATH, "//*[@text]")

    # Scan, print, and save text along with their dynamically generated XPath
    for element in elements_with_text:
        text = element.text
        class_name = element.get_attribute("className")  # Retrieve class name
        resource_id = element.get_attribute("resourceId")  # Retrieve resource ID

        # Construct an XPath dynamically based on available attributes
        xpath_parts = []
        if class_name:
            xpath_parts.append(f"//{class_name}")
        if text:
            xpath_parts.append(f"[@text='{text}']")
        if resource_id:
            xpath_parts.append(f"[@resource-id='{resource_id}']")

        generated_xpath = "".join(xpath_parts) if xpath_parts else "Not Available"

        print(f"Text: {text}, Generated XPath: {generated_xpath}")
        sheet.append([text, generated_xpath])

    # Save the Excel file
    excel_filename = "extracted_elements.xlsx"
    workbook.save(excel_filename)
    print(f"\nData saved to {excel_filename}")

finally:
    # Close the Appium driver
    driver.quit()