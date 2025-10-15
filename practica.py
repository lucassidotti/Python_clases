#print ('Hola mundo')
#edad = 31
#experiencia = 4

#nombre='Lucas'
#profesion='estudiante'

#enviado=True

#noenviado=False

#print('La edad es ',edad,' La experiencia es ',experiencia,)

#Concatenar y mostrar el texto

#nombre='Lucas'
#edad=31

#Concatenamos con coma

#print('Hola soy',nombre,'y tengo',edad)

#Concatenar con signo +

#print('Hola soy '+ nombre +' y tengo '+ str(edad))

#a=10 #int
#b=3 #int
#c=2.5 #float

#print('Suma',a+b)
#print('Resta',a-b)
#print('Multiplicacion',a*b)
#print('Division',round(a/b,3)) #Con decimales
#print('Division entera',a//b)
#print('Resto',a%b) 
#print('Potencia',a**b)

#Combinar operaciones

#total=(a-b)**b
#print('Calculo total',total)

#nombre='Lucas'*3
#print(nombre)

#age=input('Mi edad es')

#print(type(age))

#edades=int(input('Ingresa tu edad: '))
#print('El anio que viene tendras',edades+1,)

#altura=float(input('Cuanto medis en metros'))
#print('Tu altura en centimetros es',altura*100)

#numero=30
#print('El numero es ',str(numero))

#Combinar input

#numero1=int(input('Ingrese un numero'))
#numero2=int(input('Ingrese otro numero'))
#print('La suma de los numeros ingresados es',numero1+numero2)

#Area
#base=float(input('Ingrese la base del triangulo'))
#altura=float(input('Ingrese la altura del triangulo'))
##area=float((base*altura)/2)
#print('El area del triangulo es ',area)

#number=10

#print(number > 8)

#num=50
#num2=45
#print(num>0 and num%2==0)
#print(num2>0 and num2%2==0)

#Usuario sean mayor o igual a 18 o que tenga cuenta

#usuario=False
#edad=21
#mensaje={True:'Usted puede ingresar', False:'Usted no puede ingresar'}
#print(mensaje[usuario or edad>=18])

#Comparar 3 numeros y determinar que al menos 2 sean iguales

#a=3
#b=5
#c=3
#print((a==b) or (a==c) or (b==c) )

#num=int(input('Ingrese un numero '))

#print(num>100)

#x=int(input('Ingrese un numero mayor a 0 '))
#y=int(input('Ingrese un numero menor a 100 '))

#print(x >= y)

#Verificar un password

#password='1234'
#clave=input('Ingrese su password')
#print(clave==password)

#Transformar letras
#letra=input('Ingrese vocales').lower()

#print(letra in 'aeiou')

#Condicion para poder anotarse a un curso
#estudiante=input('Sos estudiante?(S/N)').lower()
#edad=int(input('Que edad tenes?'))

#print(estudiante=='s' or edad>=21)

#Si es true imprime codigo si es falso generar una respuesta 

#edad=15
#if edad>=18:
#    print('Eres mayor a 18')

#else:
#    print('Eres menor a 18')

#anidando ifs

#nota = 63

#if nota >=90:
#   print('Excelente')
#elif nota>=70:
#    print('Aprobado')
#else:
#    print('Recuperatorio')

#combinamos condicionales con operadores logicos

#edad = 20
#anotado_curso = False
#if edad >= 18 and anotado_curso: 
#    print('Usted es mayor a 18 y esta anotado')
#elif edad >=18 and not anotado_curso:
#    print('Usted es mayor pero no esta anotado')
#else: print('Usted es menor, necesita autorizacion')

#Combinar condiciones con or y dos booleanos

#llueve = False
#uso_praguas=False

#if llueve or uso_praguas:
#    print('Me mojo')
#else:
#    print('no me mojo')

#usar not ... invierte el valor de la condicion

#conectado = False

#if not conectado:
#    print('No esta conectado')
#else:
#    print('Estas conectado')

