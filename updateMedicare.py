import os
import re
import zipfile
import sqlite3
import pandas as pd
import requests
from bs4 import BeautifulSoup
import schedule
import time

base_url = 'https://www.cms.gov'
download_page_url = base_url + '/medicaremedicare-fee-service-paymentdmeposfeescheddmepos-fee-schedule/dme23'
csv_file_prefix = 'DMEPOS_'
db_file = 'medicare_fee_schedule.sqlite'

def download_zip_file(url, file_name):
    response = requests.get(url)
    response.raise_for_status()

    with open(file_name, 'wb') as file:
        file.write(response.content)


def extract_csv_from_zip(zip_file, csv_prefix):
    with zipfile.ZipFile(zip_file, 'r') as zf:
        for name in zf.namelist():
            if name.startswith(csv_prefix):
                zf.extract(name)
                return name
    return None


def csv_to_sqlite(csv_file, db_file):
    
    df = pd.read_csv(csv_file, header=6)  # Read the CSV file without a header    
    
    with sqlite3.connect(db_file) as conn:
        df.to_sql('dme_fee_schedule', conn, if_exists='replace', index=False)
        
def update_fee_schedule():
    # Scrape download page to get the link to the zip file
    page_response = requests.get(download_page_url)
    soup = BeautifulSoup(page_response.content, 'html.parser')
    zip_file_link = soup.find('a', href=re.compile(r'.*\.zip$'))['href']
    zip_file_url = base_url + zip_file_link
    zip_file_name = os.path.basename(zip_file_url)

    # Download and extract the CSV file from the zip file
    download_zip_file(zip_file_url, zip_file_name)
    csv_file = extract_csv_from_zip(zip_file_name, csv_file_prefix)
    if csv_file:
        # Convert the CSV file to an SQLite database
        csv_to_sqlite(csv_file, db_file)
        
        print("Medicare Fee Schedule updated successfully")

        # Remove downloaded files
        os.remove(zip_file_name)
        os.remove(csv_file)
    else:
        print("CSV file not found in the downloaded zip file")


# Run the script immediately
update_fee_schedule()

# Schedule the script to run daily
schedule.every().day.at("00:00").do(update_fee_schedule)

# Keep the script running and execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)
