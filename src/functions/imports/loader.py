#
#
#

"""
Toma un archivo .txt y lo convierte a una matriz 2D    

(path): Direccion al ASCII / archivo .txt escogido
return: Retorna la matriz 2D conteniendo el ASCII
"""

def loadText(path):
    file = open(path, "r", encoding='utf8')
    content = file.read()
    file.close()
    #======================================
    matrix = []
    XSIZE = 0
    newRow = []
    for char in content:
        if char != "\n":
            newRow.append(char)
        else:
            matrix.append(newRow)
            newRow = []

        if XSIZE < len(newRow):
            XSIZE = len(newRow)
        
    for m in range(len(matrix)):
        diff = XSIZE - len(matrix[m])
        for _ in range(diff):
            matrix[m].append(" ")

    return matrix