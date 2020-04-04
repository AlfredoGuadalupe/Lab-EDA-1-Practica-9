#Al igual que las tuplas, éstas no son mutables
#si se trata de cambiar el contenido, se genera un error
from collections import namedtuple

planeta = namedtuple('planeta', ['nombre', 'numero'])
planeta1 = planeta('Mercurio', 1)

planeta1.nombre = 'Tierra'
