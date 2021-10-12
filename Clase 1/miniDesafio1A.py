#Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato. El archivo tiene cuatro columnas, Equipo, Puntos, Goles a favor y Goles en contra. Determinar de cada equipo la diferencia de gol (goles a favor - goles en contra), y mostrar todas las diferencias de gol usando print.

import pandas as pd

archivo = pd.read_excel("Tabla1.xlsx")
print(archivo)
print()

data = archivo.to_dict("records")

for x in range (len(data)):
    print(data[x]["Equipo"], "tiene", data[x]["Goles a favor"] - data[x]["Goles en contra"], "goles a favor")
