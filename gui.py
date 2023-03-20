from json import tool
import profile
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from typing import Counter
import pickle
from PDFCreator import formatInput, readPDF
from DatabaseTest import searchMedicalCPT, searchMedicareCPT, searchMedcalCPT2, searchMedicareCPT2
from npiSearch import getDrInfo
from searchICD10 import getICDInfo
from fillClaimForm import fillClaimFormFunction

default_input_width = 20
default_item_input_width = 10
default_ICD_Description_width = 65
default_modifier_width = 5
root = Tk()
currentProfile = ''


root.title("Create Patient Profile")


profile_dict ={
    'makeInvoice':1,
    'makeIntake':1,
    'UserName':'',
    'account':'',
    'patientOrderDate':'',
    'patientLastName':'',
    'patientAddress':'',
    'patientCity':'',
    'patientState':'',
    'patientZip':'',
    'patientPhone':'',
    'patientOrderDate':'',
    'patientDateOfBirth': '',
    'patientGender': '',    
    'patientMBI':'',
    'patientPreauthorization':'',
    'patientReferralName':'',
    'patientPCPFirstName':'',
    'patientPCPLastName':'',
    'patientPCPAddress':'',
    'patientPCPCity':'',
    'patientPCPState':'',
    'patientPCPZip':'',
    'patientPCPPhone':'',
    'patientPCPNPI':'',
    'itemRow1CPT':'',
    'itemRow2CPT':'',
    'itemRow3CPT':'',
    'itemRow4CPT':'',
    'itemRow5CPT':'',
    'itemRow6CPT':'',
    'itemRow1Modifier1':'',
    'itemRow1Modifier2':'',
    'itemRow1Modifier3':'',
    'itemRow1Modifier4':'',
    'itemRow2Modifier1':'',
    'itemRow2Modifier2':'',
    'itemRow2Modifier3':'',
    'itemRow2Modifier4':'',
    'itemRow3Modifier1':'',
    'itemRow3Modifier2':'',
    'itemRow3Modifier3':'',
    'itemRow3Modifier4':'',
    'itemRow4Modifier1':'',
    'itemRow4Modifier2':'',
    'itemRow4Modifier3':'',
    'itemRow4Modifier4':'',
    'itemRow5Modifier1':'',
    'itemRow5Modifier2':'',
    'itemRow5Modifier3':'',
    'itemRow5Modifier4':'',
    'itemRow6Modifier1':'',
    'itemRow5Modifier2':'',
    'itemRow5Modifier3':'',
    'itemRow5Modifier4':'',
    'itemRow6Modifier1':'',
    'itemRow6Modifier2':'',
    'itemRow6Modifier3':'',
    'itemRow6Modifier4':'',
    'itemRow1Qty':'',
    'itemRow2Qty':'',
    'itemRow3Qty':'',
    'itemRow4Qty':'',
    'itemRow5Qty':'',
    'itemRow6Qty':'',
    'itemRow1Price':'',
    'itemRow2Price':'',
    'itemRow3Price':'',
    'itemRow4Price':'',
    'itemRow5Price':'',
    'itemRow6Price':'',
    'itemRow1Description':'',
    'itemRow2Description':'',
    'itemRow3Description':'',
    'itemRow4Description':'',
    'itemRow5Description':'',
    'itemRow6Description':'',
    'diagnosisCodeRow1':'',
    'diagnosisCodeRow2':'',
    'diagnosisCodeRow3':'',
    'diagnosisCodeRow4':'',
    'diagnosisCodeRow1Description':'',
    'diagnosisCodeRow2Description':'',
    'diagnosisCodeRow3Description':'',
    'diagnosisCodeRow4Description':'',
    'profileCreationDate':'',

}


patientFrame = LabelFrame(root, text='Patient',  bd=2, relief=RIDGE)
doctorFrame = LabelFrame(root, text='Doctor', bd=2, relief=RIDGE)
submitFrame = Frame(root, relief=RIDGE)
itemsFrame = LabelFrame(root, text='Items', relief=RIDGE)
insuranceFrame = LabelFrame(root, text="Insurance Type", relief=RIDGE)
diagnosisFrame = LabelFrame(root, text="Diagnosis", relief=RIDGE)
InsuranceType = IntVar()
InsuranceType.set(0)

#cptRatesFile = open("MEDI-CALRATES.csv", "r")

def clearDr():

    patientPCPAddressCityInput.delete(0,END)
    patientPCPAddressInput.delete(0,END)
    patientPCPFirstNameInput.delete(0,END)
    patientPCPLastNameInput.delete(0,END)
    patientPCPAddressZipCodeInput.delete(0,END)
    patientPCPPhoneNumberInput.delete(0,END)
    patientPCPNPIInput.delete(0,END)

def clearPatient():

    patientAddressCityInput.delete(0,END)
    patientAddressInput.delete(0,END)
    patientFirstNameInput.delete(0,END)
    patientLastNameInput.delete(0,END)
    patientAddressZipCodeInput.delete(0,END)
    patientPhoneNumberInput.delete(0,END)
    patientInsuranceInput.delete(0,END)
    patientPreauthorizationInput.delete(0,END)
    patientDateOfBirth.delete(0,END)
    orderDateInput.delete(0,END)


def clearCpt():

    itemRow1Cpt.delete(0,END)
    itemRow2Cpt.delete(0,END)
    itemRow3Cpt.delete(0,END)
    itemRow4Cpt.delete(0,END)
    itemRow5Cpt.delete(0,END)
    itemRow6Cpt.delete(0,END)

    itemRow1Modifier1.delete(0,END)
    itemRow1Modifier2.delete(0,END)
    itemRow1Modifier3.delete(0,END)
    itemRow1Modifier4.delete(0,END)
    itemRow2Modifier1.delete(0,END)
    itemRow2Modifier2.delete(0,END)
    itemRow2Modifier3.delete(0,END)
    itemRow2Modifier4.delete(0,END)
    itemRow3Modifier1.delete(0,END)
    itemRow3Modifier2.delete(0,END)
    itemRow3Modifier3.delete(0,END)
    itemRow3Modifier4.delete(0,END)
    itemRow4Modifier1.delete(0,END)
    itemRow4Modifier2.delete(0,END)
    itemRow4Modifier3.delete(0,END)
    itemRow4Modifier4.delete(0,END)
    itemRow5Modifier1.delete(0,END)
    itemRow5Modifier2.delete(0,END)
    itemRow5Modifier3.delete(0,END)
    itemRow5Modifier4.delete(0,END)
    itemRow6Modifier1.delete(0,END)
    itemRow6Modifier2.delete(0,END)
    itemRow6Modifier3.delete(0,END)
    itemRow6Modifier4.delete(0,END)

    itemRow1Description.delete(0,END)
    itemRow2Description.delete(0,END)
    itemRow3Description.delete(0,END)
    itemRow4Description.delete(0,END)
    itemRow5Description.delete(0,END)
    itemRow6Description.delete(0,END)

    itemRow1Qty.delete(0,END)
    itemRow2Qty.delete(0,END)
    itemRow3Qty.delete(0,END)
    itemRow4Qty.delete(0,END)
    itemRow5Qty.delete(0,END)
    itemRow6Qty.delete(0,END)

    itemRow1Price.delete(0,END)
    itemRow2Price.delete(0,END)
    itemRow3Price.delete(0,END)
    itemRow4Price.delete(0,END)
    itemRow5Price.delete(0,END)
    itemRow6Price.delete(0,END)

def clearICD():

    diagnosisCodeRow1.delete(0,END)
    diagnosisCodeRow2.delete(0,END)
    diagnosisCodeRow3.delete(0,END)
    diagnosisCodeRow4.delete(0,END)
          
    diagnosisCodeRow1Description.delete(0,END)
    diagnosisCodeRow2Description.delete(0,END)
    diagnosisCodeRow3Description.delete(0,END)
    diagnosisCodeRow4Description.delete(0,END)

def clearAll():
    global currentProfile
    currentProfile = ''
    userName.delete(0,END)
    clearICD()
    clearCpt()
    clearPatient()
    clearDr()

def setInsuranceType(*args):
    if(value_inside_insurance.get() != "IEHP"):
        InsuranceType.set(0)
    else:
        InsuranceType.set(1)
    
    print(InsuranceType.get())

def insert_data(input_field, data):
    try:
        input_field.delete(0, 'end')
        input_field.insert(0, data)
    except Exception as e:
        print(f"Error while inserting data into the input field: {e}")

def getICDInfoFromPY():
    
    if(diagnosisCodeRow1.get().strip() != ""):

        try:
            tempDict = getICDInfo(diagnosisCodeRow1.get())
            if(tempDict['Valid'] == "true"):
                diagnosisCodeRow1Description.delete(0,END)
                diagnosisCodeRow1.delete(0,END)
                diagnosisCodeRow1Description.insert(0, "-" +  tempDict['Description'])
                diagnosisCodeRow1.insert(0,tempDict['Name'])
            else:
                messagebox.showerror(title="Not Billable", message= ("{}: {} is not billable".format(tempDict['Name'], tempDict['Description'],) + "\n" + tempDict["Note"] + "\nConsider using {}: {}".format(tempDict["ConsiderationName"], tempDict["ConsiderationDescription"])),)
        except: 
            messagebox.showerror(title="Error", message="ICD 10 code {} Not Found!".format(diagnosisCodeRow1.get()),)
            diagnosisCodeRow1Description.delete(0,END)
            diagnosisCodeRow1.delete(0,END)
    
    if(diagnosisCodeRow2.get().strip() != ""):

        try:
            tempDict = getICDInfo(diagnosisCodeRow2.get())
            if(tempDict['Valid'] == "true"):
                diagnosisCodeRow2Description.delete(0,END)
                diagnosisCodeRow2.delete(0,END)
                diagnosisCodeRow2Description.insert(0, "-" +  tempDict['Description'])
                diagnosisCodeRow2.insert(0,tempDict['Name'])
            else:
                messagebox.showerror(title="Not Billable", message= ("{}: {} is not billable".format(tempDict['Name'], tempDict['Description'],) + "\n" + tempDict["Note"] + "\nConsider using {}: {}".format(tempDict["ConsiderationName"], tempDict["ConsiderationDescription"])),)
        except:
            messagebox.showerror(title="Error", message="ICD 10 code {} Not Found!".format(diagnosisCodeRow2.get()),)
            diagnosisCodeRow2Description.delete(0,END)
            diagnosisCodeRow2.delete(0,END)
    
    if(diagnosisCodeRow3.get().strip() != ""):

        try:
            tempDict = getICDInfo(diagnosisCodeRow3.get())
            if(tempDict['Valid'] == "true"):
                diagnosisCodeRow3Description.delete(0,END)
                diagnosisCodeRow3.delete(0,END)
                diagnosisCodeRow3Description.insert(0, "-" +  tempDict['Description'])
                diagnosisCodeRow3.insert(0,tempDict['Name'])
            else:
                messagebox.showerror(title="Not Billable", message= ("{}: {} is not billable".format(tempDict['Name'], tempDict['Description'],) + "\n" + tempDict["Note"] + "\nConsider using {}: {}".format(tempDict["ConsiderationName"], tempDict["ConsiderationDescription"])),)
        except:
            messagebox.showerror(title="Error", message="ICD 10 code {} Not Found!".format(diagnosisCodeRow3.get()),)
            diagnosisCodeRow3Description.delete(0,END)
            diagnosisCodeRow3.delete(0,END)
    
    if(diagnosisCodeRow4.get().strip() != ""):

        try:
            tempDict = getICDInfo(diagnosisCodeRow4.get())
            if(tempDict['Valid'] == "true"):
                diagnosisCodeRow4Description.delete(0,END)
                diagnosisCodeRow4.delete(0,END)
                diagnosisCodeRow4Description.insert(0, "-" +  tempDict['Description'])
                diagnosisCodeRow4.insert(0,tempDict['Name'])
            else:
                messagebox.showerror(title="Not Billable", message= ("{}: {} is not billable".format(tempDict['Name'], tempDict['Description'],) + "\n" + tempDict["Note"] + "\nConsider using {}: {}".format(tempDict["ConsiderationName"], tempDict["ConsiderationDescription"])),)
        except:
            messagebox.showerror(title="Error", message="ICD 10 code {} Not Found!".format(diagnosisCodeRow4.get()),)
            diagnosisCodeRow4Description.delete(0,END)
            diagnosisCodeRow4.delete(0,END)
    
