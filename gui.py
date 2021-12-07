from tkinter import *
from typing import Counter
import pdfrw
import sqlite3
import os
from PDFCreator import formatInput
from DatabaseTest import searchMedicalCPT, searchMedicareCPT
default_input_width = 20
default_item_input_width = 10
default_modifier_width = 5
root = Tk()

root.title("Create Patient Profile")

profile_dict ={
    'makeInvoice':1,
    'makeIntake':1,
    'patientOrderDate':'',
    'patientLastName':'',
    'patientAddress':'',
    'patientCity':'',
    'patientState':'',
    'patientZip':'',
    'patientPhone':'',
    'patientOrderDate':'',    
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
}

patientFrame = LabelFrame(root, text='Patient',  bd=2, relief=RIDGE)
doctorFrame = LabelFrame(root, text='Doctor', bd=2, relief=RIDGE)
submitFrame = Frame(root, relief=RIDGE)
itemsFrame = LabelFrame(root, text='Items', relief=RIDGE)
insuranceFrame = LabelFrame(root, text="Insurance Type", relief=RIDGE)

#cptRatesFile = open("MEDI-CALRATES.csv", "r")

def getCPTInfo():
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

    if(InsuranceType.get() == 1):
        details = searchMedicalCPT(query, options)
    elif(InsuranceType.get() == 0):
        details = searchMedicareCPT(query, options)

    #IF Medicare NU
    if(InsuranceType.get() == 0 and rentalCheckRow1.get() == 1 and itemRow1Cpt.get() != ""):
        itemRow1Modifier1.delete(0,END)
        itemRow1Modifier1.insert(0,"NU")
        itemRow1Modifier2.delete(0,END)
        itemRow1Modifier2.insert(0,"KX")
        itemRow1Modifier3.delete(0,END)
        itemRow1Modifier4.delete(0,END)
    if(InsuranceType.get() == 0 and rentalCheckRow2.get() == 1 and itemRow2Cpt.get() != ""):
        itemRow2Modifier1.delete(0,END)
        itemRow2Modifier1.insert(0,"NU")
        itemRow2Modifier2.delete(0,END)
        itemRow2Modifier2.insert(0,"KX")
        itemRow2Modifier3.delete(0,END)
        itemRow2Modifier4.delete(0,END)
    if(InsuranceType.get() == 0 and rentalCheckRow3.get() == 1 and itemRow3Cpt.get() != ""):
        itemRow3Modifier1.delete(0,END)
        itemRow3Modifier1.insert(0,"NU")
        itemRow3Modifier2.delete(0,END)
        itemRow3Modifier2.insert(0,"KX")
        itemRow3Modifier3.delete(0,END)
        itemRow3Modifier4.delete(0,END)
    if(InsuranceType.get() == 0 and rentalCheckRow4.get() == 1 and itemRow4Cpt.get() != ""):
        itemRow4Modifier1.delete(0,END)
        itemRow4Modifier1.insert(0,"NU")
        itemRow4Modifier2.delete(0,END)
        itemRow4Modifier2.insert(0,"KX")
        itemRow4Modifier3.delete(0,END)
        itemRow4Modifier4.delete(0,END)
    if(InsuranceType.get() == 0 and rentalCheckRow5.get() == 1 and itemRow5Cpt.get() != ""):
        itemRow5Modifier1.delete(0,END)
        itemRow5Modifier1.insert(0,"NU")
        itemRow5Modifier2.delete(0,END)
        itemRow5Modifier2.insert(0,"KX")
        itemRow5Modifier3.delete(0,END)
        itemRow5Modifier4.delete(0,END)
    if(InsuranceType.get() == 0 and rentalCheckRow6.get() == 1 and itemRow6Cpt.get() != ""):
        itemRow6Modifier1.delete(0,END)
        itemRow6Modifier1.insert(0,"NU")
        itemRow6Modifier2.delete(0,END)
        itemRow6Modifier2.insert(0,"KX")
        itemRow6Modifier3.delete(0,END)
        itemRow6Modifier4.delete(0,END)
    #IF Medicare RR
    if(InsuranceType.get() == 0 and rentalCheckRow1.get() == 0 and itemRow1Cpt.get() != ""):
        itemRow1Modifier1.delete(0,END)
        itemRow1Modifier1.insert(0,"RR")
        itemRow1Modifier2.delete(0,END)
        itemRow1Modifier2.insert(0,"KH")
        itemRow1Modifier3.delete(0,END)
        itemRow1Modifier3.insert(0,"KX")
        itemRow1Modifier4.delete(0,END)
    if(InsuranceType.get() == 0 and rentalCheckRow2.get() == 0 and itemRow2Cpt.get() != ""):
        itemRow2Modifier1.delete(0,END)
        itemRow2Modifier1.insert(0,"RR")
        itemRow2Modifier2.delete(0,END)
        itemRow2Modifier2.insert(0,"KH")
        itemRow2Modifier3.delete(0,END)
        itemRow2Modifier3.insert(0,"KX")
        itemRow2Modifier4.delete(0,END)
    if(InsuranceType.get() == 0 and rentalCheckRow3.get() == 0 and itemRow3Cpt.get() != ""):
        itemRow3Modifier1.delete(0,END)
        itemRow3Modifier1.insert(0,"RR")
        itemRow3Modifier2.delete(0,END)
        itemRow3Modifier2.insert(0,"KH")
        itemRow3Modifier3.delete(0,END)
        itemRow3Modifier3.insert(0,"KX")
        itemRow3Modifier4.delete(0,END)
    if(InsuranceType.get() == 0 and rentalCheckRow4.get() == 0 and itemRow4Cpt.get() != ""):
        itemRow4Modifier1.delete(0,END)
        itemRow4Modifier1.insert(0,"RR")
        itemRow4Modifier2.delete(0,END)
        itemRow4Modifier2.insert(0,"KH")
        itemRow4Modifier3.delete(0,END)
        itemRow4Modifier3.insert(0,"KX")
        itemRow4Modifier4.delete(0,END)
    if(InsuranceType.get() == 0 and rentalCheckRow5.get() == 0 and itemRow5Cpt.get() != ""):
        itemRow5Modifier1.delete(0,END)
        itemRow5Modifier1.insert(0,"RR")
        itemRow5Modifier2.delete(0,END)
        itemRow5Modifier2.insert(0,"KH")
        itemRow5Modifier3.delete(0,END)
        itemRow5Modifier3.insert(0,"KX")
        itemRow5Modifier4.delete(0,END)
    if(InsuranceType.get() == 0 and rentalCheckRow6.get() == 0 and itemRow6Cpt.get() != ""):
        itemRow6Modifier1.delete(0,END)
        itemRow6Modifier1.insert(0,"RR")
        itemRow6Modifier2.delete(0,END)
        itemRow6Modifier2.insert(0,"KH")
        itemRow6Modifier3.delete(0,END)
        itemRow6Modifier3.insert(0,"KX")
        itemRow6Modifier4.delete(0,END)

    #IF Medical NU
    if(InsuranceType.get() == 1 and rentalCheckRow1.get() == 1 and itemRow1Cpt.get() != ""):
        itemRow1Modifier1.delete(0,END)
        itemRow1Modifier1.insert(0,"NU")
        itemRow1Modifier2.delete(0,END)
        itemRow1Modifier3.delete(0,END)
        itemRow1Modifier4.delete(0,END)
    if(InsuranceType.get() == 1 and rentalCheckRow2.get() == 1 and itemRow2Cpt.get() != ""):
        itemRow2Modifier1.delete(0,END)
        itemRow2Modifier1.insert(0,"NU")
        itemRow2Modifier2.delete(0,END)
        itemRow2Modifier3.delete(0,END)
        itemRow2Modifier4.delete(0,END)
    if(InsuranceType.get() == 1 and rentalCheckRow3.get() == 1 and itemRow3Cpt.get() != ""):
        itemRow3Modifier1.delete(0,END)
        itemRow3Modifier1.insert(0,"NU")
        itemRow3Modifier2.delete(0,END)
        itemRow3Modifier3.delete(0,END)
        itemRow3Modifier4.delete(0,END)
    if(InsuranceType.get() == 1 and rentalCheckRow4.get() == 1 and itemRow4Cpt.get() != ""):
        itemRow4Modifier1.delete(0,END)
        itemRow4Modifier1.insert(0,"NU")
        itemRow4Modifier2.delete(0,END)
        itemRow4Modifier3.delete(0,END)
        itemRow4Modifier4.delete(0,END)
    if(InsuranceType.get() == 1 and rentalCheckRow5.get() == 1 and itemRow5Cpt.get() != ""):
        itemRow5Modifier1.delete(0,END)
        itemRow5Modifier1.insert(0,"NU")
        itemRow5Modifier2.delete(0,END)
        itemRow5Modifier3.delete(0,END)
        itemRow5Modifier4.delete(0,END)
    if(InsuranceType.get() == 1 and rentalCheckRow6.get() == 1 and itemRow6Cpt.get() != ""):
        itemRow6Modifier1.delete(0,END)
        itemRow6Modifier1.insert(0,"NU")
        itemRow6Modifier2.delete(0,END)
        itemRow6Modifier3.delete(0,END)
        itemRow6Modifier4.delete(0,END)

    #IF Medical RR
    if(InsuranceType.get() == 1 and rentalCheckRow1.get() == 0 and itemRow1Cpt.get() != ""):
        itemRow1Modifier1.delete(0,END)
        itemRow1Modifier1.insert(0,"RR")
        itemRow1Modifier2.delete(0,END)
        itemRow1Modifier3.delete(0,END)
        itemRow1Modifier4.delete(0,END)
    if(InsuranceType.get() == 1 and rentalCheckRow2.get() == 0 and itemRow2Cpt.get() != ""):
        itemRow2Modifier1.delete(0,END)
        itemRow2Modifier1.insert(0,"RR")
        itemRow2Modifier2.delete(0,END)
        itemRow2Modifier3.delete(0,END)
        itemRow2Modifier4.delete(0,END)
    if(InsuranceType.get() == 1 and rentalCheckRow3.get() == 0 and itemRow3Cpt.get() != ""):
        itemRow3Modifier1.delete(0,END)
        itemRow3Modifier1.insert(0,"RR")
        itemRow3Modifier2.delete(0,END)
        itemRow3Modifier3.delete(0,END)
        itemRow3Modifier4.delete(0,END)
    if(InsuranceType.get() == 1 and rentalCheckRow4.get() == 0 and itemRow4Cpt.get() != ""):
        itemRow4Modifier1.delete(0,END)
        itemRow4Modifier1.insert(0,"RR")
        itemRow4Modifier2.delete(0,END)
        itemRow4Modifier3.delete(0,END)
        itemRow4Modifier4.delete(0,END)
    if(InsuranceType.get() == 1 and rentalCheckRow5.get() == 0 and itemRow5Cpt.get() != ""):
        itemRow5Modifier1.delete(0,END)
        itemRow5Modifier1.insert(0,"RR")
        itemRow5Modifier2.delete(0,END)
        itemRow5Modifier3.delete(0,END)
        itemRow5Modifier4.delete(0,END)
    if(InsuranceType.get() == 1 and rentalCheckRow6.get() == 0 and itemRow6Cpt.get() != ""):
        itemRow6Modifier1.delete(0,END)
        itemRow6Modifier1.insert(0,"RR")
        itemRow6Modifier2.delete(0,END)
        itemRow6Modifier3.delete(0,END)
        itemRow6Modifier4.delete(0,END)
    
    print(details)
    itemRow1Price.delete(0,END)
    itemRow1Price.insert(0,details[0])

    itemRow1Description.delete(0, END)
    itemRow1Description.insert(0, details[1])

    itemRow2Price.delete(0,END)
    itemRow2Price.insert(0,details[2])

    itemRow2Description.delete(0, END)
    itemRow2Description.insert(0, details[3])

    itemRow3Price.delete(0,END)
    itemRow3Price.insert(0,details[4])

    itemRow3Description.delete(0, END)
    itemRow3Description.insert(0, details[5])

    itemRow4Price.delete(0,END)
    itemRow4Price.insert(0,details[6])

    itemRow4Description.delete(0, END)
    itemRow4Description.insert(0, details[7])

    itemRow5Price.delete(0,END)
    itemRow5Price.insert(0,details[8])

    itemRow5Description.delete(0, END)
    itemRow5Description.insert(0, details[9])

    itemRow6Price.delete(0,END)
    itemRow6Price.insert(0,details[10])

    itemRow6Description.delete(0, END)
    itemRow6Description.insert(0, details[11])




