notas = {'Amir':5 , 'dev':4 , 'egfwag':6 , 'dafe':7}
eleccion = input('Que quiere hacer (1)Añadir alumno, (2)Número de aprobados o (3)La clase entera:')
def eleccion_de_funciones(eleccion):
   '''Una funcion para que salte a otras dependiendo la eleccion de la persona
   Parámetros:
   eleccion = Un numero que habra elejido el usuario
   Salidas:
   Dependiendo del numero elejido ira a una funcion o otra
   1 = funcion añadir_alumno
   2 = aprobados
   3 = mostrar_toda_la_clase'''
   if eleccion == 1:
      return añadir_alumno(notas)
   if eleccion == 2:
      return aprobados(notas)
   if eleccion == 3:
      return mostrar_toda_la_clase(notas)

def aprobados(notas):
   '''Una funcion para saber cuantos aprobados hay en la clase
   parametros:
   Nota_min = Numero que nos dice que nota es la minima del aprobado
   cont = Contador para saber cuantos aporbados hat
   con el for i in notas.values() ira por todos los valores del diccionario para saber si son aprobados
   Salidas:
   El numero de aprobados'''
   nota_min = 5
   cont = 0
   for i in notas.values():
      if i >= nota_min:
         cont +=1
   return cont
def mostrar_toda_la_clase(notas):
   '''Funcion que muestra toda las clase
   Parametros:
   clase_total = La lista de clase
   Salidas:
   La lista de toda la clase solo con los nombres'''
   clase_total = notas.keys()
   return clase_total

def añadir_alumno(notas):
   '''Funcion para añadir un alumno al diccionario
   parametros:'''
   while True:
      a=input('Introduzca el nombre del alumno:')
      b=input('Introduzca la nota del alumno escrito:')
      c=input('Si quiere continuar añadiendo dale enter,si acabo escriba (fin):')
      notas[a] = b
      if c == 'fin':
         break
   return notas