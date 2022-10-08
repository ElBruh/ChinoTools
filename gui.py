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

def getICDInfoFromPY():
    
    if(diagnosisCodeRow1.get() != ""):

        try:
            tempDict = getICDInfo(diagnosisCodeRow1.get())
            diagnosisCodeRow1Description.delete(0,END)
            diagnosisCodeRow1.delete(0,END)
            diagnosisCodeRow1Description.insert(0, "-" +  tempDict['Description'])
            diagnosisCodeRow1.insert(0,tempDict['Name'])
        except:
            messagebox.showerror(title="Error", message="ICD 10 code {} Not Found!".format(diagnosisCodeRow1.get()),)
    
    if(diagnosisCodeRow2.get() != ""):

        try:
            tempDict = getICDInfo(diagnosisCodeRow2.get())
            diagnosisCodeRow2Description.delete(0,END)
            diagnosisCodeRow2.delete(0,END)
            diagnosisCodeRow2Description.insert(0, "-" +  tempDict['Description'])
            diagnosisCodeRow2.insert(0,tempDict['Name'])
        except:
            messagebox.showerror(title="Error", message="ICD 10 code {} Not Found!".format(diagnosisCodeRow2.get()),)
    
    if(diagnosisCodeRow3.get() != ""):

        try:
            tempDict = getICDInfo(diagnosisCodeRow3.get())
            diagnosisCodeRow3Description.delete(0,END)
            diagnosisCodeRow3.delete(0,END)
            diagnosisCodeRow3Description.insert(0, "-" + tempDict['Description'])
            diagnosisCodeRow3.insert(0,tempDict['Name'])
        except:
            messagebox.showerror(title="Error", message="ICD 10 code {} Not Found!".format(diagnosisCodeRow3.get()),)
    
    if(diagnosisCodeRow4.get() != ""):

        try:
            tempDict = getICDInfo(diagnosisCodeRow4.get())
            diagnosisCodeRow4Description.delete(0,END)
            diagnosisCodeRow4.delete(0,END)
            diagnosisCodeRow4Description.insert(0, "-" +  tempDict['Description'])
            diagnosisCodeRow4.insert(0,tempDict['Name'])
        except:
            messagebox.showerror(title="Error", message="ICD 10 code {} Not Found!".format(diagnosisCodeRow4.get()),)
    
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
    profile_dict["UserName"] = userName.get()
    profile_dict["account"] = value_inside_insurance.get()
    #get patient info from forms
    profile_dict['makeInvoice'] = invoiceCheck.get()
    profile_dict['makeIntake'] = intakeCheck.get()
    profile_dict['patientFirstName'] = patientFirstNameInput.get()
    profile_dict['patientLastName'] = patientLastNameInput.get()
    profile_dict['patientAddress'] = patientAddressInput.get()
    profile_dict['patientCity'] = patientAddressCityInput.get()
    profile_dict['patientState'] = value_inside_patient.get()
    profile_dict['patientZip'] = patientAddressZipCodeInput.get()
    profile_dict['patientPhone'] = patientPhoneNumberInput.get()
    profile_dict['patientOrderDate'] = orderDateInput.get()
    profile_dict['patientMBI'] = patientInsuranceInput.get()
    profile_dict['patientPreauthorization'] = patientPreauthorizationInput.get()
    profile_dict["patientDateOfBirth"] = patientDateOfBirth.get()

    #get doctor info from forms
    profile_dict['patientPCPFirstName'] = patientPCPFirstNameInput.get()
    profile_dict['patientPCPLastName'] = patientPCPLastNameInput.get()
    profile_dict['patientPCPAddress'] = patientPCPAddressInput.get()
    profile_dict['patientPCPCity'] = patientPCPAddressCityInput.get()
    profile_dict['patientPCPState'] = value_inside_doctor.get()
    profile_dict['patientPCPZip'] = patientPCPAddressZipCodeInput.get()
    profile_dict['patientPCPPhone'] = patientPCPPhoneNumberInput.get()
    profile_dict['patientPCPNPI'] = patientPCPNPIInput.get()
    
    #get Cpt Row1 info from forms 
    profile_dict['itemRow1CPT'] = itemRow1Cpt.get()
    profile_dict['itemRow1Modifier1'] = itemRow1Modifier1.get()
    profile_dict['itemRow1Modifier2'] = itemRow1Modifier2.get()
    profile_dict['itemRow1Modifier3'] = itemRow1Modifier3.get()
    profile_dict['itemRow1Modifier4'] = itemRow1Modifier4.get()
    profile_dict['itemRow1Description'] = itemRow1Description.get().strip()
    profile_dict['itemRow1Qty'] = itemRow1Qty.get()
    profile_dict['itemRow1Price'] = itemRow1Price.get()

    #get Cpt Row2 info from forms
    profile_dict['itemRow2CPT'] = itemRow2Cpt.get()
    profile_dict['itemRow2Modifier1'] = itemRow2Modifier1.get()
    profile_dict['itemRow2Modifier2'] = itemRow2Modifier2.get()
    profile_dict['itemRow2Modifier3'] = itemRow2Modifier3.get()
    profile_dict['itemRow2Modifier4'] = itemRow2Modifier4.get()
    profile_dict['itemRow2Description'] = itemRow2Description.get().strip()
    profile_dict['itemRow2Qty'] = itemRow2Qty.get()
    profile_dict['itemRow2Price'] = itemRow2Price.get()

    #get Cpt Row3 info from forms
    profile_dict['itemRow3CPT'] = itemRow3Cpt.get()
    profile_dict['itemRow3Modifier1'] = itemRow3Modifier1.get()
    profile_dict['itemRow3Modifier2'] = itemRow3Modifier2.get()
    profile_dict['itemRow3Modifier3'] = itemRow3Modifier3.get()
    profile_dict['itemRow3Modifier4'] = itemRow3Modifier4.get()
    profile_dict['itemRow3Description'] = itemRow3Description.get().strip()
    profile_dict['itemRow3Qty'] = itemRow3Qty.get()
    profile_dict['itemRow3Price'] = itemRow3Price.get()

    #get Cpt Row4 info from forms
    profile_dict['itemRow4CPT'] = itemRow4Cpt.get()
    profile_dict['itemRow4Modifier1'] = itemRow4Modifier1.get()
    profile_dict['itemRow4Modifier2'] = itemRow4Modifier2.get()
    profile_dict['itemRow4Modifier3'] = itemRow4Modifier3.get()
    profile_dict['itemRow4Modifier4'] = itemRow4Modifier4.get()
    profile_dict['itemRow4Description'] = itemRow4Description.get().strip()
    profile_dict['itemRow4Qty'] = itemRow4Qty.get()
    profile_dict['itemRow4Price'] = itemRow4Price.get()

    #get Cpt Row5 info from forms 
    profile_dict['itemRow5CPT'] = itemRow5Cpt.get()
    profile_dict['itemRow5Modifier1'] = itemRow5Modifier1.get()
    profile_dict['itemRow5Modifier2'] = itemRow5Modifier2.get()
    profile_dict['itemRow5Modifier3'] = itemRow5Modifier3.get()
    profile_dict['itemRow5Modifier4'] = itemRow5Modifier4.get()
    profile_dict['itemRow5Description'] = itemRow5Description.get().strip()
    profile_dict['itemRow5Qty'] = itemRow5Qty.get()
    profile_dict['itemRow5Price'] = itemRow5Price.get()

    #get Cpt Row6 info from forms 
    profile_dict['itemRow6CPT'] = itemRow6Cpt.get()
    profile_dict['itemRow6Modifier1'] = itemRow6Modifier1.get()
    profile_dict['itemRow6Modifier2'] = itemRow6Modifier2.get()
    profile_dict['itemRow6Modifier3'] = itemRow6Modifier3.get()
    profile_dict['itemRow6Modifier4'] = itemRow6Modifier4.get()
    profile_dict['itemRow6Description'] = itemRow6Description.get().strip()
    profile_dict['itemRow6Qty'] = itemRow6Qty.get()
    profile_dict['itemRow6Price'] = itemRow6Price.get()

    #get diagnosis codes and descriptions from forms
    profile_dict['diagnosisCodeRow1'] = diagnosisCodeRow1.get()
    profile_dict['diagnosisCodeRow2'] = diagnosisCodeRow2.get()
    profile_dict['diagnosisCodeRow3'] = diagnosisCodeRow3.get()
    profile_dict['diagnosisCodeRow4'] = diagnosisCodeRow4.get()

    profile_dict['diagnosisCodeRow1Description'] = diagnosisCodeRow1Description.get()
    profile_dict['diagnosisCodeRow2Description'] = diagnosisCodeRow2Description.get()
    profile_dict['diagnosisCodeRow3Description'] = diagnosisCodeRow3Description.get()
    profile_dict['diagnosisCodeRow4Description'] = diagnosisCodeRow4Description.get()
    
    
    try:
        formatInput(profile_dict)
        messagebox.showinfo(title="Success!", message="PDFs have been created!")
    except:
        messagebox.showerror(title="Error!", message="An error has occured")
    #os.system("python PDFCreator.py {} {} {} {} \"{}\" {} {} {} {} {} {} {} {}".format(a,b,c,d,e,f,g,h,i,j,k,l,m))

