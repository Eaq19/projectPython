def calcularCategoria(temperaturaAnualTxt, profundidadEfectivaTxt):
    categoria = 0
    respuestaTemperatura = 0
    respuestaProfundidad = 0
    temperaturaAnual = (temperaturaAnualTxt)
    profundidadEfectiva = (profundidadEfectivaTxt)
    if ((temperaturaAnual > 24 and temperaturaAnual <= 28)) :
        respuestaTemperatura = 1
    elif ((temperaturaAnual >= 22 and temperaturaAnual < 25) or (temperaturaAnual > 28 and temperaturaAnual <= 30)) :
        respuestaTemperatura = 2
    elif ((temperaturaAnual >= 18 and temperaturaAnual <= 20) or (temperaturaAnual > 30 and temperaturaAnual <= 32)) :
        respuestaTemperatura = 3
    elif ((temperaturaAnual < 18) or (temperaturaAnual > 32 )) :
        respuestaTemperatura = 4

    if ((profundidadEfectiva > 100)) :
        respuestaProfundidad = 1
    elif ((profundidadEfectiva >= 50 and profundidadEfectiva <= 100)) :
        respuestaProfundidad = 2
    elif ((profundidadEfectiva >= 25 and profundidadEfectiva < 50)) :
        respuestaProfundidad = 3
    elif ((profundidadEfectiva < 25)) :
        respuestaProfundidad = 4

    if (respuestaTemperatura >= respuestaProfundidad) :
        categoria = respuestaTemperatura
    else :
        categoria = respuestaProfundidad
    return categoria

def leerLista():
    listaTxt = input()
    lista = listaTxt.split(" ")
    lenLista = len(lista)
    aux = 0
    for i in lista:
        aux += float(i)
    return (aux/lenLista)

def imprimirPromedio(lista):
    for i in lista:
        lista[lista.index(i)] = "{0:.2f}".format(i)
    txt = " ".join(lista)
    print(txt)

def imprimirClasificacion(cantCategoria1, cantCategoria2, cantCategoria3, cantCategoria4):
    print(f"sumamente apto {cantCategoria1}")
    print(f"moderadamente apto {cantCategoria2}")
    print(f"marginalmente apto {cantCategoria3}")
    print(f"no apto {cantCategoria4}")


cantCategorias = int(input(""))
auxCategorias = cantCategorias
cantCategoria1 = 0
cantCategoria2 = 0
cantCategoria3 = 0
cantCategoria4 = 0
auxTemperaturaAnual = 0
auxPrrofundidadEfectiva = 0
listaPromTemp = []
listaPromPro = []
while (auxCategorias > 0) :
    temperaturaAnualProm = leerLista()
    profundidadEfectivaProm = leerLista()
    listaPromTemp.append(temperaturaAnualProm)
    listaPromPro.append(profundidadEfectivaProm)
    categoria = calcularCategoria(temperaturaAnualProm, profundidadEfectivaProm)
    if (categoria == 1) :
        cantCategoria1 += 1
    elif (categoria == 2) :
        cantCategoria2 += 1
    elif (categoria == 3) :
        cantCategoria3 += 1
    elif (categoria == 4) :
        cantCategoria4 += 1
    auxCategorias -=1
imprimirPromedio(listaPromTemp)
imprimirPromedio(listaPromPro)
imprimirClasificacion(cantCategoria1, cantCategoria2, cantCategoria3, cantCategoria4)
