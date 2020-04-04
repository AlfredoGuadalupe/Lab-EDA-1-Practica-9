#Definiendo una función que regresa el cuadrado de un número
def cuadrado(x):
    return x**2
x = 5
#La función format() sirve para convertir los parámetros que recibe,
#en cadenas; éstos valores son reemplazadas por las llaves de la cadena.
print("El cuadrado de {} es {}".format(x, cuadrado(x)))
#La función cuadrado() regresa un valor
