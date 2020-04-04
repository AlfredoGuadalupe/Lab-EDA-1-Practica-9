#Se trata de imprimir el valor de la variable global, a diferencia de la
#función_v1(), se creó en el espacio local de la funcion_v3() una variable con
#el mismo nombre, por lo que se reemplaza la variable global
vg = "Global"
def funcion_v3():
    print(vg)
    vg = "Local"
    print(vg)
#Como se tiene una variable local y no se le ha asignado un valor, se genera
#un error
funcion_v3()
