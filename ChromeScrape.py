from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle
import time

fileOfIds = open("./TXTx/TestMedicareClaims.txt", "r")
#fileOfIds = open("IEHPCLAIMS.txt", "r")
ids = []
patientList = []
skipped_count = 0
for lines in fileOfIds:
    ids.append(int(lines))


#DRIVER_PATH = 'C:\\Users\\ValleyCareGG\\Downloads\\chromedriver_win32\\chromedriver.exe'
DRIVER_PATH = 'C:\\Users\\Eli\\Downloads\\chromedriver_win32\\chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("user-data-dir=./selenium")
#driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url='https://www.officeally.com/slogin.aspx')
###   driver.add_cookie(cookie)
#login = driver.find_element_by_xpath("//input[@type='username']").send_keys('romaminc')
#password = driver.find_element_by_xpath("//input[@type='password']").send_keys('Advancemedical$2021!^!')
#submit = driver.find_element_by_xpath("//button[@ID='Login1_LoginButton']").click()

login = driver.find_element(By.ID, "Login1_UserName").send_keys('romaminc')
password = driver.find_element(By.ID, "Login1_Password").send_keys('Advancemedical$2021!^!!')
submit = driver.find_element(By.ID, "Login1_LoginButton").click()
#i = 1
for myId in ids:
    time.sleep(1)
    
    driver.execute_script("window.open('https://www.officeally.com/secure_oa.asp?GOTO=ClaimFix&TaskAction=Edit&Mode=Insert&FromIR=True&AllowCorrectedClaim=True&ClaimID={}');".format(myId))

    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.frame("Iframe9")
    
    LastName = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_LAST_NAME').get_attribute('value')
    FirstName = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_FIRST_NAME').get_attribute('value')
    DOBMonth = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PATIENT_BIRTHDATE_Month').get_attribute('value')
    DOBDay = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PATIENT_BIRTHDATE_Day').get_attribute('value')
    DOBYear = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PATIENT_BIRTHDATE_Year').get_attribute('value')
    PatientStreet = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_STREET_ADDR').get_attribute('value')
    PatientCity = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_CITY').get_attribute('value')
    PatientState = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_STATE').get_attribute('value')
    PatientZip = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_ZIP').get_attribute('value')
    PatientPhoneArea = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PHONE_AreaCode').get_attribute('value')
    PatientPhonePrefix = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PHONE_Prefix').get_attribute('value')
    PaientPhoneNumber = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_PHONE_Number').get_attribute('value')
    OrderingPhysicianFirst = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_OrderFirst0212').get_attribute('value')
    OrderingPhysicianlast = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_OrderLast0212').get_attribute('value')
    OrderingPhysicianNPI = driver.find_element(By.ID, 'ctl00_phFolderContent_ucHCFA_REFER_PHYSICIAN_NPI').get_attribute('value')
    CPTCode = driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_CPT_CODE0").get_attribute('value')
    Modifiers = driver.find_element(By.ID, "ctl00_phFolderContent_ucHCFA_ucHCFALineItem_ucClaimLineItem_MODIFIER_A0").get_attribute('value')
    
    if (FirstName + " " + LastName) in patientList:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        skipped_count += 1
        continue
    else:
        patientList.append(FirstName + " " + LastName)

    #f = open("ListOfPatientsDatabaseIEHPCPT.csv", "a")
    #f = open("ListOfPatientsDatabaseMedicareCPT.csv", "a")
    f = open("ListOfPatientsTest", "a")
    f.write("\n" + FirstName + ", " + LastName
     + ", " + DOBMonth + "/" + DOBDay + "/" + DOBYear + ", " + PatientStreet + " " + PatientCity + " " + PatientState + " " + PatientZip
    + ", " + PatientPhoneArea + PatientPhonePrefix + PaientPhoneNumber + ", " +
    OrderingPhysicianFirst + ", " + OrderingPhysicianlast + ", " + " ," + OrderingPhysicianNPI + ", " + CPTCode + ", " + Modifiers)
    f.close()
    #i += 1
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    


print("skipped {} patients".format(skipped_count))
    
'''
    try:
        driver.switch_to_window(driver.window_handles[1])
        #wait = WebDriverWait(driver, 5)
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "Iframe9"))
        )
        
    finally:
        driver.switch_to_frame("Iframe9")
        #driver.switch_to.frame('Iframe9')
'''
    
    
    
    
    #f = open("cookies", "w")
    #f.write(c)
    #window_name = driver.execute_script("return window.name")
    #print(window_name)

    #exitButton = driver.find_element_by_name ('btnAcknowledge').click()

    #driver.execute_script("window.open('');")
#driver.get('https://www.officeally.com/secure_oa.asp?GOTO=ClaimFix&TaskAction=Edit&Mode=Insert&FromIR=True&AllowCorrectedClaim=True&ClaimID=2480336207')https://www.officeally.com/secure_oa.asp?GOTO=ClaimFix&TaskAction=Edit&Mode=Insert&FromIR=True&AllowCorrectedClaim=True&ClaimID=2480336207
#driver.

