#Calcular el promedio de las notas de química de todos los alumnos en el archivo Datos.xlsx.

import pandas as pd

datos = pd.read_excel("datos.xlsx")
print (datos)

chemical = datos.to_dict("list")
#print(chemical)

promedio = round((sum(chemical["Quimica"]) / len(chemical["Quimica"])), 2)

print(promedio)