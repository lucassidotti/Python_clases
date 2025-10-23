#no sabemos cuantos parametros va a recibir la funcion

#args * antes del nombre del argumento
def sumar(*argumentos):
    print('La suma de los valores pasados por la funcion es: ',argumentos)
    return sum(argumentos)

print(sumar(8,4))
print(sumar(10,20,34,43,50))

#kargs recibe los  valores en diccionario
#no sabemos cuantos {key:value} vamos a ingresar. sintaxis **

def perfil(**kwargs):
    print(f"Los datos del perfil son {kwargs}")
    for clave,valor in kwargs.items():
        print(f"{clave}:{valor}")

perfil(nombre="Carlos", edad=140, ciudad="Buenos Aires",profesion="cantor")

#sistema de registro de empleado. soy un RRHH

def registro_empleados(*datos_empleado,**perfil_empleado):
    print(f"Datos del empleado: {datos_empleado}")
    print(f"Datos adicionales")
    for key,value in perfil_empleado.items():
        print(f" -{key}:{value}")
    print('Empleado registrado \n')

registro_empleados('Roberto','Galan',98,'Gerente',sector='ventas',antiguedad=45,ciudad='Pergamino')
registro_empleados('Monica','Gonzaga',telefono=24771234254)
registro_empleados('Tomas',45,'Empleado',mail='toto@gmail.com')



