import csv
import functools

def calculateAverage(field, list): 
    return (functools.reduce(lambda x, y: int(x) + int(y[field]), list, 0)) / len(list)

def calculateField(value, listFilter): 
    return int(len(list(filter(lambda x : x['aptitud'] == value, listFilter))))

def funcTemp(p):
   return int(p['temperatura_media_anual'])

def funcProf(p):
    return int(p['profundidad_efectiva_suelo'])

def orden(mClasificar, n) :
    matriz = []
    for i in range(n) :
        aux = [0 , 0]
        for j in range(4) :
            if (i == j and i == 0) or (aux[1] < mClasificar[j][1]) :
                aux = mClasificar[j]
                if((i != j or i != 0)) :
                    mClasificar[j] = [0 , 0]
            elif (aux[1] == mClasificar[j][1]) :
                if (aux[0] > mClasificar[j][0]) :
                    aux = mClasificar[j]
                    mClasificar[j] = [0 , 0]
        matriz.append(aux)
    for i in range(n) :
        text = ""
        if (matriz[i][0] == 4) :
            text += "sumamente apto"
        elif (matriz[i][0] == 2) :
            text += "moderadamente apto"
        elif (matriz[i][0] == 1) :
            text += "marginalmente apto"
        elif (matriz[i][0] == 3) :
            text += "no apto"
        print(text + " " + str(matriz[i][1]))

def readFile(name, city) :
    with open(name, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        listCity = list(filter(lambda x : x['capital'] == city, reader))
        tempAverage = "{0:.2f}".format(calculateAverage('temperatura_media_anual', listCity))
        profAverage = "{0:.2f}".format(calculateAverage('profundidad_efectiva_suelo', listCity))
        print(f"{tempAverage} {profAverage}")
        print(f"{min(listCity, key=funcTemp)['temperatura_media_anual']} {min(listCity, key=funcProf)['profundidad_efectiva_suelo']}")
        print(f"{max(listCity, key=funcTemp)['temperatura_media_anual']} {max(listCity, key=funcProf)['profundidad_efectiva_suelo']}")
        margApto = calculateField("marginalmente apto", listCity)
        nogApto = calculateField("no apto", listCity)
        modApto = calculateField("moderadamente apto", listCity)
        sumApto = calculateField("sumamente apto", listCity)
        matriz = [[1, margApto], [3, nogApto], [2, modApto], [4, sumApto]]
        orden(matriz, 4)
        #for row in listCity:
        #    print(row)

readFile("data.csv", input(""))