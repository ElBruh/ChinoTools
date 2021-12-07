import pdfrw
from datetime import date
import sys
import os

def makePDF(myPDF, myDict, Name):
    for page in myPDF.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    #print(key)
                
                    if key in myDict.keys():
                        print("found {}".format(key))
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(myDict[key]))
                        )
    pdfrw.PdfWriter().write('{}.pdf'.format(Name), pdf)
    print("Created PDF!")
def formatInput(profile_dict):
    moddedPDF = pdf
    if(profile_dict['makeInvoice'] == 1):
        data_dictForInvoice = {
            'CUST PHONE Row1' : profile_dict['patientPhone'],
            'ORDER DATERow1' : profile_dict['patientOrderDate'],
            'DELIVERY DATERow1' : profile_dict['patientOrderDate'],
            'SHIP TORow1' : (profile_dict['patientFirstName'] + " " + profile_dict['patientLastName'] + " \n" + 
                        profile_dict['patientAddress'] + "\n" + 
                        profile_dict['patientCity'] + " " + profile_dict['patientState'] + " " + profile_dict['patientZip']),

            'INSURANCE INFORMATIONRow1' : ("ID: " + profile_dict['patientMBI'] + "\n"+ profile_dict['patientPreauthorization']),
            'SALESPERSONRow1' : profile_dict['patientLastName'],
            'MANUFRow1' : profile_dict['itemRow1CPT'],
            'ITEMLOTRow1' : profile_dict['itemRow1CPT'],
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
                        'MANUFRow2' : profile_dict['itemRow2CPT'],
            'ITEMLOTRow2' : profile_dict['itemRow2CPT'],
            'DESCRIPTIONRow2' : profile_dict['itemRow2Description'].upper(),
            'BILLING CODERow2' : profile_dict['itemRow2CPT'].upper(),
            'QTYRow2' : profile_dict['itemRow2Qty'],
            'UnitPriceRow2' : profile_dict['itemRow2Price'],

            'MANUFRow3' : profile_dict['itemRow3CPT'],
            'ITEMLOTRow3' : profile_dict['itemRow3CPT'],
            'DESCRIPTIONRow3' : profile_dict['itemRow3Description'].upper(),
            'BILLING CODERow3' : profile_dict['itemRow3CPT'].upper(),
            'QTYRow3' : profile_dict['itemRow3Qty'],
            'UnitPriceRow3' : profile_dict['itemRow3Price'],

            'MANUFRow4' : profile_dict['itemRow4CPT'],
            'ITEMLOTRow4' : profile_dict['itemRow4CPT'],
            'DESCRIPTIONRow4' : profile_dict['itemRow4Description'].upper(),
            'BILLING CODERow4' : profile_dict['itemRow4CPT'].upper(),
            'QTYRow4' : profile_dict['itemRow4Qty'],
            'UnitPriceRow4' : profile_dict['itemRow4Price'],

            'MANUFRow5' : profile_dict['itemRow5CPT'],
            'ITEMLOTRow5' : profile_dict['itemRow5CPT'],
            'DESCRIPTIONRow5' : profile_dict['itemRow5Description'].upper(),
            'BILLING CODERow5' : profile_dict['itemRow5CPT'].upper(),
            'QTYRow5' : profile_dict['itemRow5Qty'],
            'UnitPriceRow5' : profile_dict['itemRow5Price'],

            'MANUFRow6' : profile_dict['itemRow6CPT'],
            'ITEMLOTRow6' : profile_dict['itemRow6CPT'],
            'DESCRIPTIONRow6' : profile_dict['itemRow6Description'].upper(),
            'BILLING CODERow6' : profile_dict['itemRow6CPT'].upper(),
            'QTYRow6' : profile_dict['itemRow6Qty'],
            'UnitPriceRow6' : profile_dict['itemRow6Price'],
        }
        makePDF(moddedPDF, data_dictForInvoice, (profile_dict['patientFirstName'] + "_" + profile_dict['patientLastName'] + "_" + str(some_date)))
    elif(profile_dict['make_intake'] == 1):
        data_dictForIntake = {
            'Date' : some_date,
            'Phone' : '5625567619',
            'Phone_2' : some_date,
            'INSURANCE INFORMATIONRow1' : 'sample',
            'Name': 'Carls jr',
            'By' : 'Eli',
            'Address' : 'sample',
            'CityState Zip_3' : 'sample',
            'Clinical InformationRow1' : 'sample',
            'Name_2' : '1',#DOCTOR
            'Address_5' : '25',
            'CityState' : '25',
            'Date:' : '25',
            'Time' : '25',
            'Name Facility:' : '25',
            'Address_2:' : '25',
            'Clinical InformationRow1_2:' : '25',
            'I received instructions and understand that Medicare defines the' : 'stuff'
        }
        makePDF(moddedPDF, data_dictForIntake)
    else:
        print("No Intake Sheet Created")    


#directory = sys.executable
#baseDir = os.path.dirname(directory)
#pdf_path = (baseDir + "/" + "BlankInvoice(edit).pdf")

pdf_path = ("BlankInvoice(edit).pdf")

#pdf_path = "OrderIntakeSheet(edit).pdf"
#pdf_path = ""
pdf = pdfrw.PdfReader(pdf_path)
pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

some_date = date.today()






#print(pdf)