#edad = 16
#tiene_permiso= False
#acompaniado=True

#if (edad>=18 or tiene_permiso) and not acompaniado:
#    print('Puede manejar')
#else: print('No puede manejar')

#Operacion matematica dentro del condicional

#edad = int(input('Ingrese su edad'))
#jubilacion = 65 - edad

#if edad<65:
#    print(f'Te faltan {jubilacion} anios para jubilarte')
#else: print(f'Ya podes jubilarte'.upper)

#Metodos de cadena

#Lower. convertir el string en minuscula

#name = 'PYTHON'

#print(name.lower())

#De forma directa un metodo

#print('HOLA ESTOY HACIENDO UN CURSO'.lower())

#upper es mayuscula

#nombrado='lucas'
#print(f'Mi nombre es {nombrado.upper()}')

#title transforma en mayusculas la primer letra de las palabras que componen el string

#frase='mi buenos aires querido'
#print(f'el tango se llama: {frase}'.title())

#strip quita espacios
#password='          hola             '

#print(password.strip())

#replace reemplaza texto del string

#lenguaje='Me gusta usar Java'

#print(f'{lenguaje.replace("Java","Python")}')

#Split sirve para separar listas
#colores='rojo,negro,blanco'
#print(colores.split('/'))

#Find busca la posicion de un caracter dentro de un string

#palabra='Estoy aprendiendo python'
#print(palabra.find('python'))
#f-string
#print(f'Posicion de thon {palabra.find("thon")}')
#directamente
#print(f'banana '.find('na'))

#count cuenta los caracteres

#fruta='frutilla'
#variable
#print(fruta.count('l'))

#directo
#print('Otorrinolaringologo'.count(''))

#lista colecciones de valores ordenadas y mutables

#frutas=['anana','melon','pera',3]
#print(frutas)

#print(frutas[0])
#print(frutas[-2])

# append agrega al final

#frutas.append('sandia')
#frutas.insert(1,10) #elegimos primero la posicion ',' el elemento a insertar

#print(frutas)

#Elimino elementos de la lista, el primero que coincide
#frutas.remove(3)
#print(frutas)

#pop elimina segun el indice
#borrar=frutas.pop(0)
#print(borrar)

#tuple grupo de elementos que estan ordenados pero no se pueden modificar

#numbers=(10,20,30,40)
#print(numbers[0])

#Combinamos listas y tuple

#coordenadas=[(0,0),(1,1),(2,2),(3,3)]
#print(coordenadas[0])
#print(coordenadas[1][0])

#coordenadas.append((4,4))
#print(coordenadas)

#set elementos desordenados(sin indice) y sin duplicados.

#cosas={'buzo','campera',1,'boxer',1,'buzo'}

#print(cosas)

#agregar un elemento

#cosas.add('pullover')

#discard elimina un elemento si existe.Sino esta no da error.
#cosas.discard('campera')

#print(cosas)

#voy llamar a dos conjuntos y traer elementos que coincidan y elementos propios de cada conjunto.

#a={1,2,3,4}
#b={4,5,6,7,2}

#Unir los dos conjuntos. Es usando el simbolo | .
#print(a | b)

#Interseccion de conjuntos.Son los elementos comunes a los dos conjuntos.&

#print(a & b )

#Diferencia entre los dos conjuntos. Los elementos que traemos son los particulares a cada conjunto.

#print(a - b)
#print(b-a)
 
# ejemplo de una red social.

#seguidores={'Ana','Rosario','Juan Carlos','Pedro'}
#seguidos={'Patricia','Julian','Pedro','Ana'}

#Todos los participantes de mi perfil en la red social.

#print(seguidores | seguidos)

#Personas que te siguen y vos seguis.

#print(seguidores & seguidos)

#Personas que me siguen y no los que yo sigo.

#print(seguidores- seguidos)

#Ecommerce. Dos sucursales.
#sucursal_A={ 'mouse','teclado' ,'monitor'}
#sucursal_B={'teclado','memoria','monitor'}

