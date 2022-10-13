from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle
import time
import tkinter as tk
from tkinter import filedialog
import os
import sys
#from ChromeScrape import DRIVER_PATH

#root = tk.Tk()
#root.withdraw()


def fillClaimFormFunction(b):
    print(b)
    #fileOfIds = filedialog.askopenfilename(filetypes=[("Pickle Data Files", ".pickle")])
    #with open(fileOfIds, 'rb') as handle:
    #    b = pickle.load(handle)
    #fileOfIds = open("TestMedicareClaims.txt", "r")
    #fileOfIds = open("IEHPCLAIMS.txt", "r")
    print(b['patientFirstName'])



    #DRIVER_PATH = 'C:\\Users\\ValleyCareGG\\Downloads\\chromedriver_win32\\chromedriver.exe'
    #DRIVER_PATH = 'C:\\Users\\Eli\\Downloads\\chromedriver_win32\\chromedriver.exe'
    #DRIVER_PATH = 'C:\\Users\\Bruh\\Downloads\\chromedriver_win32\\chromedriver.exe'
    #DRIVER_PATH = ".\\src\\chromedriver.exe"
    
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
    #print(DRIVER_PATH)

    
    
    #chrome_options.add_argument("user-data-dir=C:\\Src\\ChinoTools\\selenium") 
    #chrome_options.add_argument("user-data-dir=C:{}\\selenium".format(baseDir))
    
    #chrome_options.add_argument("executable_path={}".format(DRIVER_PATH))
    #driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=chrome_options)

    #driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get('https://www.officeally.com/slogin.aspx')
    #driver.switch_to.frame("Iframe9")
    driver.find_element(By.ID, "Login1_UserName").send_keys('romaminc')
    driver.find_element(By.ID, "Login1_Password").send_keys('Advancemedical$2021!^!!^!')
    driver.find_element(By.ID, "Login1_LoginButton").click()
    #i = 1
    time.sleep(1)
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




#DOSMonth = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Month').send_keys('value')
#DOSDay = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Day').send_keys('value')
#DOSYear = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_P_SIG_ON_FILE_DATE_Year').send_keys('value')