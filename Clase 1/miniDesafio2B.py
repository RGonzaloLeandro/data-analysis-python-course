#Escribir una funcion que reciba como parámetros: una variable de tipo DataFrame (la tabla de alumnos) y el índice de un alumno. Luego debe devolver con return el promedio de sus notas en las diferentes materias.

import pandas as pd

def promedios (tabla,indice):
    notas = tabla.to_dict("records")

    promedio = round((notas[indice]["Quimica"] + notas[indice]["Matematica"] + notas[indice]["Fisica"]) / 3, 2)
    print(promedio)

tab = pd.read_excel("Datos.xlsx")
print(tab)
ind = int(input("Índice de alumno?"))
promedios(tab,ind)