def sendToPDFCreator():
    #print(e)
    

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
    
    

    formatInput(profile_dict)
    #os.system("python PDFCreator.py {} {} {} {} \"{}\" {} {} {} {} {} {} {} {}".format(a,b,c,d,e,f,g,h,i,j,k,l,m))


option_list=["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI"]
value_inside_patient=StringVar(root)
value_inside_patient.set("CA")

value_inside_doctor=StringVar(root)
value_inside_doctor.set("CA")



patientFirstNameInput= Entry(patientFrame, width = default_input_width)
patientLastNameInput = Entry(patientFrame, width = default_input_width)
patientAddressInput = Entry(patientFrame, width = default_input_width)
patientAddressCityInput = Entry(patientFrame, width = default_input_width)
patientAddressZipCodeInput = Entry(patientFrame, width = 10)
patientAddressStateInput = OptionMenu(patientFrame, value_inside_patient, *option_list)
patientPhoneNumberInput = Entry(patientFrame, width = default_input_width)
orderDateInput = Entry(patientFrame, width = default_input_width)
patientDateOfBirth = Entry(patientFrame, width = default_input_width)
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
patientInsuranceLabel = Label(patientFrame, text="MBI")
patientPreauthorizationLabel = Label(patientFrame, text="Pre-auth")
patientPCPFirstNameLabel = Label(doctorFrame, text="First Name")
patientPCPLastNameLabel = Label(doctorFrame, text="Last Name")
patientPCPAddressLabel = Label(doctorFrame, text="Street")
patientPCPAddressCityLabel = Label(doctorFrame, text="City")
patientPCPAddressStateLabel = Label(doctorFrame, text="State")
patientPCPAddressZipCodeLabel = Label(doctorFrame, text="Zip")
patientPCPPhoneNumberLabel = Label(doctorFrame, text="Phone Number")
patientPCPNPILabel = Label(doctorFrame, text="NPI")


