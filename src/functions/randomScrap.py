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
        ascii = result.get_text()
        listaFinal.append(ascii)
    n = randint(0, len(lista)-1)
    ascii = listaFinal[n]
    lines = ascii.split("\n")

    # <pre> html ASCII to python matrix
    matrix = []
    for line in lines:
        matrixRow = []
        for char in line:
            matrixRow.append(char)
        matrix.append(matrixRow)

    # Getting the max row length number to make the matrix like a rectangle
    lengthList = []
    for row in matrix:
        lengthList.append(len(row))
    index = lengthList.index(max(lengthList))
    maxRowLength = len(matrix[index])

    # Filling the matrix rows
    for m in range(len(matrix)):
        diff = maxRowLength - len(matrix[m])
        for _ in range(diff):
            matrix[m].append(" ")

    return matrix