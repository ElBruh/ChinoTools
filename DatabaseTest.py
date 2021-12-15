import sqlite3
import os
import sys

#directory = sys.executable
#baseDir = os.path.dirname(directory)
#medical = sqlite3.connect(baseDir + "/" + 'Medi-CalRatesDB1.db')
#medicare = sqlite3.connect(baseDir + "/" + 'MedicareRatesDB1.db')

medical = sqlite3.connect('./src/Medi-CalRatesDB1.db')
medicare = sqlite3.connect('./src/MedicareRatesDB1.db')


def searchMedcalCPT2(query, options):
    found={
        'ItemValue':'',
        'itemDescription':'',
        }
    if(options == 1):
        cur.execute("SELECT UnitValue, ProcedureDescription FROM data WHERE ProcCode LIKE ?", (query,))
    else:
        cur.execute("SELECT RentalRate, ProcedureDescription FROM data WHERE ProcCode LIKE ?", (query,))
    r = cur.fetchone()
    
    found["ItemValue"] = r[0]
    found["itemDescription"] = r[1]

    return found

def searchMedicareCPT2(query, options):
    found={
        'ItemValue':'',
        'itemDescription':'',
        }
    
    if(options == 1):
            #cur1.execute("SELECT 'CA (NR)', Description FROM data WHERE HCPCS LIKE ? AND (MOD LIKE 'NU' OR MOD LIKE '') AND WHERE JURIS LIKE 'D'", (item,))
        cur1.execute("SELECT [CA (NR)], Description From data WHERE HCPCS LIKE ? AND Mod = 'NU'", (query,))
            #cur.execute("SELECT ProcedureDescription FROM data WHERE ProcCode LIKE ?", (item,))
            
    else:
            #cur1.execute("SELECT 'CA (NR)', Description FROM data WHERE HCPCS LIKE ? AND (MOD LIKE 'RR' OR MOD LIKE '') AND WHERE JURIS LIKE 'D'", (item,))
        cur1.execute("SELECT [CA (NR)], Description From data WHERE HCPCS LIKE ? AND Mod = 'RR'", (query,))
            #cur.execute("SELECT ProcedureDescription FROM data WHERE ProcCode LIKE ?", (item,))

    s = cur1.fetchone()
    print(s)
    found["ItemValue"] = s[0]
    found["itemDescription"] = s[1]
    
    return found

def searchMedicalCPT(query, options):
    found = []
    for i, item in enumerate(query):
        
        if(options[i] == 1):
            cur.execute("SELECT UnitValue, ProcedureDescription FROM data WHERE ProcCode LIKE ?", (item,))
        else:
            cur.execute("SELECT RentalRate, ProcedureDescription FROM data WHERE ProcCode LIKE ?", (item,))
        
        r = cur.fetchone()
        if(r == None):
            found.append("")
            found.append("")
            continue
        found.append(r[0])
        found.append(r[1])
    return found

def searchMedicareCPT(query, options):
    found = []
    for i, item in enumerate(query):
        if(options[i] == 1):
            #cur1.execute("SELECT 'CA (NR)', Description FROM data WHERE HCPCS LIKE ? AND (MOD LIKE 'NU' OR MOD LIKE '') AND WHERE JURIS LIKE 'D'", (item,))
            cur1.execute("SELECT [CA (NR)], Description From data WHERE HCPCS LIKE ? AND Mod = 'NU'", (item,))
            #cur.execute("SELECT ProcedureDescription FROM data WHERE ProcCode LIKE ?", (item,))
            
        else:
            #cur1.execute("SELECT 'CA (NR)', Description FROM data WHERE HCPCS LIKE ? AND (MOD LIKE 'RR' OR MOD LIKE '') AND WHERE JURIS LIKE 'D'", (item,))
            cur1.execute("SELECT [CA (NR)], Description From data WHERE HCPCS LIKE ? AND Mod = 'RR'", (item,))
            #cur.execute("SELECT ProcedureDescription FROM data WHERE ProcCode LIKE ?", (item,))

        s = cur1.fetchone()
        if(s == None):
            found.append("")
            found.append("")
            continue
            
        print(s[0])   
        print(s[1]) 
        
        found.append(s[0])
        found.append(s[1])
    return found

cur = medical.cursor()
cur1 = medicare.cursor()

