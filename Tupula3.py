#Probando la mutabilidad de las listas vs la no mutabilidad de las tuplas

lista_diasDelMes=[31,28,31,30,31,30,31,31,30,31,30,31]
tupla_diasDelMes=(31,28,31,30,31,30,31,31,30,31,30,31)
print("valor actual {}".format(lista_diasDelMes[0]))
lista_diasDelMes[0] = 50
print("valor cambiado {}".format(lista_diasDelMes[0]))
tupla_diasDelMes[0]=50  #Esta asignacion manda un error, ya que no pueden
                        #cambiar los valores de na tupla
