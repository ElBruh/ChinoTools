import os
import zipfile
import sqlite3
import pandas as pd
import requests
import openpyxl
import schedule
import time

url = 'https://files.medi-cal.ca.gov/Rates/rates_excel.zip'
file_name = 'rates_data.xlsx'
db_file = 'medi_cal_fee_schedule.sqlite'

def download_zip_file(url, file_name):
    response = requests.get(url)
    response.raise_for_status()

    with open(file_name, 'wb') as file:
        file.write(response.content)


def extract_excel_from_zip(zip_file, excel_file_name):
    with zipfile.ZipFile(zip_file, 'r') as zf:
        for name in zf.namelist():
            if name == excel_file_name:
                zf.extract(name)
                return name
    return None


def excel_to_sqlite(excel_file, db_file):
    df = pd.read_excel(excel_file, engine='openpyxl', header=1)
    
    with sqlite3.connect(db_file) as conn:
        df.to_sql('medi_cal_fee_schedule', conn, if_exists='replace', index=False)

        
def update_fee_schedule():
    # Download and extract the Excel file from the zip file
    zip_file_name = os.path.basename(url)
    download_zip_file(url, zip_file_name)
    excel_file = extract_excel_from_zip(zip_file_name, file_name)
    
    if excel_file:
        # Convert the Excel file to an SQLite database
        excel_to_sqlite(excel_file, db_file)
        
        print("Medi-Cal Fee Schedule updated successfully")

        # Remove downloaded files
        os.remove(zip_file_name)
        os.remove(excel_file)
    else:
        print("Excel file not found in the downloaded zip file")


# Run the script immediately
update_fee_schedule()
# Schedule the script to run daily
schedule.every().day.at("00:00").do(update_fee_schedule)

# Keep the script running and execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)