itemRow1Cpt = Entry(itemsFrame, width = default_item_input_width)
itemRow1Modifier1 = Entry(itemsFrame, width=default_modifier_width)
itemRow1Modifier2 = Entry(itemsFrame, width=default_modifier_width)
itemRow1Modifier3 = Entry(itemsFrame, width=default_modifier_width)
itemRow1Modifier4 = Entry(itemsFrame, width=default_modifier_width)
itemRow1Qty = Entry(itemsFrame, width=default_modifier_width)
itemRow1Description = Entry(itemsFrame, width=default_input_width)
itemRow1Price = Entry(itemsFrame, width=default_modifier_width)

itemRow2Cpt = Entry(itemsFrame, width = default_item_input_width)
itemRow2Modifier1 = Entry(itemsFrame, width=default_modifier_width)
itemRow2Modifier2 = Entry(itemsFrame, width=default_modifier_width)
itemRow2Modifier3 = Entry(itemsFrame, width=default_modifier_width)
itemRow2Modifier4 = Entry(itemsFrame, width=default_modifier_width)
itemRow2Qty = Entry(itemsFrame, width=default_modifier_width)
itemRow2Description = Entry(itemsFrame, width=default_input_width)
itemRow2Price = Entry(itemsFrame, width=default_modifier_width)

