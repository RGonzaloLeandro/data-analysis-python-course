#Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato y determinar qué equipo es el campeón (1ro) y perdedor (último). El archivo tiene cuatro columnas, Equipo, Puntos, Goles a favor y Goles en contra.

import pandas as pd

tabla = pd.read_excel("Tabla1.xlsx")
print(tabla)

data = tabla.to_dict("records")

winnerPoints = 0
for x in range (len(data)):
    if data[x]["Puntos"] > winnerPoints:
      winnerPoints = data[x]["Puntos"]
      winner = data[x]["Equipo"]

print("El campeón es", winner)    

loserPoints = 1000000
for x in range (len(data)):
    if data[x]["Puntos"] < loserPoints:
      loserPoints = data[x]["Puntos"]
      loser = data[x]["Equipo"]

print("El último en la tabla es", loser) 