import pandas as pd
ruta=r"/home/shido/Documentos/Proyectos/Python_clases/alumnos.csv"
db=pd.read_csv(ruta)
print(db)
print(db.head(3))
print(db["notas"])