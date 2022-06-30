from scipy import special
import matplotlib.pyplot as plt
x = np.linspace(-3, 3)
plt.plot(x, 1-special.erfc(x))
plt.xlabel('$x$')
plt.ylabel('$erf(x)$')
plt.show()