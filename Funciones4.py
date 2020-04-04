#Función con un parámetro con un valor por defecto
def cuadrado_default(x=3):
    return x**2
#Como la función tiene un valor por default, si se manda llamar la función
#sin especificar el parámetro, se toma el que tiene por defecto
print(cuadrado_default())