itemRow3Cpt = Entry(itemsFrame, width = default_item_input_width)
itemRow3Modifier1 = Entry(itemsFrame, width=default_modifier_width)
itemRow3Modifier2 = Entry(itemsFrame, width=default_modifier_width)
itemRow3Modifier3 = Entry(itemsFrame, width=default_modifier_width)
itemRow3Modifier4 = Entry(itemsFrame, width=default_modifier_width)
itemRow3Qty = Entry(itemsFrame, width=default_modifier_width)
itemRow3Description = Entry(itemsFrame, width=default_input_width)
itemRow3Price = Entry(itemsFrame, width=default_modifier_width)

itemRow4Cpt = Entry(itemsFrame, width = default_item_input_width)
itemRow4Modifier1 = Entry(itemsFrame, width=default_modifier_width)
itemRow4Modifier2 = Entry(itemsFrame, width=default_modifier_width)
itemRow4Modifier3 = Entry(itemsFrame, width=default_modifier_width)
itemRow4Modifier4 = Entry(itemsFrame, width=default_modifier_width)
itemRow4Qty = Entry(itemsFrame, width=default_modifier_width)
itemRow4Description = Entry(itemsFrame, width=default_input_width)
itemRow4Price = Entry(itemsFrame, width=default_modifier_width)

