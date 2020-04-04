#La función regresa tres, valores, pero sólo nos interesa el primero y el
#tercero
def varios(x):
    return x**2, x**3, x**4

val4, _, val5 = varios(2)
print("{} {}".format(val4, val5))
