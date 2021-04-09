import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


with open('nedvizh.csv', 'a', encoding='utf8') as f:
    writer = csv.DictWriter(f, fieldnames=["price", "year", "floors", "rooms", "m2", "url"])
    writer.writeheader()


def write_csv(data):
    with open('nedvizh.csv', 'a', encoding='utf8') as f:
        writer = csv.DictWriter(f, fieldnames=["price", "year", "floors", "rooms", "m2", "url"])
        writer.writerow({'price': data['price'], 'year': data['year'], 'floors': data['floors'],
                         'rooms': data['rooms'], 'm2': data['m2'], 'url': data['url']})
        print(data)
        print('--------------------------------')
        print()


for z in range(1, 42):
    r = requests.get('https://www.domofond.ru/arenda-kvartiry-ryazan-c2718?RentalRate=Month&Page={}'.format(z))
    s = BeautifulSoup(r.text, 'lxml')

    all_links = ['https://www.domofond.ru' + i.get('href') for i in s.find(
        'div', class_='search-results__main___38xtS').find(
        'div', class_='search-results__itemCardList___RdWje').find_all(
        'a', class_='long-item-card__item___ubItG'
    )]
    r2 = requests.get('https://www.domofond.ru/1-komnatnaya-kvartira-v-arendu-ryazan-3234992066')
    s2 = BeautifulSoup(r2.text, 'lxml')

    for l in all_links:
        r2 = requests.get(l)
        s2 = BeautifulSoup(r2.text, 'lxml')
        price = ''.join(s2.find('div', class_='information__price___2Lpc0').text.strip().split()[:2])
        year = [i.find_next('span').text for i in s2.find_all('span', class_='project-info__bold___1u6R5') if i.text == 'Год постройки:']

        if len(year) == 0:
            year = [i.find_next('span').text for i in s2.find_all('span', class_='project-info__bold___1u6R5') if i.text == 'Год ввода в эксплуатацию:']
        if len(year) == 0:
            year = ''
        else:
            year = year[0]

        try:
            floors = [i.find_next('span').text for i in s2.find_all('span', class_='detail-information__bold___3IcDP') if i.text == 'Этаж:'][0].split('/')[-1]
        except IndexError:
            floors = ''

        try:
            rooms = [i.find_next('span').text for i in s2.find_all('span', class_='detail-information__bold___3IcDP') if i.text == 'Комнаты:'][0]
        except IndexError:
            rooms = ''

        try:
            m2 = [i.find_next('span').text for i in s2.find_all('span', class_='detail-information__bold___3IcDP') if i.text == 'Цена за м²:'][0].split()[0]
        except IndexError:
            m2 = ''
        if floors == '':
            floors = s2.find('h1').text.split(',')[-1].split()[0].split('/')[-1]
        data = {'price': price, 'year': year, 'floors': floors,
                'rooms': rooms, 'm2': m2, 'url': l}

        write_csv(data)