def getNpiInfo():

    try:
        dr_info_dict = getDrInfo(patientPCPNPIInput.get())
        
    
    except:
        messagebox.showerror(title="Error", message="Dr. Info Not Found!", )
        return
    

    #dr_info_dict = getDrInfo(patientPCPNPIInput.get())

    patientPCPAddressCityInput.delete(0,END)
    patientPCPAddressInput.delete(0,END)
    patientPCPFirstNameInput.delete(0,END)
    patientPCPLastNameInput.delete(0,END)
    patientPCPAddressZipCodeInput.delete(0,END)
    patientPCPPhoneNumberInput.delete(0,END)

    patientPCPAddressCityInput.insert(0,dr_info_dict["city"])
    patientPCPAddressInput.insert(0,dr_info_dict["address_1"] + dr_info_dict["address_2"])
    patientPCPFirstNameInput.insert(0,dr_info_dict["first_name"])
    patientPCPLastNameInput.insert(0,dr_info_dict["last_name"])
    patientPCPAddressZipCodeInput.insert(0,dr_info_dict["zip"])
    patientPCPPhoneNumberInput.insert(0,dr_info_dict["phone_number"])


    

def getCPTInfo():
    '''
    query = []
    options = []
    
    options.append(rentalCheckRow1.get())
    options.append(rentalCheckRow2.get())
    options.append(rentalCheckRow3.get())
    options.append(rentalCheckRow4.get())
    options.append(rentalCheckRow5.get())
    options.append(rentalCheckRow6.get())
    

    query.append(itemRow1Cpt.get())
    query.append(itemRow2Cpt.get())
    query.append(itemRow3Cpt.get())
    query.append(itemRow4Cpt.get())
    query.append(itemRow5Cpt.get())
    query.append(itemRow6Cpt.get())
    '''

    if(itemRow1Cpt.get() != ""):
        #if Medical
        if(InsuranceType.get() == 1):
            try:
                temp_Dict = searchMedcalCPT2(itemRow1Cpt.get(), rentalCheckRow1.get())
                itemRow1Price.delete(0,END)
                itemRow1Price.insert(0, temp_Dict["ItemValue"])
                itemRow1Description.delete(0,END)
                itemRow1Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow1.get() == 1):
                    itemRow1Modifier1.delete(0,END)
                    itemRow1Modifier1.insert(0,"NU")
                    itemRow1Modifier2.delete(0,END)
                    itemRow1Modifier3.delete(0,END)
                    itemRow1Modifier4.delete(0,END)
                if(rentalCheckRow1.get() == 0):
                    itemRow1Modifier1.delete(0,END)
                    itemRow1Modifier1.insert(0,"RR")
                    itemRow1Modifier2.delete(0,END)
                    itemRow1Modifier3.delete(0,END)
                    itemRow1Modifier4.delete(0,END)
            except:
                if(rentalCheckRow1.get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medi-Cal Fee Schedule".format(itemRow1Cpt.get()),)
                else:
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medi-Cal Fee Schedule".format(itemRow1Cpt.get()),)
        #if Medicare
        if(InsuranceType.get() == 0):
            try:
                temp_Dict = searchMedicareCPT2(itemRow1Cpt.get(), rentalCheckRow1.get())
                itemRow1Price.delete(0,END)
                itemRow1Price.insert(0, temp_Dict["ItemValue"])
                itemRow1Description.delete(0,END)
                itemRow1Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow1.get() == 1):
                    itemRow1Modifier1.delete(0,END)
                    itemRow1Modifier1.insert(0,"NU")
                    itemRow1Modifier2.delete(0,END)
                    itemRow1Modifier2.insert(0,"KX")
                    itemRow1Modifier3.delete(0,END)
                    itemRow1Modifier4.delete(0,END)
                if(rentalCheckRow1.get() == 0):
                    itemRow1Modifier1.delete(0,END)
                    itemRow1Modifier1.insert(0,"RR")
                    itemRow1Modifier2.delete(0,END)
                    itemRow1Modifier2.insert(0,"KH")
                    itemRow1Modifier3.delete(0,END)
                    itemRow1Modifier3.insert(0,"KX")
                    itemRow1Modifier4.delete(0,END)
            except:
                #temp_Dict = searchMedicareCPT2(itemRow1Cpt.get(), 2)
                if(rentalCheckRow1.get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medicare Fee Schedule".format(itemRow1Cpt.get()),)
                else:
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medicare Fee Schedule".format(itemRow1Cpt.get()),)
    if(itemRow2Cpt.get() != ""):
        #if Medical
        if(InsuranceType.get() == 1):
            try:
                temp_Dict = searchMedcalCPT2(itemRow2Cpt.get(), rentalCheckRow2.get())
                itemRow2Price.delete(0,END)
                itemRow2Price.insert(0, temp_Dict["ItemValue"])
                itemRow2Description.delete(0,END)
                itemRow2Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow2.get() == 1):
                    itemRow2Modifier1.delete(0,END)
                    itemRow2Modifier1.insert(0,"NU")
                    itemRow2Modifier2.delete(0,END)
                    itemRow2Modifier3.delete(0,END)
                    itemRow2Modifier4.delete(0,END)
                if(rentalCheckRow2.get() == 0):
                    itemRow2Modifier1.delete(0,END)
                    itemRow2Modifier1.insert(0,"RR")
                    itemRow2Modifier2.delete(0,END)
                    itemRow2Modifier3.delete(0,END)
                    itemRow2Modifier4.delete(0,END)
            except:
                if(rentalCheckRow2.get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medi-Cal Fee Schedule".format(itemRow2Cpt.get()),)
                else:
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medi-Cal Fee Schedule".format(itemRow2Cpt.get()),)
        #if medicare
        if(InsuranceType.get() == 0):
            try:
                temp_Dict = searchMedicareCPT2(itemRow2Cpt.get(), rentalCheckRow2.get())
                itemRow2Price.delete(0,END)
                itemRow2Price.insert(0, temp_Dict["ItemValue"])
                itemRow2Description.delete(0,END)
                itemRow2Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow2.get() == 1):
                    itemRow2Modifier1.delete(0,END)
                    itemRow2Modifier1.insert(0,"NU")
                    itemRow2Modifier2.delete(0,END)
                    itemRow2Modifier2.insert(0,"KX")
                    itemRow2Modifier3.delete(0,END)
                    itemRow2Modifier4.delete(0,END)

                if(rentalCheckRow2.get() == 0):
                    itemRow2Modifier1.delete(0,END)
                    itemRow2Modifier1.insert(0,"RR")
                    itemRow2Modifier2.delete(0,END)
                    itemRow2Modifier2.insert(0,"KH")
                    itemRow2Modifier3.delete(0,END)
                    itemRow2Modifier3.insert(0,"KX")
                    itemRow2Modifier4.delete(0,END)
            except:
                if(rentalCheckRow2.get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medicare Fee Schedule".format(itemRow2Cpt.get()),)
                else:
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medicare Fee Schedule".format(itemRow2Cpt.get()),)
    if(itemRow3Cpt.get() != ""):
        #if Medical
        if(InsuranceType.get() == 1):
            try:
                temp_Dict = searchMedcalCPT2(itemRow3Cpt.get(), rentalCheckRow3.get())
                itemRow3Price.delete(0,END)
                itemRow3Price.insert(0, temp_Dict["ItemValue"])
                itemRow3Description.delete(0,END)
                itemRow3Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow3.get() == 1):
                    itemRow3Modifier1.delete(0,END)
                    itemRow3Modifier1.insert(0,"NU")
                    itemRow3Modifier2.delete(0,END)
                    itemRow3Modifier3.delete(0,END)
                    itemRow3Modifier4.delete(0,END)
                if(rentalCheckRow3.get() == 0):
                    itemRow3Modifier1.delete(0,END)
                    itemRow3Modifier1.insert(0,"RR")
                    itemRow3Modifier2.delete(0,END)
                    itemRow3Modifier3.delete(0,END)
                    itemRow3Modifier4.delete(0,END)
            except:
                if(rentalCheckRow3.get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medi-Cal Fee Schedule".format(itemRow3Cpt.get()),)
                else:
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medi-Cal Fee Schedule".format(itemRow3Cpt.get()),)
        #if Medicare
        if(InsuranceType.get() == 0):
            try:
                temp_Dict = searchMedicareCPT2(itemRow3Cpt.get(), rentalCheckRow3.get())
                itemRow3Price.delete(0,END)
                itemRow3Price.insert(0, temp_Dict["ItemValue"])
                itemRow3Description.delete(0,END)
                itemRow3Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow3.get() == 1):
                    itemRow3Modifier1.delete(0,END)
                    itemRow3Modifier1.insert(0,"NU")
                    itemRow3Modifier2.delete(0,END)
                    itemRow3Modifier2.insert(0,"KX")
                    itemRow3Modifier3.delete(0,END)
                    itemRow3Modifier4.delete(0,END)
                if(rentalCheckRow3.get() == 0):
                    itemRow3Modifier1.delete(0,END)
                    itemRow3Modifier1.insert(0,"RR")
                    itemRow3Modifier2.delete(0,END)
                    itemRow3Modifier2.insert(0,"KH")
                    itemRow3Modifier3.delete(0,END)
                    itemRow3Modifier3.insert(0,"KX")
                    itemRow3Modifier4.delete(0,END)
                
            except:
                if(rentalCheckRow3.get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medicare Fee schedule".format(itemRow3Cpt.get()),)
                else:
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medicare Fee schedule".format(itemRow3Cpt.get()),)
    if(itemRow4Cpt.get() != ""):
        #if Medical
        if(InsuranceType.get() == 1):
            try:
                temp_Dict = searchMedcalCPT2(itemRow4Cpt.get(), rentalCheckRow4.get())
                itemRow4Price.delete(0,END)
                itemRow4Price.insert(0, temp_Dict["ItemValue"])
                itemRow4Description.delete(0,END)
                itemRow4Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow4.get() == 1):
                    itemRow4Modifier1.delete(0,END)
                    itemRow4Modifier1.insert(0,"NU")
                    itemRow4Modifier2.delete(0,END)
                    itemRow4Modifier3.delete(0,END)
                    itemRow4Modifier4.delete(0,END)
                if(rentalCheckRow4.get() == 0):
                    itemRow4Modifier1.delete(0,END)
                    itemRow4Modifier1.insert(0,"RR")
                    itemRow4Modifier2.delete(0,END)
                    itemRow4Modifier3.delete(0,END)
                    itemRow4Modifier4.delete(0,END)
            except:
                if(rentalCheckRow4.get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medi-Cal Fee Schedule".format(itemRow4Cpt.get()),)
                else:
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medi-Cal Fee Schedule".format(itemRow4Cpt.get()),)
        #if Medicare
        if(InsuranceType.get() == 0):
            try:
                temp_Dict = searchMedicareCPT2(itemRow4Cpt.get(), rentalCheckRow4.get())
                itemRow4Price.delete(0,END)
                itemRow4Price.insert(0, temp_Dict["ItemValue"])
                itemRow4Description.delete(0,END)
                itemRow4Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow4.get() == 1):
                    itemRow4Modifier1.delete(0,END)
                    itemRow4Modifier1.insert(0,"NU")
                    itemRow4Modifier2.delete(0,END)
                    itemRow4Modifier2.insert(0,"KX")
                    itemRow4Modifier3.delete(0,END)
                    itemRow4Modifier4.delete(0,END)
                if(rentalCheckRow4.get() == 0):
                    itemRow4Modifier1.delete(0,END)
                    itemRow4Modifier1.insert(0,"RR")
                    itemRow4Modifier2.delete(0,END)
                    itemRow4Modifier2.insert(0,"KH")
                    itemRow4Modifier3.delete(0,END)
                    itemRow4Modifier3.insert(0,"KX")
                    itemRow4Modifier4.delete(0,END)
            except:
                if(rentalCheckRow4.get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medicare Fee Schedule".format(itemRow4Cpt.get()),)
                else:
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medicare Fee Schedule".format(itemRow4Cpt.get()),)
    if(itemRow5Cpt.get() != ""):
        #if Medical
        if(InsuranceType.get() == 1):
            try:
                temp_Dict = searchMedcalCPT2(itemRow5Cpt.get(), rentalCheckRow5.get())
                itemRow5Price.delete(0,END)
                itemRow5Price.insert(0, temp_Dict["ItemValue"])
                itemRow5Description.delete(0,END)
                itemRow5Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow5.get() == 1):
                    itemRow5Modifier1.delete(0,END)
                    itemRow5Modifier1.insert(0,"NU")
                    itemRow5Modifier2.delete(0,END)
                    itemRow5Modifier3.delete(0,END)
                    itemRow5Modifier4.delete(0,END)
                if(rentalCheckRow5.get() == 0):
                    itemRow5Modifier1.delete(0,END)
                    itemRow5Modifier1.insert(0,"RR")
                    itemRow5Modifier2.delete(0,END)
                    itemRow5Modifier3.delete(0,END)
                    itemRow5Modifier4.delete(0,END)
            except:
                if(rentalCheckRow5().get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medi-Cal Fee Schedule".format(itemRow5Cpt.get()),)
                else:
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medi-Cal Fee Schedule".format(itemRow5Cpt.get()),)
        #if Medicare
        if(InsuranceType.get() == 0):
            try:
                temp_Dict = searchMedicareCPT2(itemRow5Cpt.get(), rentalCheckRow5.get())
                itemRow5Price.delete(0,END)
                itemRow5Price.insert(0, temp_Dict["ItemValue"])
                itemRow5Description.delete(0,END)
                itemRow5Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow5.get() == 1):
                    itemRow5Modifier1.delete(0,END)
                    itemRow5Modifier1.insert(0,"NU")
                    itemRow5Modifier2.delete(0,END)
                    itemRow5Modifier2.insert(0,"KX")
                    itemRow5Modifier3.delete(0,END)
                    itemRow5Modifier4.delete(0,END)
                if(rentalCheckRow5.get() == 0):
                    itemRow5Modifier1.delete(0,END)
                    itemRow5Modifier1.insert(0,"RR")
                    itemRow5Modifier2.delete(0,END)
                    itemRow5Modifier2.insert(0,"KH")
                    itemRow5Modifier3.delete(0,END)
                    itemRow5Modifier3.insert(0,"KX")
                    itemRow5Modifier4.delete(0,END)
            except:
                if(rentalCheckRow5.get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medicare Fee Schedule".format(itemRow5Cpt.get()),)
                else:
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medicare Fee Schedule".format(itemRow5Cpt.get()),)
    if(itemRow6Cpt.get() != ""):
        #if Medical
        if(InsuranceType.get() == 1):
            try:
                temp_Dict = searchMedcalCPT2(itemRow6Cpt.get(), rentalCheckRow6.get())
                itemRow6Price.delete(0,END)
                itemRow6Price.insert(0, temp_Dict["ItemValue"])
                itemRow6Description.delete(0,END)
                itemRow6Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow6.get() == 1):
                    itemRow6Modifier1.delete(0,END)
                    itemRow6Modifier1.insert(0,"NU")
                    itemRow6Modifier2.delete(0,END)
                    itemRow6Modifier3.delete(0,END)
                    itemRow6Modifier4.delete(0,END)
                if(rentalCheckRow6.get() == 0):
                    itemRow6Modifier1.delete(0,END)
                    itemRow6Modifier1.insert(0,"RR")
                    itemRow6Modifier2.delete(0,END)
                    itemRow6Modifier3.delete(0,END)
                    itemRow6Modifier4.delete(0,END)
            except:
                if(rentalCheckRow6.get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medi-Cal Fee Schedule".format(itemRow6Cpt.get()),)
                else:
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medi-Cal Fee Schedule".format(itemRow6Cpt.get()),)    
        #if Medicare
        if(InsuranceType.get() == 0):
            try:
                temp_Dict = searchMedicareCPT2(itemRow6Cpt.get(), rentalCheckRow6.get())
                itemRow6Price.delete(0,END)
                itemRow6Price.insert(0, temp_Dict["ItemValue"])
                itemRow6Description.delete(0,END)
                itemRow6Description.insert(0, temp_Dict["itemDescription"])

                if(rentalCheckRow6.get() == 1):
                    itemRow6Modifier1.delete(0,END)
                    itemRow6Modifier1.insert(0,"NU")
                    itemRow6Modifier2.delete(0,END)
                    itemRow6Modifier2.insert(0,"KX")
                    itemRow6Modifier3.delete(0,END)
                    itemRow6Modifier4.delete(0,END)
                if(rentalCheckRow6.get() == 0):
                    itemRow6Modifier1.delete(0,END)
                    itemRow6Modifier1.insert(0,"RR")
                    itemRow6Modifier2.delete(0,END)
                    itemRow6Modifier2.insert(0,"KH")
                    itemRow6Modifier3.delete(0,END)
                    itemRow6Modifier3.insert(0,"KX")
                    itemRow6Modifier4.delete(0,END)
            except:
                if(rentalCheckRow6.get() == 0):
                    messagebox.showerror(title="Error", message="CPT code ({} RR) Not Found In Medicare Fee Schedule".format(itemRow6Cpt.get()),)
                else:   
                    messagebox.showerror(title="Error", message="CPT code ({} NU) Not Found In Medicare Fee Schedule".format(itemRow6Cpt.get()),)


def sendToPDFCreator():
    #print(e)
    #new_date = datetime.now()
    #some_date = new_date.strftime("%B.%d.%Y--%H.%M.%S ")
    #profile_dict["profileCreationDate"] = some_date
    profile_dict["UserName"] = userName.get().strip()
    profile_dict["account"] = value_inside_insurance.get().strip()
    #get patient info from forms
    profile_dict['makeInvoice'] = invoiceCheck.get()
    profile_dict['makeIntake'] = intakeCheck.get()
    profile_dict['patientFirstName'] = patientFirstNameInput.get().strip()
    profile_dict['patientLastName'] = patientLastNameInput.get().strip()
    profile_dict['patientAddress'] = patientAddressInput.get().strip()
    profile_dict['patientCity'] = patientAddressCityInput.get().strip()
    profile_dict['patientState'] = value_inside_patient.get().strip()
    profile_dict['patientZip'] = patientAddressZipCodeInput.get().strip()
    profile_dict['patientPhone'] = patientPhoneNumberInput.get().strip()
    profile_dict['patientOrderDate'] = orderDateInput.get().strip()
    profile_dict['patientMBI'] = patientInsuranceInput.get().strip()
    profile_dict['patientPreauthorization'] = patientPreauthorizationInput.get().strip()
    profile_dict["patientDateOfBirth"] = patientDateOfBirth.get().strip()
    
    try:
        if(genderCheck.get() == 0):
            profile_dict['patientGender'] = 'Male'
        else:
            profile_dict['patientGender'] = 'Female'
    except:
        print("An error has occured in genderCheck")
    #get doctor info from forms
    profile_dict['patientPCPFirstName'] = patientPCPFirstNameInput.get().strip()
    profile_dict['patientPCPLastName'] = patientPCPLastNameInput.get().strip()
    profile_dict['patientPCPAddress'] = patientPCPAddressInput.get().strip()
    profile_dict['patientPCPCity'] = patientPCPAddressCityInput.get().strip()
    profile_dict['patientPCPState'] = value_inside_doctor.get().strip()
    profile_dict['patientPCPZip'] = patientPCPAddressZipCodeInput.get().strip()
    profile_dict['patientPCPPhone'] = patientPCPPhoneNumberInput.get().strip()
    profile_dict['patientPCPNPI'] = patientPCPNPIInput.get().strip()
    
    #get Cpt Row1 info from forms 
    profile_dict['itemRow1CPT'] = itemRow1Cpt.get().strip()
    profile_dict['itemRow1Modifier1'] = itemRow1Modifier1.get().strip()
    profile_dict['itemRow1Modifier2'] = itemRow1Modifier2.get().strip()
    profile_dict['itemRow1Modifier3'] = itemRow1Modifier3.get().strip()
    profile_dict['itemRow1Modifier4'] = itemRow1Modifier4.get().strip()
    profile_dict['itemRow1Description'] = itemRow1Description.get().strip().strip()
    profile_dict['itemRow1Qty'] = itemRow1Qty.get().strip()
    profile_dict['itemRow1Price'] = itemRow1Price.get().strip()

    #get Cpt Row2 info from forms
    profile_dict['itemRow2CPT'] = itemRow2Cpt.get().strip()
    profile_dict['itemRow2Modifier1'] = itemRow2Modifier1.get().strip()
    profile_dict['itemRow2Modifier2'] = itemRow2Modifier2.get().strip()
    profile_dict['itemRow2Modifier3'] = itemRow2Modifier3.get().strip()
    profile_dict['itemRow2Modifier4'] = itemRow2Modifier4.get().strip()
    profile_dict['itemRow2Description'] = itemRow2Description.get().strip().strip()
    profile_dict['itemRow2Qty'] = itemRow2Qty.get().strip()
    profile_dict['itemRow2Price'] = itemRow2Price.get().strip()

    #get Cpt Row3 info from forms
    profile_dict['itemRow3CPT'] = itemRow3Cpt.get().strip()
    profile_dict['itemRow3Modifier1'] = itemRow3Modifier1.get().strip()
    profile_dict['itemRow3Modifier2'] = itemRow3Modifier2.get().strip()
    profile_dict['itemRow3Modifier3'] = itemRow3Modifier3.get().strip()
    profile_dict['itemRow3Modifier4'] = itemRow3Modifier4.get().strip()
    profile_dict['itemRow3Description'] = itemRow3Description.get().strip()
    profile_dict['itemRow3Qty'] = itemRow3Qty.get().strip()
    profile_dict['itemRow3Price'] = itemRow3Price.get().strip()

    #get Cpt Row4 info from forms
    profile_dict['itemRow4CPT'] = itemRow4Cpt.get().strip()
    profile_dict['itemRow4Modifier1'] = itemRow4Modifier1.get().strip()
    profile_dict['itemRow4Modifier2'] = itemRow4Modifier2.get().strip()
    profile_dict['itemRow4Modifier3'] = itemRow4Modifier3.get().strip()
    profile_dict['itemRow4Modifier4'] = itemRow4Modifier4.get().strip()
    profile_dict['itemRow4Description'] = itemRow4Description.get().strip().strip()
    profile_dict['itemRow4Qty'] = itemRow4Qty.get().strip()
    profile_dict['itemRow4Price'] = itemRow4Price.get().strip()

    #get Cpt Row5 info from forms 
    profile_dict['itemRow5CPT'] = itemRow5Cpt.get().strip()
    profile_dict['itemRow5Modifier1'] = itemRow5Modifier1.get().strip()
    profile_dict['itemRow5Modifier2'] = itemRow5Modifier2.get().strip()
    profile_dict['itemRow5Modifier3'] = itemRow5Modifier3.get().strip()
    profile_dict['itemRow5Modifier4'] = itemRow5Modifier4.get().strip()
    profile_dict['itemRow5Description'] = itemRow5Description.get().strip()
    profile_dict['itemRow5Qty'] = itemRow5Qty.get().strip()
    profile_dict['itemRow5Price'] = itemRow5Price.get().strip()

    #get Cpt Row6 info from forms 
    profile_dict['itemRow6CPT'] = itemRow6Cpt.get().strip()
    profile_dict['itemRow6Modifier1'] = itemRow6Modifier1.get().strip()
    profile_dict['itemRow6Modifier2'] = itemRow6Modifier2.get().strip()
    profile_dict['itemRow6Modifier3'] = itemRow6Modifier3.get().strip()
    profile_dict['itemRow6Modifier4'] = itemRow6Modifier4.get().strip()
    profile_dict['itemRow6Description'] = itemRow6Description.get().strip()
    profile_dict['itemRow6Qty'] = itemRow6Qty.get().strip()
    profile_dict['itemRow6Price'] = itemRow6Price.get().strip()

    #get diagnosis codes and descriptions from forms
    profile_dict['diagnosisCodeRow1'] = diagnosisCodeRow1.get().strip()
    profile_dict['diagnosisCodeRow2'] = diagnosisCodeRow2.get().strip()
    profile_dict['diagnosisCodeRow3'] = diagnosisCodeRow3.get().strip()
    profile_dict['diagnosisCodeRow4'] = diagnosisCodeRow4.get().strip()

    profile_dict['diagnosisCodeRow1Description'] = diagnosisCodeRow1Description.get().strip()
    profile_dict['diagnosisCodeRow2Description'] = diagnosisCodeRow2Description.get().strip()
    profile_dict['diagnosisCodeRow3Description'] = diagnosisCodeRow3Description.get().strip()
    profile_dict['diagnosisCodeRow4Description'] = diagnosisCodeRow4Description.get().strip()
    
    try:
        formatInput(profile_dict)
        messagebox.showinfo(title="Success!", message="PDFs have been created!")
    except:
        messagebox.showerror(title="Error!", message="An error has occured")
    #os.system("python PDFCreator.py {} {} {} {} \"{}\" {} {} {} {} {} {} {} {}".format(a,b,c,d,e,f,g,h,i,j,k,l,m))

def sendToFillClaimForm():
    #print(e)
    #new_date = datetime.now()
    #some_date = new_date.strftime("%B.%d.%Y--%H.%M.%S ")
    #profile_dict["profileCreationDate"] = some_date
    profile_dict["UserName"] = userName.get().strip()
    profile_dict["account"] = value_inside_insurance.get().strip()
    #get patient info from forms
    profile_dict['makeInvoice'] = invoiceCheck.get()
    profile_dict['makeIntake'] = intakeCheck.get()
    profile_dict['patientFirstName'] = patientFirstNameInput.get().strip()
    profile_dict['patientLastName'] = patientLastNameInput.get().strip()
    profile_dict['patientAddress'] = patientAddressInput.get().strip()
    profile_dict['patientCity'] = patientAddressCityInput.get().strip()
    profile_dict['patientState'] = value_inside_patient.get().strip()
    profile_dict['patientZip'] = patientAddressZipCodeInput.get().strip()
    profile_dict['patientPhone'] = patientPhoneNumberInput.get().strip()
    profile_dict['patientOrderDate'] = orderDateInput.get().strip()
    profile_dict['patientMBI'] = patientInsuranceInput.get().strip()
    profile_dict['patientPreauthorization'] = patientPreauthorizationInput.get().strip()
    profile_dict["patientDateOfBirth"] = patientDateOfBirth.get().strip()
    
    try:
        if(genderCheck.get() == 0):
            profile_dict['patientGender'] = 'Male'
        else:
            profile_dict['patientGender'] = 'Female'
    except:
        print("An error has occured in genderCheck")

    #get doctor info from forms
    profile_dict['patientPCPFirstName'] = patientPCPFirstNameInput.get().strip()
    profile_dict['patientPCPLastName'] = patientPCPLastNameInput.get().strip()
    profile_dict['patientPCPAddress'] = patientPCPAddressInput.get().strip()
    profile_dict['patientPCPCity'] = patientPCPAddressCityInput.get().strip()
    profile_dict['patientPCPState'] = value_inside_doctor.get().strip()
    profile_dict['patientPCPZip'] = patientPCPAddressZipCodeInput.get().strip()
    profile_dict['patientPCPPhone'] = patientPCPPhoneNumberInput.get().strip()
    profile_dict['patientPCPNPI'] = patientPCPNPIInput.get().strip()
    
    #get Cpt Row1 info from forms 
    profile_dict['itemRow1CPT'] = itemRow1Cpt.get().strip()
    profile_dict['itemRow1Modifier1'] = itemRow1Modifier1.get().strip()
    profile_dict['itemRow1Modifier2'] = itemRow1Modifier2.get().strip()
    profile_dict['itemRow1Modifier3'] = itemRow1Modifier3.get().strip()
    profile_dict['itemRow1Modifier4'] = itemRow1Modifier4.get().strip()
    profile_dict['itemRow1Description'] = itemRow1Description.get().strip()
    profile_dict['itemRow1Qty'] = itemRow1Qty.get().strip()
    profile_dict['itemRow1Price'] = itemRow1Price.get().strip()

    #get Cpt Row2 info from forms
    profile_dict['itemRow2CPT'] = itemRow2Cpt.get().strip()
    profile_dict['itemRow2Modifier1'] = itemRow2Modifier1.get().strip()
    profile_dict['itemRow2Modifier2'] = itemRow2Modifier2.get().strip()
    profile_dict['itemRow2Modifier3'] = itemRow2Modifier3.get().strip()
    profile_dict['itemRow2Modifier4'] = itemRow2Modifier4.get().strip()
    profile_dict['itemRow2Description'] = itemRow2Description.get().strip()
    profile_dict['itemRow2Qty'] = itemRow2Qty.get().strip()
    profile_dict['itemRow2Price'] = itemRow2Price.get().strip()

    #get Cpt Row3 info from forms
    profile_dict['itemRow3CPT'] = itemRow3Cpt.get().strip()
    profile_dict['itemRow3Modifier1'] = itemRow3Modifier1.get().strip()
    profile_dict['itemRow3Modifier2'] = itemRow3Modifier2.get().strip()
    profile_dict['itemRow3Modifier3'] = itemRow3Modifier3.get().strip()
    profile_dict['itemRow3Modifier4'] = itemRow3Modifier4.get().strip()
    profile_dict['itemRow3Description'] = itemRow3Description.get().strip()
    profile_dict['itemRow3Qty'] = itemRow3Qty.get().strip()
    profile_dict['itemRow3Price'] = itemRow3Price.get().strip()

    #get Cpt Row4 info from forms
    profile_dict['itemRow4CPT'] = itemRow4Cpt.get().strip()
    profile_dict['itemRow4Modifier1'] = itemRow4Modifier1.get().strip()
    profile_dict['itemRow4Modifier2'] = itemRow4Modifier2.get().strip()
    profile_dict['itemRow4Modifier3'] = itemRow4Modifier3.get().strip()
    profile_dict['itemRow4Modifier4'] = itemRow4Modifier4.get().strip()
    profile_dict['itemRow4Description'] = itemRow4Description.get().strip()
    profile_dict['itemRow4Qty'] = itemRow4Qty.get().strip()
    profile_dict['itemRow4Price'] = itemRow4Price.get().strip()

    #get Cpt Row5 info from forms 
    profile_dict['itemRow5CPT'] = itemRow5Cpt.get().strip()
    profile_dict['itemRow5Modifier1'] = itemRow5Modifier1.get().strip()
    profile_dict['itemRow5Modifier2'] = itemRow5Modifier2.get().strip()
    profile_dict['itemRow5Modifier3'] = itemRow5Modifier3.get().strip()
    profile_dict['itemRow5Modifier4'] = itemRow5Modifier4.get().strip()
    profile_dict['itemRow5Description'] = itemRow5Description.get().strip()
    profile_dict['itemRow5Qty'] = itemRow5Qty.get().strip()
    profile_dict['itemRow5Price'] = itemRow5Price.get().strip()

    #get Cpt Row6 info from forms 
    profile_dict['itemRow6CPT'] = itemRow6Cpt.get().strip()
    profile_dict['itemRow6Modifier1'] = itemRow6Modifier1.get().strip()
    profile_dict['itemRow6Modifier2'] = itemRow6Modifier2.get().strip()
    profile_dict['itemRow6Modifier3'] = itemRow6Modifier3.get().strip()
    profile_dict['itemRow6Modifier4'] = itemRow6Modifier4.get().strip()
    profile_dict['itemRow6Description'] = itemRow6Description.get().strip()
    profile_dict['itemRow6Qty'] = itemRow6Qty.get().strip()
    profile_dict['itemRow6Price'] = itemRow6Price.get().strip()

    #get diagnosis codes and descriptions from forms
    profile_dict['diagnosisCodeRow1'] = diagnosisCodeRow1.get().strip()
    profile_dict['diagnosisCodeRow2'] = diagnosisCodeRow2.get().strip()
    profile_dict['diagnosisCodeRow3'] = diagnosisCodeRow3.get().strip()
    profile_dict['diagnosisCodeRow4'] = diagnosisCodeRow4.get().strip()

    profile_dict['diagnosisCodeRow1Description'] = diagnosisCodeRow1Description.get().strip()
    profile_dict['diagnosisCodeRow2Description'] = diagnosisCodeRow2Description.get().strip()
    profile_dict['diagnosisCodeRow3Description'] = diagnosisCodeRow3Description.get().strip()
    profile_dict['diagnosisCodeRow4Description'] = diagnosisCodeRow4Description.get().strip()
    
    
    try:
        fillClaimFormFunction(profile_dict)
        #messagebox.showinfo(title="Success!", message="PDFs have been created!")
    except:
        messagebox.showerror(title="Error!", message="An error has occured")
    #os.system("python PDFCreator.py {} {} {} {} \"{}\" {} {} {} {} {} {} {} {}".format(a,b,c,d,e,f,g,h,i,j,k,l,m))
    
def saveProfile():
    global currentProfile
    print(currentProfile)
    if(currentProfile != ''):
        #print(e)
        #new_date = datetime.now()
        #some_date = new_date.strftime("%B.%d.%Y--%H.%M.%S ")
        #profile_dict["profileCreationDate"] = some_date
        profile_dict["UserName"] = userName.get().strip()
        profile_dict["account"] = value_inside_insurance.get().strip()
        #get patient info from forms
        profile_dict['makeInvoice'] = invoiceCheck.get()
        profile_dict['makeIntake'] = intakeCheck.get()
        profile_dict['patientFirstName'] = patientFirstNameInput.get().strip()
        profile_dict['patientLastName'] = patientLastNameInput.get().strip()
        profile_dict['patientAddress'] = patientAddressInput.get().strip()
        profile_dict['patientCity'] = patientAddressCityInput.get().strip()
        profile_dict['patientState'] = value_inside_patient.get().strip()
        profile_dict['patientZip'] = patientAddressZipCodeInput.get().strip()
        profile_dict['patientPhone'] = patientPhoneNumberInput.get().strip()
        profile_dict['patientOrderDate'] = orderDateInput.get().strip()
        profile_dict['patientMBI'] = patientInsuranceInput.get().strip()
        profile_dict['patientPreauthorization'] = patientPreauthorizationInput.get().strip()
        profile_dict["patientDateOfBirth"] = patientDateOfBirth.get().strip()
        
        try:
            if(genderCheck.get() == 0):
                profile_dict['patientGender'] = 'Male'
            else:
                profile_dict['patientGender'] = 'Female'
        except:
            print("An error has occured in genderCheck")

        #get doctor info from forms
        profile_dict['patientPCPFirstName'] = patientPCPFirstNameInput.get().strip()
        profile_dict['patientPCPLastName'] = patientPCPLastNameInput.get().strip()
        profile_dict['patientPCPAddress'] = patientPCPAddressInput.get().strip()
        profile_dict['patientPCPCity'] = patientPCPAddressCityInput.get().strip()
        profile_dict['patientPCPState'] = value_inside_doctor.get().strip()
        profile_dict['patientPCPZip'] = patientPCPAddressZipCodeInput.get().strip()
        profile_dict['patientPCPPhone'] = patientPCPPhoneNumberInput.get().strip()
        profile_dict['patientPCPNPI'] = patientPCPNPIInput.get().strip()
        
        #get Cpt Row1 info from forms 
        profile_dict['itemRow1CPT'] = itemRow1Cpt.get().strip()
        profile_dict['itemRow1Modifier1'] = itemRow1Modifier1.get().strip()
        profile_dict['itemRow1Modifier2'] = itemRow1Modifier2.get().strip()
        profile_dict['itemRow1Modifier3'] = itemRow1Modifier3.get().strip()
        profile_dict['itemRow1Modifier4'] = itemRow1Modifier4.get().strip()
        profile_dict['itemRow1Description'] = itemRow1Description.get().strip()
        profile_dict['itemRow1Qty'] = itemRow1Qty.get().strip()
        profile_dict['itemRow1Price'] = itemRow1Price.get().strip()

        #get Cpt Row2 info from forms
        profile_dict['itemRow2CPT'] = itemRow2Cpt.get().strip()
        profile_dict['itemRow2Modifier1'] = itemRow2Modifier1.get().strip()
        profile_dict['itemRow2Modifier2'] = itemRow2Modifier2.get().strip()
        profile_dict['itemRow2Modifier3'] = itemRow2Modifier3.get().strip()
        profile_dict['itemRow2Modifier4'] = itemRow2Modifier4.get().strip()
        profile_dict['itemRow2Description'] = itemRow2Description.get().strip()
        profile_dict['itemRow2Qty'] = itemRow2Qty.get().strip()
        profile_dict['itemRow2Price'] = itemRow2Price.get().strip()

        #get Cpt Row3 info from forms
        profile_dict['itemRow3CPT'] = itemRow3Cpt.get().strip()
        profile_dict['itemRow3Modifier1'] = itemRow3Modifier1.get().strip()
        profile_dict['itemRow3Modifier2'] = itemRow3Modifier2.get().strip()
        profile_dict['itemRow3Modifier3'] = itemRow3Modifier3.get().strip()
        profile_dict['itemRow3Modifier4'] = itemRow3Modifier4.get().strip()
        profile_dict['itemRow3Description'] = itemRow3Description.get().strip()
        profile_dict['itemRow3Qty'] = itemRow3Qty.get().strip()
        profile_dict['itemRow3Price'] = itemRow3Price.get().strip()

        #get Cpt Row4 info from forms
        profile_dict['itemRow4CPT'] = itemRow4Cpt.get().strip()
        profile_dict['itemRow4Modifier1'] = itemRow4Modifier1.get().strip()
        profile_dict['itemRow4Modifier2'] = itemRow4Modifier2.get().strip()
        profile_dict['itemRow4Modifier3'] = itemRow4Modifier3.get().strip()
        profile_dict['itemRow4Modifier4'] = itemRow4Modifier4.get().strip()
        profile_dict['itemRow4Description'] = itemRow4Description.get().strip()
        profile_dict['itemRow4Qty'] = itemRow4Qty.get().strip()
        profile_dict['itemRow4Price'] = itemRow4Price.get().strip()

        #get Cpt Row5 info from forms 
        profile_dict['itemRow5CPT'] = itemRow5Cpt.get().strip()
        profile_dict['itemRow5Modifier1'] = itemRow5Modifier1.get().strip()
        profile_dict['itemRow5Modifier2'] = itemRow5Modifier2.get().strip()
        profile_dict['itemRow5Modifier3'] = itemRow5Modifier3.get().strip()
        profile_dict['itemRow5Modifier4'] = itemRow5Modifier4.get().strip()
        profile_dict['itemRow5Description'] = itemRow5Description.get().strip()
        profile_dict['itemRow5Qty'] = itemRow5Qty.get().strip()
        profile_dict['itemRow5Price'] = itemRow5Price.get().strip()

        #get Cpt Row6 info from forms 
        profile_dict['itemRow6CPT'] = itemRow6Cpt.get().strip()
        profile_dict['itemRow6Modifier1'] = itemRow6Modifier1.get().strip()
        profile_dict['itemRow6Modifier2'] = itemRow6Modifier2.get().strip()
        profile_dict['itemRow6Modifier3'] = itemRow6Modifier3.get().strip()
        profile_dict['itemRow6Modifier4'] = itemRow6Modifier4.get().strip()
        profile_dict['itemRow6Description'] = itemRow6Description.get().strip()
        profile_dict['itemRow6Qty'] = itemRow6Qty.get().strip()
        profile_dict['itemRow6Price'] = itemRow6Price.get().strip()

        #get diagnosis codes and descriptions from forms
        profile_dict['diagnosisCodeRow1'] = diagnosisCodeRow1.get().strip()
        profile_dict['diagnosisCodeRow2'] = diagnosisCodeRow2.get().strip()
        profile_dict['diagnosisCodeRow3'] = diagnosisCodeRow3.get().strip()
        profile_dict['diagnosisCodeRow4'] = diagnosisCodeRow4.get().strip()

        profile_dict['diagnosisCodeRow1Description'] = diagnosisCodeRow1Description.get().strip()
        profile_dict['diagnosisCodeRow2Description'] = diagnosisCodeRow2Description.get().strip()
        profile_dict['diagnosisCodeRow3Description'] = diagnosisCodeRow3Description.get().strip()
        profile_dict['diagnosisCodeRow4Description'] = diagnosisCodeRow4Description.get().strip()
        
        with open(currentProfile, 'wb') as handle:
            pickle.dump(profile_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        messagebox.showinfo(title="Error", message="No Patient Selected")

def donothing():
    print("Nothing")

def getProfileFromFile():
    try:
        global currentProfile 
        currentProfile = filedialog.askopenfilename(filetypes=[("Pickle Data Files", ".pickle")])
        with open(currentProfile, 'rb') as handle:
            b = pickle.load(handle)
        
        print(currentProfile)
        userName.delete(0,END)
        clearICD()
        clearCpt()
        clearPatient()
        clearDr()

        userName.insert(0,b["UserName"])
        value_inside_insurance.set(b["account"])
        
        #Set patient info from forms
        #invoiceCheck.set(b['makeInvoice'])
        #intakeCheck.set(b['makeIntake'])
        patientFirstNameInput.insert(0,b['patientFirstName'])
        patientLastNameInput.insert(0,b['patientLastName'])
        patientAddressInput.insert(0,b['patientAddress'])
        patientAddressCityInput.insert(0,b['patientCity'])
        value_inside_patient.set(b['patientState'])
        patientAddressZipCodeInput.insert(0,b['patientZip'])
        patientPhoneNumberInput.insert(0,b['patientPhone'])
        orderDateInput.insert(0,b['patientOrderDate'])
        patientInsuranceInput.insert(0,b['patientMBI'])
        patientPreauthorizationInput.insert(0,b['patientPreauthorization'])
        patientDateOfBirth.insert(0,b["patientDateOfBirth"])
        try:
            if(b['patientGender'] == 'Male'):
                genderCheck.set(0)
            else:
                genderCheck.set(1)
        except:
            print("Patient has no gender!?")
            genderCheck.set(0)
        #Set doctor info from forms
        patientPCPFirstNameInput.insert(0,b['patientPCPFirstName'])
        patientPCPLastNameInput.insert(0,b['patientPCPLastName'])
        patientPCPAddressInput.insert(0,b['patientPCPAddress'])
        patientPCPAddressCityInput.insert(0,b['patientPCPCity'])
        value_inside_doctor.set(b['patientPCPState'])
        patientPCPAddressZipCodeInput.insert(0,b['patientPCPZip'])
        patientPCPPhoneNumberInput.insert(0,b['patientPCPPhone'])
        patientPCPNPIInput.insert(0,b['patientPCPNPI'])
        
        #Set Cpt Row1 info from forms 
        itemRow1Cpt.insert(0,b['itemRow1CPT'] )
        itemRow1Modifier1.insert(0,b['itemRow1Modifier1'])
        itemRow1Modifier2.insert(0,b['itemRow1Modifier2'])
        itemRow1Modifier3.insert(0,b['itemRow1Modifier3'])
        itemRow1Modifier4.insert(0,b['itemRow1Modifier4'])
        itemRow1Description.insert(0,b['itemRow1Description'])
        itemRow1Qty.insert(0,b['itemRow1Qty'])
        itemRow1Price.insert(0,b['itemRow1Price'])

        #Set Cpt Row2 info from forms
        itemRow2Cpt.insert(0,b['itemRow2CPT'])
        itemRow2Modifier1.insert(0,b['itemRow2Modifier1'])
        itemRow2Modifier2.insert(0,b['itemRow2Modifier2'])
        itemRow2Modifier3.insert(0,b['itemRow2Modifier3'])
        itemRow2Modifier4.insert(0,b['itemRow2Modifier4'])
        itemRow2Description.insert(0,b['itemRow2Description'])
        itemRow2Qty.insert(0,b['itemRow2Qty'])
        itemRow2Price.insert(0,b['itemRow2Price'])

        #Set Cpt Row3 info from forms
        itemRow3Cpt.insert(0,b['itemRow3CPT'])
        itemRow3Modifier1.insert(0,b['itemRow3Modifier1'])
        itemRow3Modifier2.insert(0,b['itemRow3Modifier2'])
        itemRow3Modifier3.insert(0,b['itemRow3Modifier3'])
        itemRow3Modifier4.insert(0,b['itemRow3Modifier4'])
        itemRow3Description.insert(0,b['itemRow3Description'])
        itemRow3Qty.insert(0,b['itemRow3Qty'])
        itemRow3Price.insert(0,b['itemRow3Price'])

        #Set Cpt Row4 info from forms
        itemRow4Cpt.insert(0,b['itemRow4CPT'])
        itemRow4Modifier1.insert(0,b['itemRow4Modifier1'])
        itemRow4Modifier2.insert(0,b['itemRow4Modifier2'])
        itemRow4Modifier3.insert(0,b['itemRow4Modifier3'])
        itemRow4Modifier4.insert(0,b['itemRow4Modifier4'])
        itemRow4Description.insert(0,b['itemRow4Description'])
        itemRow4Qty.insert(0,b['itemRow4Qty'])
        itemRow4Price.insert(0,b['itemRow4Price'])

        #Set Cpt Row5 info from forms 
        itemRow5Cpt.insert(0,b['itemRow5CPT'])
        itemRow5Modifier1.insert(0,b['itemRow5Modifier1'])
        itemRow5Modifier2.insert(0,b['itemRow5Modifier2'])
        itemRow5Modifier3.insert(0,b['itemRow5Modifier3'])
        itemRow5Modifier4.insert(0,b['itemRow5Modifier4'])
        itemRow5Description.insert(0,b['itemRow5Description'])
        itemRow5Qty.insert(0,b['itemRow5Qty'])
        itemRow5Price.insert(0,b['itemRow5Price'])

        #Set Cpt Row6 info from forms 
        itemRow6Cpt.insert(0,b['itemRow6CPT'])
        itemRow6Modifier1.insert(0,b['itemRow6Modifier1'])
        itemRow6Modifier2.insert(0,b['itemRow6Modifier2'])
        itemRow6Modifier3.insert(0,b['itemRow6Modifier3'])
        itemRow6Modifier4.insert(0,b['itemRow6Modifier4'])
        itemRow6Description.insert(0,b['itemRow6Description'])
        itemRow6Qty.insert(0,b['itemRow6Qty'])
        itemRow6Price.insert(0,b['itemRow6Price'])

        #Set diagnosis codes and descriptions from forms
        diagnosisCodeRow1.insert(0,b['diagnosisCodeRow1'])
        diagnosisCodeRow2.insert(0,b['diagnosisCodeRow2'])
        diagnosisCodeRow3.insert(0,b['diagnosisCodeRow3'])
        diagnosisCodeRow4.insert(0,b['diagnosisCodeRow4'])

        diagnosisCodeRow1Description.insert(0,b['diagnosisCodeRow1Description'])
        diagnosisCodeRow2Description.insert(0,b['diagnosisCodeRow2Description'])
        diagnosisCodeRow3Description.insert(0,b['diagnosisCodeRow3Description'])
        diagnosisCodeRow4Description.insert(0,b['diagnosisCodeRow4Description'])

    except:
        messagebox.showinfo(title="Canceled", message="The dialog has been canceled")




def getProfileFromPDF():
    try:
        fileOfIds = filedialog.askopenfilename(filetypes=[("PDF File", "Invoice.pdf")])
        profile_data = readPDF(fileOfIds)
        print(profile_data)
        clearAll()

        input_fields = [
            (userName, "UserName"),
            (patientFirstNameInput, "patientFirstName"),
            (patientLastNameInput, "patientLastName"),
            (patientAddressInput, "patientAddress"),
            (patientAddressCityInput, "patientCity"),
            (patientAddressZipCodeInput, "patientZip"),
            (patientPhoneNumberInput, "patientPhone"),
            (orderDateInput, "patientOrderDate"),
            (patientInsuranceInput, "patientMBI"),
            (patientPreauthorizationInput, "patientPreauthorization"),
            (patientDateOfBirth, "patientDateOfBirth"),
            (patientPCPFirstNameInput, "patientPCPFirstName"),
            (patientPCPLastNameInput, "patientPCPLastName"),
            (patientPCPAddressInput, "patientPCPAddress"),
            (patientPCPAddressCityInput, "patientPCPCity"),
            (patientPCPAddressZipCodeInput, "patientPCPZip"),
            (patientPCPPhoneNumberInput, "patientPCPPhone"),
            (patientPCPNPIInput, "patientPCPNPI"),
            
            (itemRow1Cpt, "itemRow1CPT"),
            (itemRow1Modifier1, "itemRow1Modifier1"),
            (itemRow1Modifier2, "itemRow1Modifier2"),
            (itemRow1Modifier3, "itemRow1Modifier3"),
            (itemRow1Modifier4, "itemRow1Modifier4"),
            (itemRow1Description, "itemRow1Description"),
            (itemRow1Qty, "itemRow1Qty"),
            (itemRow1Price, "itemRow1Price"),

            (itemRow2Cpt, "itemRow2CPT"),
            (itemRow2Modifier1, "itemRow2Modifier1"),
            (itemRow2Modifier2, "itemRow2Modifier2"),
            (itemRow2Modifier3, "itemRow2Modifier3"),
            (itemRow2Modifier4, "itemRow2Modifier4"),
            (itemRow2Description, "itemRow2Description"),
            (itemRow2Qty, "itemRow2Qty"),
            (itemRow2Price, "itemRow2Price"),

            (itemRow3Cpt, "itemRow3CPT"),
            (itemRow3Modifier1, "itemRow3Modifier1"),
            (itemRow3Modifier2, "itemRow3Modifier2"),
            (itemRow3Modifier3, "itemRow3Modifier3"),
            (itemRow3Modifier4, "itemRow3Modifier4"),
            (itemRow3Description, "itemRow3Description"),
            (itemRow3Qty, "itemRow3Qty"),
            (itemRow3Price, "itemRow3Price"),

            (itemRow4Cpt, "itemRow4CPT"),
            (itemRow4Modifier1, "itemRow4Modifier1"),
            (itemRow4Modifier2, "itemRow4Modifier2"),
            (itemRow4Modifier3, "itemRow4Modifier3"),
            (itemRow4Modifier4, "itemRow4Modifier4"),
            (itemRow4Description, "itemRow4Description"),
            (itemRow4Qty, "itemRow4Qty"),
            (itemRow4Price, "itemRow4Price"),

            (itemRow5Cpt, "itemRow5CPT"),
            (itemRow5Modifier1, "itemRow5Modifier1"),
            (itemRow5Modifier2, "itemRow5Modifier2"),
            (itemRow5Modifier3, "itemRow5Modifier3"),
            (itemRow5Modifier4, "itemRow5Modifier4"),
            (itemRow5Description, "itemRow5Description"),
            (itemRow5Qty, "itemRow5Qty"),
            (itemRow5Price, "itemRow5Price"),

            (itemRow6Cpt, "itemRow6CPT"),
            (itemRow6Modifier1, "itemRow6Modifier1"),
            (itemRow6Modifier2, "itemRow6Modifier2"),
            (itemRow6Modifier3, "itemRow6Modifier3"),
            (itemRow6Modifier4, "itemRow6Modifier4"),
            (itemRow6Description, "itemRow6Description"),
            (itemRow6Qty, "itemRow6Qty"),
            (itemRow6Price, "itemRow6Price"),

            (diagnosisCodeRow1, "diagnosisCodeRow1"),
            (diagnosisCodeRow1Description, "diagnosisCodeRow1Description"),
            (diagnosisCodeRow2, "diagnosisCodeRow2"),
            (diagnosisCodeRow2Description, "diagnosisCodeRow2Description"),
            (diagnosisCodeRow3, "diagnosisCodeRow3"),
            (diagnosisCodeRow3Description, "diagnosisCodeRow3Description"),
            (diagnosisCodeRow4, "diagnosisCodeRow4"),
            (diagnosisCodeRow4Description, "diagnosisCodeRow4Description"),
        ]
        
        for field, key in input_fields:
            insert_data(field, profile_data.get(key, ""))

        patient_gender = profile_data.get("patientGender", "").lower()
        if patient_gender == "male":
            genderCheck.set(0)
        elif patient_gender == "female":
            genderCheck.set(1)
        else:
            print("Patient has no gender or it's not recognized")
            genderCheck.set(0)

    except FileNotFoundError:
        print("File not found or not selected")
    except Exception as e:
        messagebox.showinfo(title="Error", message=f"An error occurred: {e}")


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
toolmenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=clearAll)
filemenu.add_command(label="Open", command=getProfileFromFile)
filemenu.add_command(label="Save", command=saveProfile)
#filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Tools", menu=toolmenu)
toolmenu.add_command(label="Open PDF", command=getProfileFromPDF)
root.config(menu=menubar)

option_list=["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI"]
value_inside_patient=StringVar(root)
value_inside_patient.set("CA")

value_inside_doctor=StringVar(root)
value_inside_doctor.set("CA")

insurance_option_list=("IEHP", "Medicare", "Anthem Blue Cross", "Health Net", "Aetna","AlphaCare Medical Group", "Anthem Blue Cross of California", "Blue Cross - California", "Blue Shield - California", "Brand New Day", "CIGNA Health Plan", "Department of Labor-DEEOIC", "Humana", "TRICARE California (WEST-WPS)", "United HealthCare")
value_inside_insurance=StringVar(root)
value_inside_insurance.set("Medicare")

#User information form field
userNameLabel = Label(insuranceFrame, text="User Name")
insuranceList = OptionMenu(insuranceFrame, value_inside_insurance, *insurance_option_list, command = setInsuranceType)

#Patient INFORMATION FORM
userName = Entry(insuranceFrame, width = default_input_width)
patientFirstNameInput= Entry(patientFrame, width = default_input_width)
patientLastNameInput = Entry(patientFrame, width = default_input_width)
patientAddressInput = Entry(patientFrame, width = default_input_width)
patientAddressCityInput = Entry(patientFrame, width = default_input_width)
patientAddressZipCodeInput = Entry(patientFrame, width = 10)
patientAddressStateInput = OptionMenu(patientFrame, value_inside_patient, *option_list)
patientPhoneNumberInput = Entry(patientFrame, width = default_input_width)
patientDateOfBirth = Entry(patientFrame, width = default_input_width)
orderDateInput = Entry(patientFrame, width = default_input_width)
patientInsuranceInput = Entry(patientFrame, width = default_input_width)
patientPreauthorizationInput = Entry(patientFrame, width = default_input_width)
patientPCPFirstNameInput = Entry(doctorFrame, width = default_input_width)
patientPCPLastNameInput = Entry(doctorFrame, width = default_input_width)
patientPCPAddressInput = Entry(doctorFrame, width = default_input_width)
patientPCPAddressCityInput = Entry(doctorFrame, width = default_input_width)
patientPCPAddressZipCodeInput = Entry(doctorFrame, width = 10)
patientPCPAddressStateInput = OptionMenu(doctorFrame, value_inside_doctor, *option_list)
patientPCPPhoneNumberInput = Entry(doctorFrame, width = default_input_width)
patientPCPNPIInput = Entry(doctorFrame, width = default_input_width)


patientFirstNameLabel = Label(patientFrame, text="First Name")
patientLastNameLabel = Label(patientFrame, text="Last Name")
patientAddressLabel = Label(patientFrame, text="Street")
patientAddressCityLabel = Label(patientFrame, text="City")
patientAddressZipCodeLabel = Label(patientFrame, text="Zip")
patientAddressStateLabel = Label(patientFrame, text="State")
patientPhoneNumberLabel = Label(patientFrame, text="Phone Number")
orderDateLabel = Label(patientFrame, text="Date Of Service")
patientDateOfBirthLabel = Label(patientFrame, text="Date Of Birth")
patientInsuranceLabel = Label(patientFrame, text="Insurance ID")
patientPreauthorizationLabel = Label(patientFrame, text="Pre-auth")
patientPCPFirstNameLabel = Label(doctorFrame, text="First Name")
patientPCPLastNameLabel = Label(doctorFrame, text="Last Name")
patientPCPAddressLabel = Label(doctorFrame, text="Street")
patientPCPAddressCityLabel = Label(doctorFrame, text="City")
patientPCPAddressStateLabel = Label(doctorFrame, text="State")
patientPCPAddressZipCodeLabel = Label(doctorFrame, text="Zip")
patientPCPPhoneNumberLabel = Label(doctorFrame, text="Phone Number")
patientPCPNPILabel = Label(doctorFrame, text="NPI")

#CPT CODE ENTRY FORMS
itemRow1Cpt = Entry(itemsFrame, width = default_item_input_width)
itemRow2Cpt = Entry(itemsFrame, width = default_item_input_width)
itemRow3Cpt = Entry(itemsFrame, width = default_item_input_width)
itemRow4Cpt = Entry(itemsFrame, width = default_item_input_width)
itemRow5Cpt = Entry(itemsFrame, width = default_item_input_width)
itemRow6Cpt = Entry(itemsFrame, width = default_item_input_width)

itemRow1Modifier1 = Entry(itemsFrame, width=default_modifier_width)
itemRow1Modifier2 = Entry(itemsFrame, width=default_modifier_width)
itemRow1Modifier3 = Entry(itemsFrame, width=default_modifier_width)
itemRow1Modifier4 = Entry(itemsFrame, width=default_modifier_width)
itemRow1Qty = Entry(itemsFrame, width=default_modifier_width)
itemRow1Description = Entry(itemsFrame, width=default_input_width)
itemRow1Price = Entry(itemsFrame, width=default_modifier_width)

itemRow2Modifier1 = Entry(itemsFrame, width=default_modifier_width)
itemRow2Modifier2 = Entry(itemsFrame, width=default_modifier_width)
itemRow2Modifier3 = Entry(itemsFrame, width=default_modifier_width)
itemRow2Modifier4 = Entry(itemsFrame, width=default_modifier_width)
itemRow2Qty = Entry(itemsFrame, width=default_modifier_width)
itemRow2Description = Entry(itemsFrame, width=default_input_width)
itemRow2Price = Entry(itemsFrame, width=default_modifier_width)

itemRow3Modifier1 = Entry(itemsFrame, width=default_modifier_width)
itemRow3Modifier2 = Entry(itemsFrame, width=default_modifier_width)
itemRow3Modifier3 = Entry(itemsFrame, width=default_modifier_width)
itemRow3Modifier4 = Entry(itemsFrame, width=default_modifier_width)
itemRow3Qty = Entry(itemsFrame, width=default_modifier_width)
itemRow3Description = Entry(itemsFrame, width=default_input_width)
itemRow3Price = Entry(itemsFrame, width=default_modifier_width)

itemRow4Modifier1 = Entry(itemsFrame, width=default_modifier_width)
itemRow4Modifier2 = Entry(itemsFrame, width=default_modifier_width)
itemRow4Modifier3 = Entry(itemsFrame, width=default_modifier_width)
itemRow4Modifier4 = Entry(itemsFrame, width=default_modifier_width)
itemRow4Qty = Entry(itemsFrame, width=default_modifier_width)
itemRow4Description = Entry(itemsFrame, width=default_input_width)
itemRow4Price = Entry(itemsFrame, width=default_modifier_width)

itemRow5Modifier1 = Entry(itemsFrame, width=default_modifier_width)
itemRow5Modifier2 = Entry(itemsFrame, width=default_modifier_width)
itemRow5Modifier3 = Entry(itemsFrame, width=default_modifier_width)
itemRow5Modifier4 = Entry(itemsFrame, width=default_modifier_width)
itemRow5Qty = Entry(itemsFrame, width=default_modifier_width)
itemRow5Description = Entry(itemsFrame, width=default_input_width)
itemRow5Price = Entry(itemsFrame, width=default_modifier_width)

itemRow6Modifier1 = Entry(itemsFrame, width=default_modifier_width)
itemRow6Modifier2 = Entry(itemsFrame, width=default_modifier_width)
itemRow6Modifier3 = Entry(itemsFrame, width=default_modifier_width)
itemRow6Modifier4 = Entry(itemsFrame, width=default_modifier_width)
itemRow6Qty = Entry(itemsFrame, width=default_modifier_width)
itemRow6Description = Entry(itemsFrame, width=default_input_width)
itemRow6Price = Entry(itemsFrame, width=default_modifier_width)


itemsTitle = Label(itemsFrame, text="CPT Code")
itemsTitleMod1 = Label(itemsFrame, text="A")
itemsTitleMod2 = Label(itemsFrame, text="B")
itemsTitleMod3 = Label(itemsFrame, text="C")
itemsTitleMod4 = Label(itemsFrame, text="D")
itemsTitleQty = Label(itemsFrame, text="Qty")
itemsTitleDescription = Label(itemsFrame, text="Description")
itemRowPriceLabel = Label(itemsFrame, text="Price")


#Diagnosis ICD-10 CODES FORM ENTRY
diagnosisCode = Label(diagnosisFrame, text = "Diagnosis Code")
diagnosisDescription = Label(diagnosisFrame, text = "Diagnosis Description")

diagnosisCodeRow1 = Entry(diagnosisFrame, width = default_item_input_width)
diagnosisCodeRow2 = Entry(diagnosisFrame, width = default_item_input_width)
diagnosisCodeRow3 = Entry(diagnosisFrame, width = default_item_input_width)
diagnosisCodeRow4 = Entry(diagnosisFrame, width = default_item_input_width)

diagnosisCodeRow1Description = Entry(diagnosisFrame, width = default_ICD_Description_width)
diagnosisCodeRow2Description = Entry(diagnosisFrame, width = default_ICD_Description_width)
diagnosisCodeRow3Description = Entry(diagnosisFrame, width = default_ICD_Description_width)
diagnosisCodeRow4Description = Entry(diagnosisFrame, width = default_ICD_Description_width)


#BUTTONS FOR FORMS
submitButton = Button(submitFrame, text="Submit", command=sendToPDFCreator)
fillClaimFormButton = Button(submitFrame, text="Create Claim", command = sendToFillClaimForm)
searchButton = Button(itemsFrame, text="Search", command= getCPTInfo)
searchDrNPI = Button(doctorFrame, text="Search NPI", command=getNpiInfo)
searchICD = Button(diagnosisFrame, text="Search", command=getICDInfoFromPY)
clearDrForms = Button(doctorFrame, text="Clear", command=clearDr)
clearPatientForms = Button(patientFrame, text="Clear", command=clearPatient)
clearCptForms = Button(itemsFrame, text="Clear", command=clearCpt)
clearICDForms = Button(diagnosisFrame, text="Clear", command=clearICD)



invoiceCheck = IntVar()
intakeCheck = IntVar()

genderCheck = IntVar()

rentalCheckRow1 = IntVar()
rentalCheckRow2 = IntVar()
rentalCheckRow3 = IntVar()
rentalCheckRow4 = IntVar()
rentalCheckRow5 = IntVar()
rentalCheckRow6 = IntVar()

invoiceCheck.set(1)
intakeCheck.set(1)

genderCheck.set(0)

rentalCheckRow1.set(1)
rentalCheckRow2.set(1)
rentalCheckRow3.set(1)
rentalCheckRow4.set(1)
rentalCheckRow5.set(1)
rentalCheckRow6.set(1)

#insuranceTypeMedicare = Radiobutton(insuranceFrame, text="Medicare", variable=InsuranceType, value=0)
#insuranceTypeMedical = Radiobutton(insuranceFrame, text="Medi-Cal", variable=InsuranceType, value=1)

createInvoicePDF = Checkbutton(submitFrame, text="Create Invoice PDF", variable=invoiceCheck)
createIntakeSheetPDF = Checkbutton(submitFrame, text="Create Intake Sheet PDF", variable=intakeCheck)

rentalCheckMarkRow1 = Radiobutton(itemsFrame, text="RR", variable=rentalCheckRow1, value=0)
purchaseCheckMarkRow1 = Radiobutton(itemsFrame, text="NU", variable=rentalCheckRow1, value=1)

rentalCheckMarkRow2 = Radiobutton(itemsFrame, text="RR", variable=rentalCheckRow2, value=0)
purchaseCheckMarkRow2 = Radiobutton(itemsFrame, text="NU", variable=rentalCheckRow2, value=1)

rentalCheckMarkRow3 = Radiobutton(itemsFrame, text="RR", variable=rentalCheckRow3, value=0)
purchaseCheckMarkRow3 = Radiobutton(itemsFrame, text="NU", variable=rentalCheckRow3, value=1)

rentalCheckMarkRow4 = Radiobutton(itemsFrame, text="RR", variable=rentalCheckRow4, value=0)
purchaseCheckMarkRow4 = Radiobutton(itemsFrame, text="NU", variable=rentalCheckRow4, value=1)

rentalCheckMarkRow5 = Radiobutton(itemsFrame, text="RR", variable=rentalCheckRow5, value=0)
purchaseCheckMarkRow5 = Radiobutton(itemsFrame, text="NU", variable=rentalCheckRow5, value=1)

rentalCheckMarkRow6 = Radiobutton(itemsFrame, text="RR", variable=rentalCheckRow6, value=0)
purchaseCheckMarkRow6 = Radiobutton(itemsFrame, text="NU", variable=rentalCheckRow6, value=1)

isMale = Radiobutton(patientFrame, text="Male", variable=genderCheck, value=0)
isFemale = Radiobutton(patientFrame, text="Female", variable=genderCheck, value=1)


#insuranceTypeMedicare.grid(column=0,row=0)
#insuranceTypeMedical.grid(column=1,row=0)

insuranceList.grid(column=1, row=0, padx=5, pady=5, sticky="w")

userNameLabel.grid(column=0, row=1, padx=5, pady=5, sticky="e")
userName.grid(column=1, row=1, padx=5, pady=5)

patientFirstNameLabel.grid(column=0, row=0, padx=5, pady=5, sticky="e")
patientLastNameLabel.grid(column=0, row=1, padx=5, pady=5, sticky="e")
patientAddressLabel.grid(column=0, row=2, padx=5, pady=5, sticky="e")
patientAddressCityLabel.grid(column=0, row=3, padx=5, pady=5, sticky="e")
patientAddressStateLabel.grid(column=2, row=3, padx=5, pady=5, sticky="w")
patientAddressZipCodeLabel.grid(column=4, row=3, padx=5, pady=5, sticky="w")
patientPhoneNumberLabel.grid(column=0, row=4, padx=5, pady=5, sticky="e")
patientDateOfBirthLabel.grid(column=0, row=5, padx=5, pady=5, sticky="e")
isMale.grid(column=2, row=5, padx=5, pady=5, sticky="w")
isFemale.grid(column=3, row=5, padx=5, pady=5, sticky="w")
orderDateLabel.grid(column=0, row=6, padx=5, pady=5, sticky="e")
patientInsuranceLabel.grid(column=0, row=7, padx=5, pady=5, sticky="e")
patientPreauthorizationLabel.grid(column=0, row=8, padx=5, pady=5, sticky="e")

patientFirstNameInput.grid(column=1, row=0, padx=5, pady=5)
patientLastNameInput.grid(column=1, row=1, padx=5, pady=5)
patientAddressInput.grid(column=1, row=2, padx=5, pady=5)
patientAddressCityInput.grid(column=1,row=3, padx=5, pady=5)
patientAddressStateInput.grid(column=3, row=3, padx=5, pady=5)
patientAddressZipCodeInput.grid(column=5, row=3, padx=5, pady=5)
patientPhoneNumberInput.grid(column=1, row=4, padx=5, pady=5)
patientDateOfBirth.grid(column=1, row=5, padx=5, pady=5)
orderDateInput.grid(column=1, row=6, padx=5, pady=5)
patientInsuranceInput.grid(column=1, row=7, padx=5, pady=5)
patientPreauthorizationInput.grid(column=1, row=8, padx=5, pady=5)
clearPatientForms.grid(column=0, row=9, pady=5)

patientPCPFirstNameLabel.grid(column=0, row=0, padx=5, pady=5, sticky="e")
patientPCPLastNameLabel.grid(column=0, row=1, padx=5, pady=5, sticky="e")
patientPCPAddressLabel.grid(column=0, row=2, padx=5, pady=5, sticky="e")
patientPCPAddressCityLabel.grid(column=0, row=3, padx=5, pady=5, sticky="e")
patientPCPAddressStateLabel.grid(column=2, row=3, padx=5, pady=5, sticky="w")
patientPCPAddressZipCodeLabel.grid(column=4, row=3, padx=5, pady=5, sticky="w")
patientPCPPhoneNumberLabel.grid(column=0, row=4, padx=5, pady=5, sticky="e")
patientPCPNPILabel.grid(column=0, row=5, padx=5, pady=5, sticky="e")

patientPCPFirstNameInput.grid(column=1, row=0, padx=5, pady=5)
patientPCPLastNameInput.grid(column=1, row=1, padx=5, pady=5)
patientPCPAddressInput.grid(column=1, row=2, padx=5, pady=5)
patientPCPAddressCityInput.grid(column=1,row=3, padx=5, pady=5)
patientPCPAddressStateInput.grid(column=3, row=3, padx=5, pady=5)
patientPCPAddressZipCodeInput.grid(column=5, row=3, padx=5, pady=5)
patientPCPPhoneNumberInput.grid(column=1, row=4, padx=5, pady=5)
patientPCPNPIInput.grid(column=1, row=5, padx=5, pady=5)

itemsTitle.grid(column=2, row=0, padx=5, pady=5)
itemsTitleMod1.grid(column=3, row=0, padx=5, pady=5)
itemsTitleMod2.grid(column=4, row=0, padx=5, pady=5)
itemsTitleMod3.grid(column=5, row=0, padx=5, pady=5)
itemsTitleMod4.grid(column=6, row=0, padx=5, pady=5)
itemsTitleQty.grid(column=7, row=0, padx=5, pady=5)
itemsTitleDescription.grid(column=8,row=0, padx=5, pady=5)
itemRowPriceLabel.grid(column=9,row=0, padx=5, pady=5)

rentalCheckMarkRow1.grid(column=0, row = 1, padx=5, pady=5)
purchaseCheckMarkRow1.grid(column=1, row = 1, padx=5, pady=5)
itemRow1Cpt.grid(column=2, row = 1, padx=5, pady=5)
itemRow1Modifier1.grid(column=3, row = 1, padx=5, pady=5)
itemRow1Modifier2.grid(column=4, row = 1, padx=5, pady=5)
itemRow1Modifier3.grid(column=5, row = 1, padx=5, pady=5)
itemRow1Modifier4.grid(column=6, row = 1, padx=5, pady=5)
itemRow1Qty.grid(column=7, row = 1, padx=5, pady=5)
itemRow1Description.grid(column=8,row=1, padx=5, pady=5)
itemRow1Price.grid(column=9,row=1, padx=5, pady=5)

rentalCheckMarkRow2.grid(column=0, row=2, padx=5, pady=5)
purchaseCheckMarkRow2.grid(column=1, row=2, padx=5, pady=5)
itemRow2Cpt.grid(column=2, row = 2, padx=5, pady=5)
itemRow2Modifier1.grid(column=3, row = 2, padx=5, pady=5)
itemRow2Modifier2.grid(column=4, row = 2, padx=5, pady=5)
itemRow2Modifier3.grid(column=5, row = 2, padx=5, pady=5)
itemRow2Modifier4.grid(column=6, row = 2, padx=5, pady=5)
itemRow2Qty.grid(column=7, row = 2, padx=5, pady=5)
itemRow2Description.grid(column=8,row=2, padx=5, pady=5)
itemRow2Price.grid(column=9,row=2, padx=5, pady=5)

rentalCheckMarkRow3.grid(column=0, row=3, padx=5, pady=5)
purchaseCheckMarkRow3.grid(column=1,row=3, padx=5, pady=5)
itemRow3Cpt.grid(column=2, row = 3, padx=5, pady=5)
itemRow3Modifier1.grid(column=3, row = 3, padx=5, pady=5)
itemRow3Modifier2.grid(column=4, row = 3, padx=5, pady=5)
itemRow3Modifier3.grid(column=5, row = 3, padx=5, pady=5)
itemRow3Modifier4.grid(column=6, row = 3, padx=5, pady=5)
itemRow3Qty.grid(column=7, row = 3, padx=5, pady=5)
itemRow3Description.grid(column=8,row=3, padx=5, pady=5)
itemRow3Price.grid(column=9,row=3, padx=5, pady=5)

rentalCheckMarkRow4.grid(column=0, row = 4, padx=5, pady=5)
purchaseCheckMarkRow4.grid(column=1, row = 4, padx=5, pady=5)
itemRow4Cpt.grid(column=2, row = 4, padx=5, pady=5)
itemRow4Modifier1.grid(column=3, row = 4, padx=5, pady=5)
itemRow4Modifier2.grid(column=4, row = 4, padx=5, pady=5)
itemRow4Modifier3.grid(column=5, row = 4, padx=5, pady=5)
itemRow4Modifier4.grid(column=6, row = 4, padx=5, pady=5)
itemRow4Qty.grid(column=7, row = 4, padx=5, pady=5)
itemRow4Description.grid(column=8,row=4, padx=5, pady=5)
itemRow4Price.grid(column=9,row=4, padx=5, pady=5)

rentalCheckMarkRow5.grid(column=0, row=5, padx=5, pady=5)
purchaseCheckMarkRow5.grid(column=1, row = 5, padx=5, pady=5)
itemRow5Cpt.grid(column=2, row = 5, padx=5, pady=5)
itemRow5Modifier1.grid(column=3, row = 5, padx=5, pady=5)
itemRow5Modifier2.grid(column=4, row = 5, padx=5, pady=5)
itemRow5Modifier3.grid(column=5, row = 5, padx=5, pady=5)
itemRow5Modifier4.grid(column=6, row = 5, padx=5, pady=5)
itemRow5Qty.grid(column=7, row = 5, padx=5, pady=5)
itemRow5Description.grid(column=8,row=5, padx=5, pady=5)
itemRow5Price.grid(column=9,row=5, padx=5, pady=5)

rentalCheckMarkRow6.grid(column=0, row=6, padx=5, pady=5)
purchaseCheckMarkRow6.grid(column=1, row=6, padx=5, pady=5)
itemRow6Cpt.grid(column=2, row = 6, padx=5, pady=5)
itemRow6Modifier1.grid(column=3, row = 6, padx=5, pady=5)
itemRow6Modifier2.grid(column=4, row = 6, padx=5, pady=5)
itemRow6Modifier3.grid(column=5, row = 6, padx=5, pady=5)
itemRow6Modifier4.grid(column=6, row = 6, padx=5, pady=5)
itemRow6Qty.grid(column=7, row = 6, padx=5, pady=5)
itemRow6Description.grid(column=8,row=6, padx=5, pady=5)
itemRow6Price.grid(column=9,row=6, padx=5, pady=5)

diagnosisCode.grid(column=0,row=0, padx=5, pady=5)
diagnosisDescription.grid(column=1,row=0, padx=5, pady=5)

diagnosisCodeRow1.grid(column=0,row=1, padx=5, pady=5)
diagnosisCodeRow1Description.grid(column=1,row=1, padx=5, pady=5)

diagnosisCodeRow2.grid(column=0,row=2, padx=5, pady=5)
diagnosisCodeRow2Description.grid(column=1,row=2, padx=5, pady=5)

diagnosisCodeRow3.grid(column=0,row=3, padx=5, pady=5)
diagnosisCodeRow3Description.grid(column=1,row=3, padx=5, pady=5)

diagnosisCodeRow4.grid(column=0,row=4, padx=5, pady=5)
diagnosisCodeRow4Description.grid(column=1,row=4, padx=5, pady=5)
clearICDForms.grid(column=1,row=5, padx=5, pady=5)

searchButton.grid(column=0,row=7, padx=5, pady=5)
clearCptForms.grid(column=1,row=7, padx=5, pady=5)

createInvoicePDF.grid(column=0, row=0, padx=5, pady=5)
createIntakeSheetPDF.grid(column=1, row=0, padx=5, pady=5)
submitButton.grid(column=2, row=0, padx=5, pady=5)
fillClaimFormButton.grid(column=3, row=0, padx=5, pady=5)
searchDrNPI.grid(column=5, row=5, padx=5, pady=5)
clearDrForms.grid(column=0,row=6, padx=5, pady=5)
searchICD.grid(column=0,row=5, padx=5, pady=5)

insuranceFrame.grid(column=0, row=0, padx=5, pady=5)
patientFrame.grid(column=0, row=1, padx=10, pady=10)
itemsFrame.grid(column=1, row=1, padx=10, pady=10)
doctorFrame.grid(column=0, row=2, padx=10, pady=10)
submitFrame.grid(column=0, row=3, padx=10, pady=10)
diagnosisFrame.grid(column=1,row=2, padx=10, pady=10)

root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_columnconfigure(3,weight=1)
root.grid_columnconfigure(4,weight=1)
root.grid_columnconfigure(5,weight=1)
root.grid_columnconfigure(6,weight=1)
root.grid_columnconfigure(7,weight=1)
root.grid_columnconfigure(8,weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)


root.update()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()