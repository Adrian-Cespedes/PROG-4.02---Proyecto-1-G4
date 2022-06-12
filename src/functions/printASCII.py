#
#
#

"""
Imprime el ASCII contenido en la matriz para una mejor visualizacion

(mat): El ASCII en matriz a ser impreso
"""

def printASCII(mat):
    row = len(mat)
    col   = len(mat[0])
    for f in range(row):
        for c in range(col):
            print((mat[f][c]), end="")
        print()   