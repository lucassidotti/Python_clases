import os
import shutil

carpeta_actual=os.getcwd()
print(f"Trabajando en: {carpeta_actual}")

os.makedirs('Textos',exist_ok=True)

#Mover los archivos

for archivo in os.listdir():
    if archivo.endswith('.txt'):
        shutil.move(archivo,'Textos')
        print(f"Archivo movido: {archivo}")
