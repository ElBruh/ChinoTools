import sqlite3

medical = sqlite3.connect('Medi_CalRatesDB1.db')
medicare = sqlite3.connect('MedicareRatesDB.db')


def searchMedicalCPT(query):
    found = []
    for item in query:
        print(item)
        cur.execute("SELECT UnitValue, ProcedureDescription FROM data WHERE ProcCode LIKE ?", (item,))
        r = cur.fetchone()
        print(r[0])
        found.append(r[0])
        found.append(r[1])
    return found

def searchMedicareCPT(query):
    cur1.execute("SELECT CAR From data WHERE HCPCS LIKE ?", (query,))
    s = cur1.fetchone()
    print(s[0])

cur = medical.cursor()
cur1 = medicare.cursor()

