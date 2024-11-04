import time
import random
import requests
from bs4 import BeautifulSoup

#added header to mimic a website, in case the site block the script
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def raminkonditoria():
    url = "https://www.raminkonditoria.fi/rami-sammonkatu-lounas"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    ramin_lunch_seciton = soup.find('div', class_='item-121')
    if ramin_lunch_seciton:
        print("Ramin's lunch section")
        print(ramin_lunch_seciton.get_text())
    else:
        print("Ramin's lunch menu not found")

    #add some delay
    time.sleep(random.uniform(1, 5))

def ravintolaaugust():
    url = "https://www.ravintolaaugust.fi"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    august_lunch_section = soup.find('div', class_='item-38')
    if august_lunch_section:
        print("August's lunch menu")
        print(august_lunch_section.get_text())
    else:
        print("August's menu not found")

    #add some delay
    time.sleep(random.uniform(1, 5))

raminkonditoria()
ravintolaaugust()