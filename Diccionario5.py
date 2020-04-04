#Agregando elementos a una llave
elementos2 = {}
elementos2['H'] = {'name': 'Hydrogen', 'number': 1, 'weight': 1.00794}
elementos2['He'] = {'name': 'Helium', 'number': 2, 'weight': 4.002602}
elementos2['H'].update({'gas noble':True})
print (elementos2['H'])
