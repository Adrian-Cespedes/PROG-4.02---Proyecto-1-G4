def loadText(path):
    file = open(path,"r")
    matrix = []
    XSIZE = 0

    for rawRow in file:
        newRow = []
        for i in rawRow:
            if i != "\n":
                newRow.append(i)
            else:
                break
        matrix.append(newRow)

        if XSIZE < len(newRow):
            XSIZE = len(newRow)

    YSIZE = len(matrix)
        
    for m in range(len(matrix)):
        diff = XSIZE - len(matrix[m])
        for _ in range(diff):
            matrix[m].append(" ")

    file.close()
    return matrix