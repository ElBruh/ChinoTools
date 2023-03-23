import sqlite3
import os
import sys

directory = sys.executable
baseDir = os.path.dirname(directory)


try:
    medical = sqlite3.connect(baseDir + "/src/" + 'medi_cal_fee_schedule.sqlite')
except:
    medical = sqlite3.connect('./src/medi_cal_fee_schedule.sqlite')
try:
    medicare = sqlite3.connect(baseDir + "/src/" + 'medicare_fee_schedule.sqlite')
except:
    medicare = sqlite3.connect('./src/medicare_fee_schedule.sqlite')
try:
    patientProfile = sqlite3.connect(baseDir + "/src/" + "patientProfiles.db")
except:
    patientProfile = sqlite3.connect("./src/patientProfiles.db")


def openPatientDB():
    cur3.execute("")


def searchMedcalCPT2(query, options):
    found = {
        'ItemValue': '',
        'itemDescription': '',
    }

    # Using a parameterized query with a tuple for better readability
    if options == 1:
        sql_query = "SELECT \"Unit Value\", \"Procedure Description\" FROM medi_cal_fee_schedule WHERE \"Proc Code\" LIKE ?"
    else:
        sql_query = "SELECT \"Rental Rate\", \"Procedure Description\" FROM medi_cal_fee_schedule WHERE \"Proc Code\" LIKE ?"

    try:
        # Use 'with' to ensure the connection is properly closed
        
        #cur = conn.cursor()
        cur.execute(sql_query, (query,))
        r = cur.fetchone()

        # Check if a result is found before assigning values
        if r:
            found["ItemValue"] = r[0]
            found["itemDescription"] = r[1]
        else:
            print(f"No results found for query: {query}")

    except sqlite3.Error as e:
        print(f"An error occurred while executing the SQL query: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return found

def searchMedicareCPT2(query, options):
    found = {
        'ItemValue': '',
        'itemDescription': '',
    }

    try:
        # Determine the modifier based on the options
        mod = 'RR' if options != 1 else 'NU'
        print(f"In {mod}")

        # Execute the query with the specified modifier
        cur1.execute("SELECT [CA (NR)], Description FROM dme_fee_schedule WHERE HCPCS LIKE ? AND Mod IS ?", (query, mod))
        s = cur1.fetchone()

        # If no results, execute the query without the modifier
        if s == None:
            cur1.execute("SELECT [CA (NR)], Description FROM dme_fee_schedule WHERE HCPCS LIKE ?", (query,))
            s = cur1.fetchone()

        found["ItemValue"] = s[0]
        found["itemDescription"] = s[1]
        print(s)
        return found

    except Exception as e:
        print(f"An error occurred while executing searchMedicareCPT2: {e}")
        print(f"Query: {query}")
        print(f"Options: {options}")
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
cur3 = patientProfile.cursor()
