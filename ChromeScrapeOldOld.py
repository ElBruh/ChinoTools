from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import codecs
import time

DRIVER_PATH = 'C:\Users\Eli\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.officeally.com/slogin.aspx')

login = driver.find_element_by_xpath("//input[@type='username']").send_keys('romaminc')
password = driver.find_element_by_xpath("//input[@type='password']").send_keys('Advancemedical$2021!^!')
submit = driver.find_element_by_xpath("//button[@ID='Login1_LoginButton']").click()

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "divMaintenance"))
    )
finally:
    window_name = driver.execute_script("return window.name")
    print(window_name)

    #exitButton = driver.find_element_by_name ('btnAcknowledge').click()

    #driver.execute_script("window.open('https://www.officeally.com/secure_oa.asp?GOTO=ClaimFix&TaskAction=Edit&Mode=Insert&FromIR=True&AllowCorrectedClaim=True&ClaimID=2480336207');")
#driver.get('https://www.officeally.com/secure_oa.asp?GOTO=ClaimFix&TaskAction=Edit&Mode=Insert&FromIR=True&AllowCorrectedClaim=True&ClaimID=2480336207')
#driver.

