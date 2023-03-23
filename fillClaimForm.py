from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pickle
import time
import tkinter as tk
from tkinter import filedialog, simpledialog
import os
import sys
import keyring
import zipfile
import platform
from urllib.request import urlretrieve
from packaging import version
#from ChromeScrape import DRIVER_PATH

#root = tk.Tk()
#root.withdraw()

def addPatientToOA():
    directory = sys.executable
    baseDir = os.path.dirname(directory)
    chrome_options = Options()

    try:
        DRIVER_PATH = baseDir + "\\src\\chromedriver.exe"
        chrome_options.add_argument("user-data-dir=C:\\src\\selenium") 
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=chrome_options)
        print("Prod Mode")
    except:
        DRIVER_PATH = "src/chromedriver.exe"
        chrome_options.add_argument("src/selenium") 
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=chrome_options)
        print("Testing Mode")

    driver.get('https://www.officeally.com/slogin.aspx')
    #driver.switch_to.frame("Iframe9")
    driver.find_element(By.ID, "Login1_UserName").send_keys('romaminc')
    driver.find_element(By.ID, "Login1_Password").send_keys('Advancemedical$2021!^!!')
    driver.find_element(By.ID, "Login1_LoginButton").click()
    #i = 1
    time.sleep(1)
    
    driver.get("https://www.officeally.com/secure_oa.asp?GOTO=OnlineEntry&TaskAction=Manage")
    driver.switch_to.frame("Iframe9")

    tablerows = driver.find_element(By.ID, "Table1").find_elements(By.TAG_NAME, "td")
    for i,  row in enumerate(tablerows):
        #print(i)
        #print(row.text)
        if(row.text == "Add" and i == 11):
            print(row)
            row.click()
    
    driver.find_element(By.ID, "INSURANCETYPE7").click()
    #windowsNames = driver.window_handles
    #driver.switch_to.window(windowsNames[-1])
    #driver.find_element(By.ID, "ctl03_popupBase_txtSearch").send_keys("Espinoza")
    #driver.find_element(By.NAME, "ctl03$popupBase$btnSearch").click()
    
def get_new_password():
    root = tk.Tk()
    root.withdraw()
    new_password = simpledialog.askstring("Password", "Enter your password:", show="*")
    return new_password
    
def login_to_website(driver):
    # Get the stored username and password
    username = "romaminc"
    stored_password = keyring.get_password("Create Patient Profile", username)
    #stored_password = "1232131"
    while True:
        # Navigate to the login page
        driver.get('https://www.officeally.com/slogin.aspx')

        # Enter the username and password
        driver.find_element(By.ID, "Login1_UserName").send_keys(username)
        driver.find_element(By.ID, "Login1_Password").send_keys(stored_password)
        driver.find_element(By.ID, "Login1_LoginButton").click()

        # Wait for the login process to complete
        time.sleep(1)

        # Check if the login was successful
        if driver.current_url != 'https://www.officeally.com/slogin.aspx':
            break
        else:
            # If the login failed, prompt the user for the password and try again
            print("Login failed. Please enter the correct password for OfficeAlly user romaminc.")
            stored_password = get_new_password()
            # Update the stored password
            keyring.set_password("Create Patient Profile", username, stored_password)