itemRow5Cpt = Entry(itemsFrame, width = default_item_input_width)
itemRow5Modifier1 = Entry(itemsFrame, width=default_modifier_width)
itemRow5Modifier2 = Entry(itemsFrame, width=default_modifier_width)
itemRow5Modifier3 = Entry(itemsFrame, width=default_modifier_width)
itemRow5Modifier4 = Entry(itemsFrame, width=default_modifier_width)
itemRow5Qty = Entry(itemsFrame, width=default_modifier_width)
itemRow5Description = Entry(itemsFrame, width=default_input_width)
itemRow5Price = Entry(itemsFrame, width=default_modifier_width)

itemRow6Cpt = Entry(itemsFrame, width = default_item_input_width)
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



submitButton = Button(submitFrame, text="Submit", command=sendToPDFCreator)
searchButton = Button(itemsFrame, text="Search", command= getCPTInfo)

InsuranceType = IntVar()


invoiceCheck = IntVar()
intakeCheck = IntVar()

rentalCheckRow1 = IntVar()
rentalCheckRow2 = IntVar()
rentalCheckRow3 = IntVar()
rentalCheckRow4 = IntVar()
rentalCheckRow5 = IntVar()
rentalCheckRow6 = IntVar()

InsuranceType.set(0)

invoiceCheck.set(1)
intakeCheck.set(1)

rentalCheckRow1.set(1)
rentalCheckRow2.set(1)
rentalCheckRow3.set(1)
rentalCheckRow4.set(1)
rentalCheckRow5.set(1)
rentalCheckRow6.set(1)

insuranceTypeMedicare = Radiobutton(insuranceFrame, text="Medicare", variable=InsuranceType, value=0)
insuranceTypeMedical = Radiobutton(insuranceFrame, text="Medi-Cal", variable=InsuranceType, value=1)

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


insuranceTypeMedicare.grid(column=0,row=0)
insuranceTypeMedical.grid(column=1,row=0)

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

orderDateLabel.grid(column=0, row=5)
orderDateInput.grid(column=1, row=5)

patientInsuranceLabel.grid(column=0, row=6)
patientInsuranceInput.grid(column=1, row=6)

patientPreauthorizationLabel.grid(column=0, row=7)
patientPreauthorizationInput.grid(column=1, row=7)

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

searchButton.grid(column=0,row=7)


createInvoicePDF.grid(column=0, row=0)
createIntakeSheetPDF.grid(column=1, row=0)
submitButton.grid(column=2, row=0)

insuranceFrame.grid(column=0, row=0, padx=0, pady=0)
patientFrame.grid(column=0, row=1, padx=10, pady=10)
itemsFrame.grid(column=1, row=1, padx=10, pady=10)
doctorFrame.grid(column=0, row=2, padx=10, pady=10)
submitFrame.grid(column=0, row=3, padx=10, pady=10)


root.mainloop()