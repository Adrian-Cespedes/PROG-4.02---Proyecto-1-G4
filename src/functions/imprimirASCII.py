def imprimirASCII(mat):
    filas = len(mat)
    col   = len(mat[0])
    for f in range(filas):
        for c in range(col):
            print((mat[f][c]), end="")
        print()   