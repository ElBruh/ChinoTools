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