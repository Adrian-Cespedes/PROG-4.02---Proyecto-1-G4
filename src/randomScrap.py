from random import randint
from bs4 import BeautifulSoup
import requests

def randomScrap():
    url = "http://www.asciiworld.com/index.html"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    lista = soup.find_all("div", attrs = {"class": "bloc menu"})
    for categoria in lista:
        if categoria.h2.text == "Categories":
            categorias = categoria.find_all("a", attrs = {"class": "mot"}, href=True)
            n = 0
            for i in range(0, len(categorias)):
                if i % 4 == 0:
                    print()
                print("%-30s" % f"[{n}] {categorias[i].text[2:]}", end="")
                n += 1

    opcion = int(input("\n\nEscoge una categoria: "))
    urlBase = "http://www.asciiworld.com/"
    urlCategoria = urlBase + categorias[opcion]["href"]

    html_content = requests.get(urlCategoria).text
    soup = BeautifulSoup(html_content, "lxml")

    print("ASCII Art:")
    lista = soup.find_all("pre", text=True)
    listaFinal = []
    for result in lista:
        ascii = result.find(text=True)
        listaFinal.append(ascii)
    n = randint(0, len(lista)-1)
    return listaFinal[n]