def fillClaimFormFunction(b):
    diagnosisPointers = "A"
    print(b['patientFirstName'])

    directory = sys.executable
    baseDir = os.path.dirname(directory)
    chrome_options = Options()

    try:
        DRIVER_PATH = os.path.join(baseDir, "src", "chromedriver.exe")
        chrome_options.add_argument("user-data-dir=C:\\src\\selenium") 
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
        print("Prod Mode")
    except:
        DRIVER_PATH = os.path.join("src", "chromedriver.exe")
        chrome_options.add_argument("src/selenium") 
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
        print("Testing Mode")

    login_to_website(driver)
    driver.get('https://www.officeally.com/secure_oa.asp?GOTO=onlineentry&TaskAction=Edit&Mode=Create&ClaimID=-1&encounter=&CMS=0212&sPatient=-1&sBillProv=1415905&sRndProv=1344022&sFacility=-1&sTemplate=-1&sPayer=1892359')
    time.sleep(1)
    driver.switch_to.frame("Iframe9")

    if(b['account'] == "Medicare"):
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_INSURANCETYPE1").click()
    else:
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_INSURANCETYPE7").click()


    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_LAST_NAME').send_keys(b["patientLastName"])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_FIRST_NAME').send_keys(b["patientFirstName"])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PRI_PATIENT_ID').send_keys(b['patientMBI'])    
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PATIENT_BIRTHDATE_Month').send_keys(b['patientDateOfBirth'].partition("/")[0])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PATIENT_BIRTHDATE_Day').send_keys(b['patientDateOfBirth'].partition("/")[2].partition("/")[0])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PATIENT_BIRTHDATE_Year').send_keys(b['patientDateOfBirth'].partition("/")[2].partition("/")[2])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_STREET_ADDR').send_keys(b["patientAddress"])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_CITY').send_keys(b["patientCity"])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_STATE').send_keys(b["patientState"])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_ZIP').send_keys(b['patientZip'])    
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PHONE_AreaCode').send_keys(b['patientPhone'].partition("-")[0])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PHONE_Prefix').send_keys(b['patientPhone'].partition("-")[2].partition("-")[0])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PHONE_Number').send_keys(b['patientPhone'].partition("-")[2].partition("-")[2])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_GENDER").send_keys(b['patientGender'])

    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Month").send_keys(b['patientOrderDate'].partition("/")[0])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Day").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Year").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_OrderFirst0212').send_keys(b["patientPCPFirstName"])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_OrderLast0212').send_keys(b["patientPCPLastName"])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_REFER_PHYSICIAN_NPI').send_keys(b["patientPCPNPI"])
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_selReferringProviderQual').send_keys("DK - Ordering Provider")

    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Month").clear()
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Day").clear()
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Year").clear()
    
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Month").send_keys(b['patientOrderDate'].partition("/")[0])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Day").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Year").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PRIOR_AUTH_NUMBER').send_keys(b["patientPreauthorization"])

    



    if(b["diagnosisCodeRow2"] != ""):
        diagnosisPointers = "AB"
        #print("AB")
        if(b["diagnosisCodeRow3"] != ""):
            diagnosisPointers = "ABC"
            #print("ABC")
            if(b["diagnosisCodeRow4"] != ""):
                diagnosisPointers = "ABCD"
                #print("ABCD")
            
        
    
    
    
    print(diagnosisPointers)

    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_DIAGNOSIS_CODECMS0212_1").send_keys(b["diagnosisCodeRow1"])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_DIAGNOSIS_CODECMS0212_2").send_keys(b["diagnosisCodeRow2"])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_DIAGNOSIS_CODECMS0212_3").send_keys(b["diagnosisCodeRow3"])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_DIAGNOSIS_CODECMS0212_4").send_keys(b["diagnosisCodeRow4"])

    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_MONTH0").send_keys(b['patientOrderDate'].partition("/")[0])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_DAY0").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_YEAR0").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_MONTH0").send_keys(b['patientOrderDate'].partition("/")[0])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_DAY0").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_YEAR0").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_CPT_CODE0").send_keys(b["itemRow1CPT"])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_PLACE_OF_SVC0").send_keys("12")
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_A0").send_keys(b["itemRow1Modifier1"])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_B0").send_keys(b["itemRow1Modifier2"])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_C0").send_keys(b["itemRow1Modifier3"])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_D0").send_keys(b["itemRow1Modifier4"])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_DIAG_CODE0").send_keys(diagnosisPointers)
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_CHRG0").send_keys(b["itemRow1Price"])
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_UNITS0").send_keys(b["itemRow1Qty"])

    if(b["itemRow2CPT"] != ""):
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_MONTH1").send_keys(b['patientOrderDate'].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_DAY1").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_YEAR1").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_MONTH1").send_keys(b['patientOrderDate'].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_DAY1").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_YEAR1").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])
        
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_CPT_CODE1").send_keys(b["itemRow2CPT"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_PLACE_OF_SVC1").send_keys("12")
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_A1").send_keys(b["itemRow2Modifier1"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_B1").send_keys(b["itemRow2Modifier2"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_C1").send_keys(b["itemRow2Modifier3"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_D1").send_keys(b["itemRow2Modifier4"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_DIAG_CODE1").send_keys(diagnosisPointers)
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_CHRG1").send_keys(b["itemRow2Price"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_UNITS1").send_keys(b["itemRow2Qty"])

    if(b["itemRow3CPT"] != ""):
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_MONTH2").send_keys(b['patientOrderDate'].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_DAY2").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_YEAR2").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_MONTH2").send_keys(b['patientOrderDate'].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_DAY2").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_YEAR2").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])
        
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_CPT_CODE2").send_keys(b["itemRow3CPT"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_PLACE_OF_SVC2").send_keys("12")
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_A2").send_keys(b["itemRow3Modifier1"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_B2").send_keys(b["itemRow3Modifier2"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_C2").send_keys(b["itemRow3Modifier3"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_D2").send_keys(b["itemRow3Modifier4"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_DIAG_CODE2").send_keys(diagnosisPointers)
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_CHRG2").send_keys(b["itemRow3Price"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_UNITS2").send_keys(b["itemRow3Qty"])

    if(b["itemRow4CPT"] != ""):
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_MONTH3").send_keys(b['patientOrderDate'].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_DAY3").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_YEAR3").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_MONTH3").send_keys(b['patientOrderDate'].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_DAY3").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_YEAR3").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_CPT_CODE3").send_keys(b["itemRow4CPT"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_PLACE_OF_SVC3").send_keys("12")
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_A3").send_keys(b["itemRow4Modifier1"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_B3").send_keys(b["itemRow4Modifier2"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_C3").send_keys(b["itemRow4Modifier3"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_D3").send_keys(b["itemRow4Modifier4"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_DIAG_CODE3").send_keys(diagnosisPointers)
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_CHRG3").send_keys(b["itemRow4Price"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_UNITS3").send_keys(b["itemRow4Qty"])

    if(b["itemRow5CPT"] != ""):
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_MONTH4").send_keys(b['patientOrderDate'].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_DAY4").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_YEAR4").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_MONTH4").send_keys(b['patientOrderDate'].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_DAY4").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_YEAR4").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_CPT_CODE4").send_keys(b["itemRow5CPT"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_PLACE_OF_SVC4").send_keys("12")
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_A4").send_keys(b["itemRow5Modifier1"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_B4").send_keys(b["itemRow5Modifier2"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_C4").send_keys(b["itemRow5Modifier3"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_D4").send_keys(b["itemRow5Modifier4"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_DIAG_CODE4").send_keys(diagnosisPointers)
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_CHRG4").send_keys(b["itemRow5Price"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_UNITS4").send_keys(b["itemRow5Qty"])

    if(b["itemRow6CPT"] != ""):
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_MONTH5").send_keys(b['patientOrderDate'].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_DAY5").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_FM_DATE_OF_SVC_YEAR5").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_MONTH5").send_keys(b['patientOrderDate'].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_DAY5").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[0])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_TO_DATE_OF_SVC_YEAR5").send_keys(b['patientOrderDate'].partition("/")[2].partition("/")[2])

        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_CPT_CODE5").send_keys(b["itemRow6CPT"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_PLACE_OF_SVC5").send_keys("12")
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_A5").send_keys(b["itemRow6Modifier1"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_B5").send_keys(b["itemRow6Modifier2"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_C5").send_keys(b["itemRow6Modifier3"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_D5").send_keys(b["itemRow6Modifier4"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_DIAG_CODE5").send_keys(diagnosisPointers)
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_DOS_CHRG5").send_keys(b["itemRow6Price"])
        driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_UNITS5").send_keys(b["itemRow6Qty"])


    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_PNT_COND_FRM_EMPL2").click()
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_PNT_COND_FRM_AUTO2").click()
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_PNT_COND_FRM_OTR2").click()
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_PNT_REL_TO_INSRD1").click()
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_OUTSIDE_LAB2").click()
    driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ACCEPT_SIGNATURE1").click()
    driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PRI_FECA_GRP_NUM').send_keys("None")


    driver.find_element(By.ID, "lnkPatientCopy").click()

def get_chrome_version():
    if platform.system() == "Windows":
        command = "reg query \"HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon\" /v version"
    elif platform.system() == "Darwin":
        command = "/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --version"
    else:
        command = "google-chrome --version"

    output = os.popen(command).read().strip()
    chrome_version = output.split()[-1].decode('utf-8') if platform.system() == "Darwin" else output.split()[-1]
    return version.parse(chrome_version)

def get_chromedriver_version(chrome_version):
    major_version = chrome_version.release[0]
    chromedriver_url = f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{major_version}"
    chromedriver_version = os.popen(f"curl {chromedriver_url}").read().strip()
    return version.parse(chromedriver_version)

def download_chromedriver(chromedriver_version, driver_directory):
    url = f"https://chromedriver.storage.googleapis.com/{chromedriver_version}/chromedriver_win32.zip" if platform.system() == "Windows" else f"https://chromedriver.storage.googleapis.com/{chromedriver_version}/chromedriver_mac64.zip"
    zip_path = os.path.join(driver_directory, "chromedriver.zip")
    urlretrieve(url, zip_path)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(driver_directory)

    os.remove(zip_path)
    os.chmod(os.path.join(driver_directory, "chromedriver"), 0o755)

def check_and_download_chromedriver(driver_directory):
    chrome_version = get_chrome_version()
    chromedriver_version = get_chromedriver_version(chrome_version)

    chromedriver_path = driver_directory

    if os.path.exists(chromedriver_path):
        try:
            current_chromedriver_version_output = os.popen(f"{chromedriver_path} --version").read().strip()
            current_chromedriver_version = version.parse(current_chromedriver_version_output.split()[1])
        except Exception as e:
            print(f"Error getting current ChromeDriver version: {e}")
            current_chromedriver_version = None

        if current_chromedriver_version != chromedriver_version:
            print(f"Updating ChromeDriver from {current_chromedriver_version} to {chromedriver_version}")
            download_chromedriver(chromedriver_version, driver_directory)
    else:
        print(f"Downloading ChromeDriver {chromedriver_version}")
        download_chromedriver(chromedriver_version, driver_directory)

    return chromedriver_path

directory = sys.executable
baseDir = os.path.dirname(directory)
chrome_options = Options()

try:
    DRIVER_PATH = os.path.join(baseDir, "src", "chromedriver.exe")
    print("Prod Mode")
except:
    DRIVER_PATH = os.path.join("src", "chromedriver.exe")
    print("Testing Mode")
driver_directory = DRIVER_PATH
#os.makedirs(driver_directory, exist_ok=True)

chromedriver_path = check_and_download_chromedriver(driver_directory)
#fillClaimFormFunction({"patientFirstName":"Bruh"})
#addPatientToOA()

#DOSMonth = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Month').send_keys('value')
#DOSDay = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Day').send_keys('value')
#DOSYear = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Year').send_keys('value')