#Área del triángulo
lad1=3 #lado 1
lad2=5 #lado 2
lad3=2 #lado 3
b=3 #base
h=6 #altura
area = (b*h)/2
peri = lad1+lad2+lad3
print("AREA Y PERIMETRO de un triángulo cuyas medidas son: lados = "+str(lad1)+
      ', '+str(lad2)+' y '+str(lad3)+", base = "+str(b)+", altura = "+str(h))
print("\tEl area del triángulo es "+str(area))
print("\tEl perimetro del triangulo es "+str(peri))
#Área del rectángulo
b=5 #base
h=4 #altura
area = b*h
peri = 2*(b+h)
print("\nAREA Y PERIMETRO de un rectángulo cuyas medidas son: base = "+str(b)+
      ", altura = "+str(h))
print("\tEl area del rectángulo es "+str(area))
print("\tEl perimetro del rectangulo es "+str(peri))
#Área del circulo
PI = 3.14
rad=4 #radio
area = PI*(rad*rad)
peri = PI*(2*rad)
print("\nAREA Y PERIMETRO de un circulo de radio = "+str(rad))
print("\tEl area del circulo es "+str(area))
print("\tEl perimetro del circulo es "+str(peri))
#Area del trapecio
#Área del rectángulo
bmen=2 #base menor
bMAY=5 #base mayor
ladt1=4 #lado 1
ladt2=4 #lado 1
h=4 #altura
area = ((bmen+bMAY)*h)/2
peri = bmen+bMAY+ladt1+ladt2
print("\nAREA Y PERIMETRO de un trapecio cuyas medidas son: base mayor = "
      +str(bMAY)+", base menor = "+str(bmen)+", altura = "+str(h)+", lados = "
      +str(ladt1)+' y '+str(ladt2))
print("\tEl area del trapecio es "+str(area))
print("\tEl perimetro del trapecio es "+str(peri))
