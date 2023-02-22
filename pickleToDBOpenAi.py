import sqlite3
import os
import sys
import pickle

def find_pickle_files(base_dir):
    """Recursively find all pickle files in the given directory and its subdirectories."""
    pickle_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.pickle'):
                pickle_files.append(os.path.join(root, file))
    print(f"Number of pickle files found: {len(pickle_files)}")            
    return pickle_files

# Connect to the patientProfiles.db database
directory = sys.executable
baseDir = os.path.dirname(directory)
try:
    patientProfile = sqlite3.connect(baseDir + "/src/" + "patientProfiles.db")
except:
    patientProfile = sqlite3.connect("./src/patientProfiles.db")

cur3 = patientProfile.cursor()

# Find all pickle files in the "./dist/gui/Output/" directory and its subdirectories
pickle_files = find_pickle_files("./dist/gui/Output/")

# Load the data from each pickle file and insert it into the database
values = []
for file in pickle_files:
    # Load the data from the pickle file
    with open(file, 'rb') as handle:
        b = pickle.load(handle)

    # Check if the patient already exists in the database
    cur3.execute("SELECT COUNT(*) FROM data WHERE patientFirstName=? AND patientLastName=?", (b['patientFirstName'], b['patientLastName']))
    result = cur3.fetchone()[0]

    # If the patient does not already exist, insert the data into the database
    if result == 0:
        # Generate the INSERT statement
        placeholder = ", ".join(["?"] * len(b))
        stmt = "INSERT INTO `{table}` ({columns}) VALUES ({values});".format(table="data", columns=",".join(b.keys()), values=placeholder)

        # Execute the INSERT statement with the values from the pickle file
        cur3.execute(stmt, list(b.values()))
        patientProfile.commit()

# Close the database connection
patientProfile.close()
