import requests
from bs4 import BeautifulSoup

# fonction qui isole et extrait le nombre dans l'information affichant le nombre d'exemplaires disponibles
def extraire_nombre(expression_brute):
    i = -12
    nombre_a_extraire = ''
    while expression_brute[i] != '(' and expression_brute[i] != ' ':
        nombre_a_extraire += expression_brute[i]
        i -= 1
    return int("".join(reversed(nombre_a_extraire)))



url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
# url = 'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html'

response = requests.get(url)


if response.ok:
    soup = BeautifulSoup(response.content, 'lxml')
    titre = soup.find('h1')
    product_information_description = soup.select('div + p')
    product_information_rating = soup.select('p.star-rating')
    product_information_values = soup.find_all('td')
    link = soup.find_all('a')




# #fonction qui calcule la note d'un livre
# i = 0
# notes = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
#
# while soup.find('p', attrs={"class": notes[i]}) != None:
#     i += 1
# print(soup.find('p', attrs={"class": notes[i-1]}))




# création du dictionnaire des données scrapées

informations_demandees = {}
informations_demandees["titre"] = titre.text
informations_demandees["description"] = product_information_description[0].text
informations_demandees["categorie"] = link[-1].text
informations_demandees["UPC"] = product_information_values[0].text
informations_demandees["prix hors taxes"] = product_information_values[2].text
informations_demandees["prix taxes incluses"] = product_information_values[3].text
informations_demandees["nombres disponibles"] = extraire_nombre(product_information_values[5].text)

for key in informations_demandees:
    print(key + ', ' + str(informations_demandees[key]))


