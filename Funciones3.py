#Definiendo una función que regrese más de un valor
def varios(x):
    return x**2, x**3, x**4
#Los valores que regresa la función pueden ser guardado en variables
#separadas por ,
val1, val2, val3 = varios(2)
print("{} {} {}".format(val1, val2, val3))
