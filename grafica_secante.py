import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 1000)

y = np.exp(x) - np.pi * x


plt.title('f(x)')
plt.plot(x, y, label = 'f(x) = e^x - πx')
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.ylim(-1,1)

plt.show()
