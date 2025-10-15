#Ejer 1
frutas=['Frutilla','kiwi','Banana']
frutas.insert(1,'Naranja')
frutas.remove('kiwi')
frutas.pop()
print(frutas)

#Ejer 2
ciudades=('pergamino','rosario','buenos aires',)
print(ciudades)
ciudades_mod=list(ciudades)
ciudades_mod.append('bahia blanca')
ciudades_mod.remove('buenos aires')
ciudades_mod.pop(0)
print(ciudades_mod)
ciudades=list(ciudades_mod)
print(ciudades)

#Ejer 3
numeros={3,6,9}
numeros.add(1)
numeros.discard(6)
numeros.pop()
print(numeros) 

#ejer4

alumno={'nombre':'Lucas','edad':'31','curso':'python'}
alumno['apellido']='Sidotti'
alumno.pop('curso')
del alumno['nombre']
print(alumno)

#ejer5
clave='python123'
ingreso=''
intentos=3
while ingreso!=clave:
    ingreso =input('Ingrese su clave ')
    intentos -=1
    print('Quedan ',intentos,'intentos')
    if ingreso == clave:
        print('Bienvenido')
    if intentos ==0:
        print('Usuario bloqueado')
        break