def donothing():
    print("Nothing")

def getProfileFromFile():
    try:
        fileOfIds = filedialog.askopenfilename(filetypes=[("Pickle Data Files", ".pickle")])
        with open(fileOfIds, 'rb') as handle:
            b = pickle.load(handle)
        
        clearAll()

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
        #print(fileOfIds)
        b = readPDF(fileOfIds)
        print(b)
        clearAll()

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



menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=clearAll)
filemenu.add_command(label="Open", command=getProfileFromFile)
filemenu.add_command(label="Open PDF", command=getProfileFromPDF)
#filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
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
fillClaimFormButton = Button(submitFrame, text="Create Claim", command = fillClaimFormFunction)
searchButton = Button(itemsFrame, text="Search", command= getCPTInfo)
searchDrNPI = Button(doctorFrame, text="Search NPI", command=getNpiInfo)
searchICD = Button(diagnosisFrame, text="Search", command=getICDInfoFromPY)
clearDrForms = Button(doctorFrame, text="Clear", command=clearDr)
clearPatientForms = Button(patientFrame, text="Clear", command=clearPatient)
clearCptForms = Button(itemsFrame, text="Clear", command=clearCpt)
clearICDForms = Button(diagnosisFrame, text="Clear", command=clearICD)



invoiceCheck = IntVar()
intakeCheck = IntVar()

