def calcularCategoria(temperaturaAnual, profundidadEfectiva):
    categoria = 0
    respuestaTemperatura = 0
    respuestaProfundidad = 0
    if ((temperaturaAnual >= 25 and temperaturaAnual <= 28)) :
        respuestaTemperatura = 1
    elif ((temperaturaAnual >= 21 and temperaturaAnual <= 24) or (temperaturaAnual >= 29 and temperaturaAnual <= 30)) :
        respuestaTemperatura = 2
    elif ((temperaturaAnual >= 18 and temperaturaAnual <= 20) or (temperaturaAnual >= 31 and temperaturaAnual <= 32)) :
        respuestaTemperatura = 3
    elif ((temperaturaAnual < 18) or (temperaturaAnual >= 33 )) :
        respuestaTemperatura = 4

    if ((profundidadEfectiva >= 101)) :
        respuestaProfundidad = 1
    elif ((profundidadEfectiva >= 50 and profundidadEfectiva <= 100)) :
        respuestaProfundidad = 2
    elif ((profundidadEfectiva >= 25 and profundidadEfectiva <= 49)) :
        respuestaProfundidad = 3
    elif ((profundidadEfectiva < 25)) :
        respuestaProfundidad = 4

    if (respuestaTemperatura >= respuestaProfundidad) :
        categoria = respuestaTemperatura
    else :
        categoria = respuestaProfundidad

    return categoria

def leerLista(type):
    txt = ""
    if (type == 1):
        txt = "Temperatura media anual (°C): "
    else:
        txt = "Profundidad efectiva del suelo (cm): "
    listaTxt = input(txt)
    lista = listaTxt.split(" ")
    lenLista = len(lista)
    aux = 0
    for i in lista:
        aux += int(i)
    return aux/lenLista

def imprimirPromedio(lista):
    for i in lista:
        lista[lista.index(i)] = "{0:.2f}".format(i)
    txt = " ".join(lista)
    print(txt)

def imprimirClasificacion(cantCategoria1, cantCategoria2, cantCategoria3, cantCategoria4):
    print(f"Sumamente apto {cantCategoria1}")
    print(f"Moderadamente apto {cantCategoria2}")
    print(f"Marginalmente apto {cantCategoria3}")
    print(f"No apto {cantCategoria4}")


cantCategorias = int(input("Cantidad de categorias a evaluar "))
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
    temperaturaAnualProm = leerLista(1)
    profundidadEfectivaProm = leerLista(2)
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
