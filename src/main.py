import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import schedule
import time

url = 'https://wellness.incloud.it/AccessMonitor/ZoneAvailabilityMonitor?zone=BmNRDKuGcv%2BPH%2B%2BPuK8Q0HFrrSF6n%2FAciPZmwYzs31g%3D%7C1769%7C1'


def fetch_free_slots():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Selezione del numero dei posti disponibili
    free_slots = soup.find('span', class_='zone_availableattendance').text

    return free_slots


def record_data():
    free_slots = fetch_free_slots()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = [timestamp, free_slots]

    with open('free_slots_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

    print(f'Recorded data at {timestamp}: {free_slots} free slots')


# Schedula lo script per eseguire ogni 10 minuti
schedule.every(5).minutes.do(record_data)

# Esegui il loop infinito
while True:
    schedule.run_pending()
    time.sleep(1)
