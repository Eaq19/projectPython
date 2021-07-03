temperaturaAnual = int(input("Temperatura media anual (°C): "))
profundidadEfectiva = int(input("Profundidad efectiva del suelo (cm): "))
respuestaTemperatura = 0
respuestaProfundidad = 0
categoria = 0
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

if (categoria == 1) :
    print("Sumamente apto")
elif (categoria == 2) :
    print("Moderadamente apto")
elif (categoria == 3) :
    print("Marginalmente apto")
elif (categoria == 4) :
    print("No apto")
