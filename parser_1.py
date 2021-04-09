import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


with open('houses.csv', 'a', encoding='utf8') as f:
    writer = csv.DictWriter(f, fieldnames=["link", "address", "year", "floors"])
    writer.writeheader()


def write_csv(data):
    with open('houses.csv', 'a', encoding='utf8') as f:
        writer = csv.DictWriter(f, fieldnames=["link", "address", "year", "floors"])
        writer.writerow({'link': data['link'], 'address': data['address'],
                         'year': data['year'], 'floors': data['floors']})
        print(data)
        print('--------------------------------')
        print()


for p in range(1, 37):
    r = requests.get('https://dom.mingkh.ru/ryazanskaya-oblast/ryazan/houses?page={}'.format(p))
    s = BeautifulSoup(r.text, 'lxml')

    table = pd.read_html(r.text)[0]
    houses = ['https://dom.mingkh.ru' + i.get('href') for i in s.find('table').find_all('a')]

    for i in range(len(table)):
        if table['Год'][i] != '—' and table['Этажей'][i] != '—':
            data = {'link': houses[i], 'address': table['Адрес'][i],
                    'year': table['Год'][i], 'floors': table['Этажей'][i]}
            write_csv(data)
