from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle
import time

fileOfIds = open("TXTx/Drids.txt", "r")
ids = []
newInfo = []
for lines in fileOfIds:
    ids.append(int(lines))
#DRIVER_PATH = 'C:\\Users\\Eli\\Downloads\\chromedriver_win32\\chromedriver.exe'
DRIVER_PATH = 'chromedriver'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.hipaaspace.com/medical_billing/coding/national_provider_identifier/npi_number_lookup.aspx')

for allIds in ids:
    search = driver.find_element(By.ID, "tbxSearchRequest").send_keys(allIds)
    time.sleep(1)
    DrInfo = driver.find_elements(By.XPATH, "//div[@id='Healthcare_Codes_Search_Results']//strong")
    for info in DrInfo:
        newInfo.append(info.text)
    count = (len(newInfo))
    if(count == 6):
        f = open("ListOfDoctorsInfo.csv", "a")
        f.write("\n" + "{}".format(allIds) + ", "  + newInfo[0] + " " + newInfo[1] + " " + newInfo[2] + " " + newInfo[3] + " " + newInfo[4] + ", " + newInfo[5])
        f.close()
    elif(count == 5): 
        f = open("ListOfDoctorsInfo.csv", "a")
        f.write("\n" + "{}".format(allIds) + ", "  + newInfo[0] + " " + newInfo[1] + " " + newInfo[2] + " " + newInfo[3] + ", " + newInfo[4])
        f.close()
    elif(count == 4): 
        f = open("ListOfDoctorsInfo.csv", "a")
        f.write("\n" + "{}".format(allIds) + ", "  + newInfo[0] + " " + newInfo[1] + " " + newInfo[2] + ", " + newInfo[3])
        f.close()
    elif(count == 3): 
        f = open("ListOfDoctorsInfo.csv", "a")
        f.write("\n" + "{}".format(allIds) + ", "  + newInfo[0] + " " + newInfo[1] + ", " + newInfo[2])
        f.close()
    elif(count == 2): 
        f = open("ListOfDoctorsInfo.csv", "a")
        f.write("\n" + "{}".format(allIds) + ", "  + newInfo[0] + ", " + newInfo[1])
        f.close()
    else:
        print("No Relevant Info")
        f = open("ListOfDoctorsInfo.csv", "a")
        f.write("\n" + "{}".format(allIds))
        f.close()
        newInfo = []    

        driver.find_element(By.ID, "tbxSearchRequest").clear()
        continue
    
    newInfo = []    

    driver.find_element(By.ID, "tbxSearchRequest").clear()
        #print(info.text)
