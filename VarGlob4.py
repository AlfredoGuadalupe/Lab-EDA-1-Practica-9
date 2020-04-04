#Para resolver el problema anterior y especificar que se quiere hacer uso de la
#variable global dentro de la función funcion_v4(), se tiene que agregar la
#palabra reservada global
vg = "Global"
def funcion_v4():
    global vg
    print(vg)
    vg = "Local"
    print(vg)
#Al momento de ejecutar la función se imprime el valor que tenía asignado vg
#antes de ser modificado por la función. Después de asignar el valor, éste es
#impreso
funcion_v4()

#Se imprime la variable global con su valor modificado
print(vg)
