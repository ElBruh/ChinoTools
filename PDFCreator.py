from doctest import testfile
import pdfrw
from datetime import datetime
import pickle
import sys
import os
import re


temp_dict = {
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
    'patientMBI': '',
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

data_dictInvoice = {
    'CUST PHONE Row1' : '',
    'ORDER DATERow1' : '',
    'DELIVERY DATERow1' : '',
    'SHIP TORow1' : '',
    'INSURANCE INFORMATIONRow1' : '',
    'SALESPERSONRow1' : '',
    'ACCN Row1' : '',
    #'MANUFRow1' : profile_dict['itemRow1CPT'],
    #'ITEMLOTRow1' : profile_dict['itemRow1CPT'],
    'DESCRIPTIONRow1' : '',
    'BILLING CODERow1' : '',
    'QTYRow1' : '',
    'UnitPriceRow1' : '',
    'DOCTORRow1' : '',
    #'MANUFRow2' : profile_dict['itemRow2CPT'],
    #'ITEMLOTRow2' : profile_dict['itemRow2CPT'],
    'DESCRIPTIONRow2' : '',
    'BILLING CODERow2' : '',
    'QTYRow2' : '',
    'UnitPriceRow2' : '',

    #'MANUFRow3' : profile_dict['itemRow3CPT'],
    #'ITEMLOTRow3' : profile_dict['itemRow3CPT'],
    'DESCRIPTIONRow3' : '',
    'BILLING CODERow3' : '',
    'QTYRow3' : '',
    'UnitPriceRow3' : '',

    #'MANUFRow4' : profile_dict['itemRow4CPT'],
    #'ITEMLOTRow4' : profile_dict['itemRow4CPT'],
    'DESCRIPTIONRow4' : '',
    'BILLING CODERow4' : '',
    'QTYRow4' : '',
    'UnitPriceRow4' : '',

    #'MANUFRow5' : profile_dict['itemRow5CPT'],
    #'ITEMLOTRow5' : profile_dict['itemRow5CPT'],
    'DESCRIPTIONRow5' : '',
    'BILLING CODERow5' : '',
    'QTYRow5' : '',
    'UnitPriceRow5' : '',

    #'MANUFRow6' : profile_dict['itemRow6CPT'],
    #'ITEMLOTRow6' : profile_dict['itemRow6CPT'],
    'DESCRIPTIONRow6' : '',
    'BILLING CODERow6' : '',
    'QTYRow6' : '',
    'UnitPriceRow6' : '',
}

#def saveProfile(profile_dict):

def makePDF(myPDF, myDict, Name, profile_dict):
    print("made it to makePDF")
    new_date = datetime.now()
    some_date = new_date.strftime("%B.%d.%Y--%I.%M.%S%p ")
    
    for page in myPDF.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    #print(key)
                
                    if key in myDict.keys():
                        #print("found {}".format(key))
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(myDict[key]))
                        )
    if(os.path.exists('./Output/{}'.format(profile_dict['patientLastName'].upper() + "_" + profile_dict['patientFirstName'].upper())) == False):
        os.makedirs('./Output/{}'.format(profile_dict['patientLastName'].upper() + "_" + profile_dict['patientFirstName'].upper()))
        pdfrw.PdfWriter().write('./Output/{}/{}.pdf'.format(profile_dict['patientLastName'] + "_" + profile_dict['patientFirstName'],Name), myPDF)
        with open('./Output/{}/{}-{}-data.pickle'.format(profile_dict['patientLastName'] + "_" + profile_dict['patientFirstName'], profile_dict['patientLastName'] + "_" + profile_dict['patientFirstName'], some_date), 'wb') as handle:
            pickle.dump(profile_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        pdfrw.PdfWriter().write('./Output/{}/{}.pdf'.format(profile_dict['patientLastName'] + "_" + profile_dict['patientFirstName'],Name), myPDF)
        with open('./Output/{}/{}-{}-data.pickle'.format(profile_dict['patientLastName'] + "_" + profile_dict['patientFirstName'], profile_dict['patientLastName'] + "_" + profile_dict['patientFirstName'], some_date), 'wb') as handle:
            pickle.dump(profile_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('./Output/{}/Communication_Log {}.txt'.format(profile_dict['patientLastName'] + "_" + profile_dict['patientFirstName'], str(some_date)), 'w') as f:
        f.write("Communication Log for " + profile_dict['patientFirstName'].upper() + "_" + profile_dict['patientLastName'].upper() + "\n" + "Created on " + str(some_date))
    
    print("Created PDF!")

def readPDF(myPDF):
    try:
        testPDF = pdfrw.PdfReader(myPDF)
        testPDF.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    except:
        print("No File Found")

    newDict = data_dictInvoice
    invoiceDict = temp_dict
    for page in testPDF.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    value = annotation[ANNOT_VAL_KEY]
                    first = re.sub(r'[()]', '', str(value))
                    second = re.sub(r'[\\]', '', str(first))
                    final = re.sub(r'[<>]', '', str(second))
                    #print(key)
                    #print(final)
                
                    if key in newDict.keys():
                        newDict[key] = final
    invoiceDict["patientPhone"] = newDict["CUST PHONE Row1"]
    invoiceDict["patientOrderDate"] = newDict["ORDER DATERow1"]
    invoiceDict["patientFirstName"] = newDict["SHIP TORow1"].partition("\n")[0].partition(" ")[0]
    invoiceDict["patientLastName"] = newDict["SHIP TORow1"].partition("\n")[0].partition(" ")[2]
    invoiceDict["patientAddress"] = newDict["SHIP TORow1"].partition("\n")[2].partition("\n")[0]
    invoiceDict["patientCity"] = newDict["SHIP TORow1"].partition("\n")[2].partition("\n")[2].partition("\n")[0].partition(" ")[0]
    invoiceDict["patientState"] = newDict["SHIP TORow1"].partition("\n")[2].partition("\n")[2].partition("\n")[0].partition(" ")[2].partition(" ")[0]
    invoiceDict["patientZip"] = newDict["SHIP TORow1"].partition("\n")[2].partition("\n")[2].partition("\n")[0].partition(" ")[2].partition(" ")[2]
    invoiceDict["patientMBI"] = newDict["INSURANCE INFORMATIONRow1"].partition("\n")[0]
    invoiceDict["patientPreauthorization"] = newDict["INSURANCE INFORMATIONRow1"].partition("\n")[2]
    
    invoiceDict["UserName"] = newDict["SALESPERSONRow1"]
    invoiceDict["account"] = newDict["ACCN Row1"]
    
    invoiceDict["itemRow1Description"] = newDict["DESCRIPTIONRow1"]
    invoiceDict["itemRow1CPT"] = newDict["BILLING CODERow1"]
    invoiceDict["itemRow1Qty"] = newDict["QTYRow1"]
    invoiceDict["itemRow1Price"] = newDict["UnitPriceRow1"]

    invoiceDict["itemRow2Description"] = newDict["DESCRIPTIONRow2"]
    invoiceDict["itemRow2CPT"] = newDict["BILLING CODERow2"]
    invoiceDict["itemRow2Qty"] = newDict["QTYRow2"]
    invoiceDict["itemRow2Price"] = newDict["UnitPriceRow2"]

    invoiceDict["itemRow3Description"] = newDict["DESCRIPTIONRow3"]
    invoiceDict["itemRow3CPT"] = newDict["BILLING CODERow3"]
    invoiceDict["itemRow3Qty"] = newDict["QTYRow3"]
    invoiceDict["itemRow3Price"] = newDict["UnitPriceRow3"]

    invoiceDict["itemRow4Description"] = newDict["DESCRIPTIONRow4"]
    invoiceDict["itemRow4CPT"] = newDict["BILLING CODERow4"]
    invoiceDict["itemRow4Qty"] = newDict["QTYRow4"]
    invoiceDict["itemRow4Price"] = newDict["UnitPriceRow4"]

    invoiceDict["itemRow5Description"] = newDict["DESCRIPTIONRow5"]
    invoiceDict["itemRow5CPT"] = newDict["BILLING CODERow5"]
    invoiceDict["itemRow5Qty"] = newDict["QTYRow5"]
    invoiceDict["itemRow5Price"] = newDict["UnitPriceRow5"]

    invoiceDict["itemRow6Description"] = newDict["DESCRIPTIONRow6"]
    invoiceDict["itemRow6CPT"] = newDict["BILLING CODERow6"]
    invoiceDict["itemRow6Qty"] = newDict["QTYRow6"]
    invoiceDict["itemRow6Price"] = newDict["UnitPriceRow6"]
    
    invoiceDict["patientPCPFirstName"] = newDict["DOCTORRow1"].partition("\n")[0].partition(" ")[0]
    invoiceDict["patientPCPLastName"] = newDict["DOCTORRow1"].partition("\n")[0].partition(" ")[2]
    invoiceDict["patientPCPAddress"] = newDict["DOCTORRow1"].partition("\n")[2].partition("\n")[0]
    invoiceDict["patientPCPCity"] = newDict["DOCTORRow1"].partition("\n")[2].partition("\n")[2].partition("\n")[0].partition(" ")[0]
    invoiceDict["patientPCPState"] = newDict["DOCTORRow1"].partition("\n")[2].partition("\n")[2].partition("\n")[0].partition(" ")[2].partition(" ")[0]
    invoiceDict["patientPCPZip"] = newDict["DOCTORRow1"].partition("\n")[2].partition("\n")[2].partition("\n")[0].partition(" ")[2].partition(" ")[2]
    invoiceDict["patientPCPPhone"] = newDict["DOCTORRow1"].partition("\n")[2].partition("\n")[2].partition("\n")[2].partition("\n")[0]
    invoiceDict["patientPCPNPI"] = newDict["DOCTORRow1"].partition("\n")[2].partition("\n")[2].partition("\n")[2].partition("\n")[2]

    return invoiceDict


def formatInput(profile_dict):
    print(profile_dict["patientGender"])
    new_date = datetime.now()
    some_date = new_date.strftime("%B.%d.%Y--%I.%M.%S%p ")
    moddedPDF = pdf
    moddedPDF1 = pdf1
    if(profile_dict['makeInvoice'] == 1):
        data_dictForInvoice = {
            'CUST PHONE Row1' : profile_dict['patientPhone'],
            'ORDER DATERow1' : profile_dict['patientOrderDate'],
            'DELIVERY DATERow1' : profile_dict['patientOrderDate'],

            'SHIP TORow1' : (profile_dict['patientFirstName'] + " " + profile_dict['patientLastName'] + " \n" + 
                        profile_dict['patientAddress'] + "\n" + 
                        profile_dict['patientCity'] + " " + profile_dict['patientState'] + " " + profile_dict['patientZip']),

            'INSURANCE INFORMATIONRow1' : ("ID: " + profile_dict['patientMBI'] + "\n"+ profile_dict['patientPreauthorization']),
            'SALESPERSONRow1' : profile_dict['UserName'].upper(),
            'ACCN Row1' : profile_dict['account'].upper(),

            #'MANUFRow1' : profile_dict['itemRow1CPT'],
            #'ITEMLOTRow1' : profile_dict['itemRow1CPT'],

            'DESCRIPTIONRow1' : profile_dict['itemRow1Description'].upper(),
            'BILLING CODERow1' : profile_dict['itemRow1CPT'].upper(),
            'QTYRow1' : profile_dict['itemRow1Qty'],
            'UnitPriceRow1' : profile_dict['itemRow1Price'],

            'DOCTORRow1' : (profile_dict['patientPCPFirstName'] + " " + profile_dict['patientPCPLastName'] + " \n" + 
                        profile_dict['patientPCPAddress'] + "\n" + 
                        profile_dict['patientPCPCity'] + " " + profile_dict['patientPCPState'] + " " + profile_dict['patientPCPZip'] + " \n" +
                        profile_dict['patientPCPPhone'] + " \n" +
                        profile_dict['patientPCPNPI']
                        ),
            #'MANUFRow2' : profile_dict['itemRow2CPT'],
            #'ITEMLOTRow2' : profile_dict['itemRow2CPT'],
            'DESCRIPTIONRow2' : profile_dict['itemRow2Description'].upper(),
            'BILLING CODERow2' : profile_dict['itemRow2CPT'].upper(),
            'QTYRow2' : profile_dict['itemRow2Qty'],
            'UnitPriceRow2' : profile_dict['itemRow2Price'],

            #'MANUFRow3' : profile_dict['itemRow3CPT'],
            #'ITEMLOTRow3' : profile_dict['itemRow3CPT'],
            'DESCRIPTIONRow3' : profile_dict['itemRow3Description'].upper(),
            'BILLING CODERow3' : profile_dict['itemRow3CPT'].upper(),
            'QTYRow3' : profile_dict['itemRow3Qty'],
            'UnitPriceRow3' : profile_dict['itemRow3Price'],

            #'MANUFRow4' : profile_dict['itemRow4CPT'],
            #'ITEMLOTRow4' : profile_dict['itemRow4CPT'],
            'DESCRIPTIONRow4' : profile_dict['itemRow4Description'].upper(),
            'BILLING CODERow4' : profile_dict['itemRow4CPT'].upper(),
            'QTYRow4' : profile_dict['itemRow4Qty'],
            'UnitPriceRow4' : profile_dict['itemRow4Price'],

            #'MANUFRow5' : profile_dict['itemRow5CPT'],
            #'ITEMLOTRow5' : profile_dict['itemRow5CPT'],
            'DESCRIPTIONRow5' : profile_dict['itemRow5Description'].upper(),
            'BILLING CODERow5' : profile_dict['itemRow5CPT'].upper(),
            'QTYRow5' : profile_dict['itemRow5Qty'],
            'UnitPriceRow5' : profile_dict['itemRow5Price'],

            #'MANUFRow6' : profile_dict['itemRow6CPT'],
            #'ITEMLOTRow6' : profile_dict['itemRow6CPT'],
            'DESCRIPTIONRow6' : profile_dict['itemRow6Description'].upper(),
            'BILLING CODERow6' : profile_dict['itemRow6CPT'].upper(),
            'QTYRow6' : profile_dict['itemRow6Qty'],
            'UnitPriceRow6' : profile_dict['itemRow6Price'],
        }
        makePDF(moddedPDF, data_dictForInvoice, (profile_dict['patientFirstName'] + "_" + profile_dict['patientLastName'] + "_" + str(some_date) + "Invoice"), profile_dict)
    if(profile_dict['makeIntake'] == 1):
        data_dictForIntake = {
            'PatientPhone' : profile_dict['patientPhone'],
            'OrderReceivedBy': profile_dict['UserName'].upper(),
            'OrderReceivedDate' : profile_dict['patientOrderDate'],
            'OrderDispensedDate' : profile_dict['patientOrderDate'],
            'PatientName':profile_dict['patientFirstName'] + " " + profile_dict["patientLastName"],
            'PatientAddress':profile_dict['patientAddress'],
            'PatientCityState':profile_dict['patientCity'] + " " + profile_dict['patientState'],
            'PatientZip':profile_dict['patientZip'],
            'PatientDOB':profile_dict['patientDateOfBirth'] + " " + profile_dict['patientGender'],
            'InsuranceInformation': profile_dict['account'].upper(),
            'MBI':profile_dict['patientMBI'] + "\n",
            'MembersName':profile_dict['patientFirstName'] + " " + profile_dict["patientLastName"],
            'PatientName1':profile_dict['patientFirstName'] + " " + profile_dict["patientLastName"],
            'ClinicalInformationRow2': profile_dict['itemRow1Description'].upper() + "\n" +
            profile_dict['itemRow2Description'].upper() + "\n"+
            profile_dict['itemRow3Description'].upper() + "\n"+
            profile_dict['itemRow4Description'].upper() + "\n"+
            profile_dict['itemRow5Description'].upper() + "\n"+
            profile_dict['itemRow6Description'].upper() + "\n",

            'DoctorName':profile_dict['patientPCPFirstName'] + " " + profile_dict['patientPCPLastName'],
            'DoctorPhone':profile_dict['patientPCPPhone'],
            'DoctorAddress':profile_dict['patientPCPAddress'],
            'DoctorCityState':profile_dict['patientPCPCity'] + " " + profile_dict['patientPCPState'] + " " + profile_dict['patientPCPZip'],
            'DoctorNPI':profile_dict['patientPCPNPI'],
            
            'CPTRow1' : profile_dict['itemRow1CPT'].upper(),
            'CPtRow2' : profile_dict['itemRow2CPT'].upper(),
            'CPTRow3' : profile_dict['itemRow3CPT'].upper(),
            'CPTRow4' : profile_dict['itemRow4CPT'].upper(),
            'CPTRow5' : profile_dict['itemRow5CPT'].upper(),
            'CPTRow6' : profile_dict['itemRow6CPT'].upper(),
            'CPTAllowableRow1':profile_dict['itemRow1Price'],
            'CPTAllowableRow2':profile_dict['itemRow2Price'],
            'CPTAllowableRow3':profile_dict['itemRow3Price'],
            'CPTAllowableRow4':profile_dict['itemRow4Price'],
            'CPTAllowableRow5':profile_dict['itemRow5Price'],
            'CPTAllowableRow6':profile_dict['itemRow6Price'],

            'ItemDescription':profile_dict['itemRow1Description'].upper() + "\n" +
            profile_dict['itemRow2Description'].upper() + "\n"+
            profile_dict['itemRow3Description'].upper() + "\n"+
            profile_dict['itemRow4Description'].upper() + "\n"+
            profile_dict['itemRow5Description'].upper() + "\n"+
            profile_dict['itemRow6Description'].upper() + "\n",
            
            'ClinicalInformationRow1': profile_dict['diagnosisCodeRow1'].upper() + " " + profile_dict['diagnosisCodeRow1Description'].upper() + "\n" +
            profile_dict['diagnosisCodeRow2'].upper() + " " + profile_dict['diagnosisCodeRow2Description'].upper() + "\n"+
            profile_dict['diagnosisCodeRow3'].upper() + " " + profile_dict['diagnosisCodeRow3Description'].upper() + "\n"+
            profile_dict['diagnosisCodeRow4'].upper() + " " + profile_dict['diagnosisCodeRow4Description'].upper(),
            
            
            
        }
        makePDF(moddedPDF1, data_dictForIntake, (profile_dict['patientFirstName'] + "_" + profile_dict['patientLastName'] + "_" + str(some_date) + "Intake"), profile_dict)
    else:
        print("No Intake Sheet Created")    


directory = sys.executable#
baseDir = os.path.dirname(directory)
try:
    pdf_path = (baseDir + "/src/" + "BlankInvoice(edit).pdf")
    pdf = pdfrw.PdfReader(pdf_path)
    pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
except:
    pdf_path = ("./src/BlankInvoice(edit).pdf")
    pdf = pdfrw.PdfReader(pdf_path)
    print("Testing File")
try:
    
    pdf_path1 = (baseDir + "/src/" + "OrderIntakeSheet(edit).pdf")
    pdf1 = pdfrw.PdfReader(pdf_path1)
    pdf1.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
except:
    pdf_path1 = "./src/OrderIntakeSheet(edit).pdf"
    pdf1 = pdfrw.PdfReader(pdf_path1)
    print("Testing File")

try:
    testPDFPath = (baseDir + "/src/" + "testPDF.pdf")
    testPDF = pdfrw.PdfReader(testPDFPath)
    testPDF.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
except:
    testPDFPath = ("src/testPDF.pdf")
    print("Testing File")





#pdf_path1 = "./src/OrderIntakeSheet(edit).pdf"
#pdf_path = ""





ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

#print(readPDF(testPDF))
#test_dict = {"test":"test"}
#new_date = datetime.now()
#some_date = new_date.strftime("%B.%d.%Y--%H.%M.%S ")
#print(some_date)
#makePDF(pdf, test_dict,"Test" )




#print(pdf)
