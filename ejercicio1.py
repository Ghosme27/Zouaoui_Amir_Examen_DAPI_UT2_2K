def ListaNombres():
    '''Un guardado de todos los alumnos que hay en una clase
    Parámetros:
    lista_alumnado = a una lista vacia que se rellenara despues
    Con el while pediremos los alumnos y la lista vacia se convertira en una lista con esos alumnos
    mediante este formato ['Nombre Apellido 1' , 'Nombre Apellido 2' , ... , 'Nombre Apellido N]
    luego con el remove quitaremos la palabra fin y con el sort ordenamos alfabeticamente la lista
    Salidas:
    lista_alumnado
    Una lista de alumnos ordenados alfabeticamente.'''
    lista_alumnado = []
    while True:
        a = input('Añada los alumnos con el nombre y apellido  separado cada alumno pulsando enter,cuando acabe escriba fin:')
        lista_alumnado.append(a)
        if a == 'fin':
            break
    lista_alumnado.remove('fin')
    lista_alumnado.sort()
    return lista_alumnado
   
x=ListaNombres()

def OrdenarNombre(lista_alumnado):
    '''Esta función recibe un ‘nombre y apellido’ y devuelve el ‘apellido, nombre’.
    • Parámetros:
        ◦ Nombre en el formato ‘Nombre Apellido’
    • Salida:
        ◦ Nombre en el formato ‘Apellido, Nombre’'''
    for i in range (len(lista_alumnado)):
        for j in lista_alumnado:
            lista_nueva=[]
            lista_nueva.append(lista_alumnado[j][i])
    return lista_nueva
print(OrdenarNombre(x))