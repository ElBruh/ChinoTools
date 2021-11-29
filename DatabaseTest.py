import sqlite3

medical = sqlite3.connect('Medi_CalRatesDB1.db')
medicare = sqlite3.connect('MedicareRatesDB.db')


def searchMedicalCPT(query, options):
    found = []
    for i, item in enumerate(query):
        
        if(options[i] == 1):
            cur.execute("SELECT UnitValue, ProcedureDescription FROM data WHERE ProcCode LIKE ?", (item,))
        else:
            cur.execute("SELECT RentalRate, ProcedureDescription FROM data WHERE ProcCode LIKE ?", (item,))
        
        r = cur.fetchone()

        found.append(r[0])
        found.append(r[1])
    return found

def searchMedicareCPT(query, options):
    found = []
    for i, item in enumerate(query):
        if(options[i] == 1):
            cur1.execute("SELECT CAR From data WHERE HCPCS LIKE ? AND (MOD LIKE 'NU' OR MOD LIke '')", (item,))
            #cur1.execute("SELECT CAR From data WHERE HCPCS LIKE ?", (item,))
            cur.execute("SELECT ProcedureDescription FROM data WHERE ProcCode LIKE ?", (item,))
            
            s = cur1.fetchone()
            r = cur.fetchone()
        else:
            cur1.execute("SELECT CAR From data WHERE HCPCS LIKE ? AND (MOD LIKE 'RR' OR MOD LIKE '')", (item,))
            #cur1.execute("SELECT CAR From data WHERE HCPCS LIKE ?", (item,))
            cur.execute("SELECT ProcedureDescription FROM data WHERE ProcCode LIKE ?", (item,))
            
            s = cur1.fetchone()
            r = cur.fetchone()
        print(s)    
        if(s == None):
            found.append("")
            found.append("")
            continue
        
        found.append(s)
        found.append(r[0])
    return found

cur = medical.cursor()
cur1 = medicare.cursor()

