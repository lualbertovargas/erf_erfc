from matplotlib import pyplot

#Función Lineal.
def f(x):
    return -x
#En esta variable se genera una lista con valores del -10 al 10.
#Todos estos valores serán los que tomara x.
x = range(-10, 10)

#Con el método plot especificamos que función graficaremos.
#El primer argumento es la variable con los valores de x.
#El segundo argumento le pasamos todos estos valares a la función con ayuda de un bucle.
pyplot.plot(x, [f(i) for i in x])

#Establecemos el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

#Especificamos los limites de los ejes.
pyplot.xlim(-10, 10)
pyplot.ylim(-10, 10)

#Guardamos el grafico en una imagen "png".
pyplot.savefig("función_lineal.png")

# Mostramos el gráfico.
pyplot.show
