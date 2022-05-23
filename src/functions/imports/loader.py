def loadText(file):
    matrix = []
    XSIZE = 0
    CRLF = '\r\n'
    CR = '\r'

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

    #file.close
    return matrix