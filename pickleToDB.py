import sqlite3
import os
import sys
import pickle

directory = sys.executable
baseDir = os.path.dirname(directory)
try:
    patientProfile = sqlite3.connect(baseDir + "/src/" + "patientProfiles.db")
except:
    patientProfile = sqlite3.connect("./src/patientProfiles.db")

cur3 = patientProfile.cursor()


x = os.listdir("./dist/gui/Output/All Pickle Files/")

for file in x:
    with open("./dist/gui/Output/All Pickle Files/{}".format(file), 'rb') as handle:
        b = pickle.load(handle)
        print(b["patientFirstName"])
        #print(b.values())
        placeholder = ", ".join(["?"] * len(b))
        #print(placeholder)
        stmt = "INSERT INTO `{table}` ({columns}) VALUES ({values});".format(table="data", columns=",".join(b.keys()), values=placeholder)
        cur3.execute(stmt, list(b.values()))
        patientProfile.commit()
        