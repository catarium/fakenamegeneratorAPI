import requests
from bs4 import BeautifulSoup
import re


URL = 'https://www.fakenamegenerator.com/'


class Parser:
    def __init__(self):
        self.url = 'https://www.fakenamegenerator.com/'
        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) ', 'accept': '*/*'}

    def create_data(self, gender, name_lang, country):
        html = requests.get(f'{self.url}gen-{gender}-{name_lang}-{country}.php',
                            headers=self.headers).text
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find('div', id='details').find('div', class_='content')
        address = data.find('div', class_='address')
        det = data.find_all('dd')
        det2 = data.find_all('dt')
        det = [f'{det[i].text}' for i in range(len(det))][:-1]
        det2 = [f'{det2[i].text}' for i in range(len(det2))][:-1]
        det.insert(0, address.h3.text)
        det.insert(1, address.div.text.strip())
        det_len = len(det)
        print(len(det))
        if "Mother's maiden name" not in det2:
            det2.insert(0, 'None')
            det.insert(2, 'None')
        if det2[1] != 'Geo coordinates':
            if 'You' in det[3]:
                det[3] = re.match(r'.+You', det[3]).group(0)[:-3]
        else:
            det.insert(3, 'None')
        if '@' in det[10]:
            det[10] = re.search(r'\w+@\w+.\w+', det[10]).group(0)
        else:
            det.insert(10, 'None')
        det[20], det[21] = re.search(r'\(.+\)', det[20]).group(0)[1:-1], \
                           re.search(r'\(.+\)', det[21]).group(0)[1:-1]
        return det
