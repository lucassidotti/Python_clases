import os
def sistema():
    print("Sistema operativo: ",os.name)#Me devuelve en nombre del OS
    print("La carpeta de trabajo actual es: ",os.getcwd())#Llamo a la carpeta que uso ahora mismo
    #getcwd get current working directory

#Voy a crear una carpeta nueva en mi carpeta de python

print('Carpeta actual',os.getcwd())
print('Creo una carpeta nueva llamada Backup')
os.makedirs('BackUp',exist_ok=True)

#ver el contenido de la carpeta Python_clases

print("La carpeta contiene los siguientes archivos: ",os.listdir())

#Cambiar de carpeta

os.chdir('BackUp')
print(os.getcwd())
