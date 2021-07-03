def leerLista():
    listaTxt = input()
    return listaTxt.split(" ")

def crearMatriz(n):
    matrizTemperatura = []
    for i in range(n) :
        aux = leerLista()
        matrizTemperatura.append(aux)
    return matrizTemperatura

def calcularCategoria(temperaturaAnualTxt, profundidadEfectivaTxt):
    categoria = 0
    respuestaTemperatura = 0
    respuestaProfundidad = 0
    temperaturaAnual = int(temperaturaAnualTxt)
    profundidadEfectiva = int(profundidadEfectivaTxt)
    if ((temperaturaAnual > 24 and temperaturaAnual <= 28)) :
        respuestaTemperatura = 1
    elif ((temperaturaAnual > 20 and temperaturaAnual <= 24) or (temperaturaAnual > 28 and temperaturaAnual <= 30)) :
        respuestaTemperatura = 2
    elif ((temperaturaAnual >= 18 and temperaturaAnual <= 20) or (temperaturaAnual > 30 and temperaturaAnual <= 32)) :
        respuestaTemperatura = 3
    elif ((temperaturaAnual < 18) or (temperaturaAnual > 32 )) :
        respuestaTemperatura = 4

    if ((profundidadEfectiva > 100)) :
        respuestaProfundidad = 1
    elif ((profundidadEfectiva > 50 and profundidadEfectiva <= 100)) :
        respuestaProfundidad = 2
    elif ((profundidadEfectiva >= 25 and profundidadEfectiva <= 50)) :
        respuestaProfundidad = 3
    elif ((profundidadEfectiva < 25)) :
        respuestaProfundidad = 4

    if (respuestaTemperatura >= respuestaProfundidad) :
        categoria = respuestaTemperatura
    else :
        categoria = respuestaProfundidad
    return categoria

def imprimirClasificacion(cantCategoria1, cantCategoria2, cantCategoria3, cantCategoria4):
    print(f"{cantCategoria4} {cantCategoria3} {cantCategoria2} {cantCategoria1}")

def masHabitual(mClasificar, n) :
    text = ""
    for i in range(n) :
        aux = mClasificar[i][0]
        code = 0
        for j in range(4) :
            if (aux < mClasificar[i][j] or  (aux == mClasificar[i][j] and i == j and i == 0)) :
                aux = mClasificar[i][j]
                code = j
            elif (aux == mClasificar[i][j]) :
                if (code > j) :
                    code = j 
        if (code == 0) :
            text += "sumamente apto,"
        elif (code == 1) :
            text += "moderadamente apto,"
        elif (code == 2) :
            text += "marginalmente apto,"
        elif (code == 3) :
            text += "no apto,"
    print(text[0:-1])

def menosHabitual(mClasificar, n) :
    text = ""
    for i in range(n) :
        aux = mClasificar[i][0]
        code = -1
        for j in range(4) :
            if ((aux > mClasificar[i][j] and mClasificar[i][j] != 0) or aux == 0 or  code == -1) :
                aux = mClasificar[i][j]
                code = j
            elif (aux == mClasificar[i][j]) :
                if (code > j) :
                    code = j
        if (code == 0) :
            text += "sumamente apto,"
        elif (code == 1) :
            text += "moderadamente apto,"
        elif (code == 2) :
            text += "marginalmente apto,"
        elif (code == 3) :
            text += "no apto,"
    print(text[0:-1])

def total (categoriaPorZona, n, m):
    aux = 0
    for i in range(n):
        aux += categoriaPorZona[i][m]
    print(aux)

def categorizar(matrizTemp, matrizTempProfundidad, n) :
    cantCategoria1 = 0
    cantCategoria2 = 0
    cantCategoria3 = 0
    cantCategoria4 = 0
    categoriaPorZona = []
    for i in range(n) :
        aux = [0]*4
        categoriaPorZona.append(aux)
    for i in range(n) :
        for j in range(len(matrizTemp[0])) :
            categoria = calcularCategoria(matrizTemp[i][j], matrizTempProfundidad[i][j])
            if (categoria == 1) :
                categoriaPorZona[i][0] += 1
                cantCategoria1 += 1
            elif (categoria == 2) :
                categoriaPorZona[i][1] += 1
                cantCategoria2 += 1
            elif (categoria == 3) :
                categoriaPorZona[i][2] += 1
                cantCategoria3 += 1
            elif (categoria == 4) :
                categoriaPorZona[i][3] += 1
                cantCategoria4 += 1
    imprimirClasificacion(cantCategoria1, cantCategoria2, cantCategoria3, cantCategoria4)
    masHabitual(categoriaPorZona, n)
    menosHabitual(categoriaPorZona, n)

cantCategorias = int(input(""))
matrizTemp = crearMatriz(cantCategorias)
matrizTempProfundidad = crearMatriz(cantCategorias)
categorizar(matrizTemp, matrizTempProfundidad, cantCategorias)