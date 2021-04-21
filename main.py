import requests
from bs4 import BeautifulSoup

# fonction qui extrait de le nombre dans l'information affichant le nombre d'exemplaires disponibles
def extraire_nombre(expression_brute):
    i = -12
    nombre_a_extraire = ''
    while expression_brute[i] != '(' and expression_brute[i] != ' ':
        nombre_a_extraire = nb_dispo + expression_brute[i]
        i -= 1
    return int("".join(reversed(nombre_a_extraire)))

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(url)


if response.ok:
    soup = BeautifulSoup(response.content, 'lxml')
    titre = soup.find('h1')
    product_information_labels = soup.findAll('th')
    product_information_values = soup.findAll('td')
    # for i in range(len(product_information_labels)):
    #     print(product_information_labels[i].text + ', ' + product_information_values[i].text)

# création du dictionnaire
informations_demandees = {}
informations_demandees["titre"] = titre.text
informations_demandees["UPC"] = product_information_values[0].text
informations_demandees["prix hors taxes"] = product_information_values[2].text
informations_demandees["prix taxes incluses"] = product_information_values[3].text
informations_demandees["nombres disponibles"] = extraire_nombre(product_information_values[5].text)

print(informations_demandees)