#print(sucursal_A | sucursal_B)
#print(sucursal_A & sucursal_B)
#print(sucursal_B-sucursal_A)

#Diccionario conjunto de elementos que esta determinado por clave y valor. key=value.

#perfil={"nombre":"Ana",'edad':24 }

#print(perfil)
#print(perfil['edad'])
#print(perfil['nombre'],perfil['edad'])

#Agregar y modificar elementos del diccionario.

#perfil['edad']=44 #Modifico la edad del perfil.
#perfil['profesion']='Maestro'#agregar elemento.

#print(perfil)

#Eliminar un elemento.

#perfil.pop('profesion')#elimino el elemento profesion.
#del perfil['edad']#Otra forma de eliminar elemento.
#print(perfil)

# esta es la manera de traer solos las claves o key/como traer todos los valores/y traemos keys y valores juntos.

#pares={'Apellido':'Galan','edad':120,'Profesion':'Locutor','Ciudad de Nacmiento':'Buenos Aires'}

#pares.keys() #llamas las claves.
#print(pares.keys())
#pares.values()#llama a los valores
#print(pares.values())
#pares.items()#llama el tandem
#print(pares.items())

#Simular la carrito de compras.

#carrito={
#"mouse":1,
#'teclado':0,
#"monitor":3,
#'telefonos':5
#}
#traer la cantidad de productos de un elemento y sumar al stock 1 unidad.

#print(carrito['monitor'])

#carrito['teclado']+=1
#print(carrito['teclado'])

#EJERCICIOS COMBINADOS DE COLECCIONES.

#persona=[{
#'nombre':'Roberto',
#'edad':105,
#'hobbies':('cantar','correr')},
#{'nombre':'Carlos',
# 'edad':120,
#'hobbies':('bailar','futbol')
#}]

#print(persona[0])

#Construir dos perfiles y ver condiciones.

#perfil1={ 'nombre':'Martin','edad':36, 'deportes':('basket','tejo') }
#perfil2={
# 'nombre' :'Melisa',
# 'edad':54,
# 'deportes':('caminar','cuidar')
#}
#comparar edades.

#if perfil1['edad'] > perfil2['edad']:
#     print(f"{perfil1['nombre']} es mayor a {perfil2['nombre']}")
#else:print(f"{perfil2['nombre']} es mayor o tiene la misma edad")

#n=0

#while n<=5:
#    print('Numero de iteracion: ',n)
#    n+=1

#bucle infinito

#x=3

#while x > 0:
#    print(x)
#    x-=1

#break

#i=1
#while True:
#    print(i)
#    if i==5:
#        break
#    i+=1
    
#Continue permite saltar alguna condicion y volver al while hasta que el while sea false

#y=0
#while y<10:
#    y+=1
#    if y % 2==0:
#        continue
#    print(y)

#clave = 'python'
#entrada=''
#while entrada !=clave:
#    entrada=input('Ingrese su clave ')
#print('Acceso correcto')

#clave='python'
#ingreso=''

#while ingreso.lower()!=clave:
#    ingreso=input('Ingrese su clave en minuscula por favor: ')
#print('Acceso correcto')

#Adivina un numero

#import random
#secreto=random.randint(1,10)
#tiro=None
#intento=0
#while tiro !=secreto or intento<=3:
#    intento+=1
#    tiro=int(input('adivina un numero de 1 a 10 '))
#    if tiro < secreto:
#        print('Su numero es demasiado bajo')
#    elif tiro > secreto:
#        print('Su numero es demasiado alto')
#print(tiro, 'es igual a ',secreto)

def saludar():
        print('Hola mundo')
saludar()

def sumar(a,b):
        resultado=a+b
        return(resultado)
print('La suma de los valores es', sumar(2,3))

#valores defecto

def perfil(nombre,saludo='Hola'):
        print(f"{saludo}, soy {nombre}")
perfil('Lucas')
perfil('Gianna','Hello')