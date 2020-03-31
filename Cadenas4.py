#Cuando se agrega un numero dentro de {#}, el valor la variable que se encuentra
#en esa posicion dentro de la funcion format{}, sera impreso
cadena1 = 'Hola '
cadena2 = 'Mundo'
num_cadena = "Cambiando el orden: {1} {2} {0} #".format(cadena1, cadena2, 3)
print(num_cadena)
