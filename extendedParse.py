import requests
from bs4 import BeautifulSoup as bs
import csv


def getUrl(region, city, street, house):
    return f'https://egrp365.ru/list4.php?street={street}&house={house}&mregion={region}&city={city}'

def gethtml(url):
    r = requests.get(url)
    return r

def write_csv(data):
    with open('data.csv', 'a') as f:
        order = ['Кадастровый номер','Адрес','Кадастровая карта','Этаж','Площадь']
        writer = csv.DictWriter(f, fieldnames = order)
        writer.writerows(data)

def getData(response):
    html = response.json()['data']
    soup = bs(html, 'lxml')

    kad_numbers = soup.find_all('div', class_='rs_kad_number')
    kad_numbers = [i.text for i in kad_numbers]
    # получаем list с кадастр.номерами

    adress = soup.find_all('div', class_='rs_address')
    for i in adress:
        print(i.text)
    #adress = [i.text for i in adress]
    # получаем list с адресами

    #print(adress)

def main():
    url = getUrl('Татарстан','Казань','Качалова',75)
    data = gethtml(url)
    res = getData(data)
    print(res)

if __name__ == '__main__':
    main()

'''
https://egrp365.ru/map/?kadnum=kad_number - кадастр.карта
https://egrp365.ru/reestr/?egrp=kad_number - ссылка на страницу объекта

'''
