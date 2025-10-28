import pandas as pd
#Voy a usar la biblioteca pandas para ordenar en celdas los valores de este diccionario
#Usamos la propiedad DataFrame
dato={
    'Nombre':['Lucas','Carlos','Gerardo'],
    'Edad':[31,87,98],
    'Ocupacion':['Estudiante','Cantor','Conductor']
}

tabla = pd.DataFrame(dato)
print(tabla)

#Mostrar una sola columna

print(tabla['Ocupacion'])