import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)


if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    titre = soup.find('h1')
    print(f'Titre: {titre.text}')
    # product_information_labels = soup.findAll('th')
    # product_information_values = soup.findAll('td')
    # for i in range(len(product_information_labels)):
    #     print(product_information_labels[i].text + ', ' + product_information_values[i].text)
    # print(product_information_values)