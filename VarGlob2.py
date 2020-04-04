#Se crea una variable local que tiene el mismo nombre que la variable global
vg = 'Global'
def funcion_v2():
    vg = "Local"
    print(vg)
#Llamada a la función 
funcion_v2()  #Imprime valor local

#Imprime la variable global
print(vg)