rentalCheckRow1 = IntVar()
rentalCheckRow2 = IntVar()
rentalCheckRow3 = IntVar()
rentalCheckRow4 = IntVar()
rentalCheckRow5 = IntVar()
rentalCheckRow6 = IntVar()



invoiceCheck.set(1)
intakeCheck.set(1)

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


#insuranceTypeMedicare.grid(column=0,row=0)
#insuranceTypeMedical.grid(column=1,row=0)

insuranceList.grid(column=1,row=0)

userNameLabel.grid(column=0,row=1)
userName.grid(column=1, row=1)

patientFirstNameLabel.grid(column=0, row=0)
patientFirstNameInput.grid(column=1, row=0)

patientLastNameLabel.grid(column=0, row=1)
patientLastNameInput.grid(column=1, row=1)

patientAddressLabel.grid(column=0, row=2)
patientAddressInput.grid(column=1, row=2)

patientAddressCityLabel.grid(column=0, row=3)
patientAddressCityInput.grid(column=1, row=3)

patientAddressStateLabel.grid(column=2, row=3)
patientAddressStateInput.grid(column=3, row=3)

patientAddressZipCodeLabel.grid(column=4, row=3)
patientAddressZipCodeInput.grid(column=5, row=3, padx=10)

patientPhoneNumberLabel.grid(column=0, row=4)
patientPhoneNumberInput.grid(column=1, row=4)

patientDateOfBirthLabel.grid(column = 0, row = 5)
patientDateOfBirth.grid(column= 1, row = 5)

orderDateLabel.grid(column=0, row=6)
orderDateInput.grid(column=1, row=6)

patientInsuranceLabel.grid(column=0, row=7)
patientInsuranceInput.grid(column=1, row=7)

patientPreauthorizationLabel.grid(column=0, row=8)
patientPreauthorizationInput.grid(column=1, row=8)

clearPatientForms.grid(column=0, row=9)

patientPCPFirstNameLabel.grid(column=0, row=0)
patientPCPFirstNameInput.grid(column=1, row=0)

patientPCPLastNameLabel.grid(column=0, row=1)
patientPCPLastNameInput.grid(column=1, row=1)

patientPCPAddressLabel.grid(column=0, row=2)
patientPCPAddressInput.grid(column=1, row=2)

patientPCPAddressCityLabel.grid(column=0, row=3)
patientPCPAddressCityInput.grid(column=1,row=3)

patientPCPAddressStateLabel.grid(column=2, row=3)
patientPCPAddressStateInput.grid(column=3, row=3)

patientPCPAddressZipCodeLabel.grid(column=4, row=3)
patientPCPAddressZipCodeInput.grid(column=5, row=3, padx=10)

patientPCPPhoneNumberLabel.grid(column=0, row=4)
patientPCPPhoneNumberInput.grid(column=1, row=4)

patientPCPNPILabel.grid(column=0, row=5)
patientPCPNPIInput.grid(column=1, row=5)


itemsTitle.grid(column=2, row=0)
itemsTitleMod1.grid(column=3, row=0)
itemsTitleMod2.grid(column=4, row=0)
itemsTitleMod3.grid(column=5, row=0)
itemsTitleMod4.grid(column=6, row=0)
itemsTitleQty.grid(column=7, row=0)
itemsTitleDescription.grid(column=8,row=0)
itemRowPriceLabel.grid(column=9,row=0)


