elementos2 = {}
elementos2['H'] = {'name': 'Hydrogen', 'number': 1, 'weight': 1.00794}
elementos2['He'] = {'name': 'Helium', 'number': 2, 'weight': 4.002602}
elementos2['H'].update({'gas noble':True})

#Muestra todos los elementos del diccionario
print (elementos2.items())

#Muestra todas las llaves del diccionario
print (elementos2.keys())
