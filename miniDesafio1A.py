import pandas as pd

archivo = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Tabla1.xlsx")
print(archivo)
print()

data = archivo.to_dict("records")

for x in range (len(data)):
    print(data[x]["Equipo"], "tiene", data[x]["Goles a favor"] - data[x]["Goles en contra"], "goles a favor")
