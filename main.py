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


# fonction qui convertie en nombre la note en lettre

def convertir_en_nombre(nombre_en_lettre):
    notes = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
    i = 0
    while notes[i] != nombre_en_lettre:
        i += 1
    return i


# fonction qui convertit un chemin en url
def convertir_chemin_en_url(chemin):
    return 'http://books.toscrape.com/catalogue/' + chemin['href'][9:]


# fonction qui va chercher les informations d'une page correspondant à un livre
def livre_informations(book_url):
    response = requests.get(book_url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'lxml')
        titre = soup.find('h1')
        product_information_description = soup.select('div + p')
        link = soup.find_all('a')
        product_information_values = soup.find_all('td')
        star_rating = soup.find('p', class_='star-rating')['class'][1]

    # création du dictionnaire des données scrapées

    informations_demandees = {}
    informations_demandees["url"] = book_url
    informations_demandees["titre"] = titre.text
    informations_demandees["description"] = product_information_description[0].text
    informations_demandees["categorie"] = link[-1].text
    informations_demandees["UPC"] = product_information_values[0].text
    informations_demandees["prix hors taxes"] = product_information_values[2].text
    informations_demandees["prix taxes incluses"] = product_information_values[3].text
    informations_demandees["nombres disponibles"] = extraire_nombre(product_information_values[5].text)
    informations_demandees["note"] = convertir_en_nombre(star_rating)

    for key in informations_demandees:
        print(key + ', ' + str(informations_demandees[key]))


url = 'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html'

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.content, 'lxml')
    chemins_vers_livre = soup.select('a[title]')
    for chemin_vers_livre in chemins_vers_livre:
        livre_url = convertir_chemin_en_url(chemin_vers_livre)
        livre_informations(livre_url)



    # next=''
    # while next != None:
    #     next = soup.find('li', class_="next")
    #     page = next.select('a')
    #     # print(str(page[0])[9:20])
    #     url = url[:68]+str(page[0])[9:20]
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.content)