rentalCheckMarkRow1.grid(column=0, row = 1)
purchaseCheckMarkRow1.grid(column=1, row = 1)
itemRow1Cpt.grid(column=2, row = 1)
itemRow1Modifier1.grid(column=3, row = 1)
itemRow1Modifier2.grid(column=4, row = 1)
itemRow1Modifier3.grid(column=5, row = 1)
itemRow1Modifier4.grid(column=6, row = 1)
itemRow1Qty.grid(column=7, row = 1)
itemRow1Description.grid(column=8,row=1)
itemRow1Price.grid(column=9,row=1)

rentalCheckMarkRow2.grid(column=0, row=2)
purchaseCheckMarkRow2.grid(column=1, row=2)
itemRow2Cpt.grid(column=2, row = 2)
itemRow2Modifier1.grid(column=3, row = 2)
itemRow2Modifier2.grid(column=4, row = 2)
itemRow2Modifier3.grid(column=5, row = 2)
itemRow2Modifier4.grid(column=6, row = 2)
itemRow2Qty.grid(column=7, row = 2)
itemRow2Description.grid(column=8,row=2)
itemRow2Price.grid(column=9,row=2)

rentalCheckMarkRow3.grid(column=0, row=3)
purchaseCheckMarkRow3.grid(column=1,row=3)
itemRow3Cpt.grid(column=2, row = 3)
itemRow3Modifier1.grid(column=3, row = 3)
itemRow3Modifier2.grid(column=4, row = 3)
itemRow3Modifier3.grid(column=5, row = 3)
itemRow3Modifier4.grid(column=6, row = 3)
itemRow3Qty.grid(column=7, row = 3)
itemRow3Description.grid(column=8,row=3)
itemRow3Price.grid(column=9,row=3)

rentalCheckMarkRow4.grid(column=0, row = 4)
purchaseCheckMarkRow4.grid(column=1, row = 4)
itemRow4Cpt.grid(column=2, row = 4)
itemRow4Modifier1.grid(column=3, row = 4)
itemRow4Modifier2.grid(column=4, row = 4)
itemRow4Modifier3.grid(column=5, row = 4)
itemRow4Modifier4.grid(column=6, row = 4)
itemRow4Qty.grid(column=7, row = 4)
itemRow4Description.grid(column=8,row=4)
itemRow4Price.grid(column=9,row=4)

rentalCheckMarkRow5.grid(column=0, row=5)
purchaseCheckMarkRow5.grid(column=1, row = 5)
itemRow5Cpt.grid(column=2, row = 5)
itemRow5Modifier1.grid(column=3, row = 5)
itemRow5Modifier2.grid(column=4, row = 5)
itemRow5Modifier3.grid(column=5, row = 5)
itemRow5Modifier4.grid(column=6, row = 5)
itemRow5Qty.grid(column=7, row = 5)
itemRow5Description.grid(column=8,row=5)
itemRow5Price.grid(column=9,row=5)

rentalCheckMarkRow6.grid(column=0, row=6)
purchaseCheckMarkRow6.grid(column=1, row=6)
itemRow6Cpt.grid(column=2, row = 6)
itemRow6Modifier1.grid(column=3, row = 6)
itemRow6Modifier2.grid(column=4, row = 6)
itemRow6Modifier3.grid(column=5, row = 6)
itemRow6Modifier4.grid(column=6, row = 6)
itemRow6Qty.grid(column=7, row = 6)
itemRow6Description.grid(column=8,row=6)
itemRow6Price.grid(column=9,row=6)


diagnosisCode.grid(column=0,row=0)
diagnosisDescription.grid(column=1,row=0)

diagnosisCodeRow1.grid(column=0,row=1)
diagnosisCodeRow1Description.grid(column=1,row=1)

diagnosisCodeRow2.grid(column=0,row=2)
diagnosisCodeRow2Description.grid(column=1,row=2)

diagnosisCodeRow3.grid(column=0,row=3)
diagnosisCodeRow3Description.grid(column=1,row=3)

diagnosisCodeRow4.grid(column=0,row=4)
diagnosisCodeRow4Description.grid(column=1,row=4)
clearICDForms.grid(column=1,row=5)

searchButton.grid(column=0,row=7)
clearCptForms.grid(column=1,row=7)

createInvoicePDF.grid(column=0, row=0)
createIntakeSheetPDF.grid(column=1, row=0)
submitButton.grid(column=2, row=0)
fillClaimFormButton.grid(column=3, row=0)
searchDrNPI.grid(column=5, row=5)
clearDrForms.grid(column=0,row=6)
searchICD.grid(column=0,row=5)


insuranceFrame.grid(column=0, row=0, padx=0, pady=0)
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