import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


r_values = np.linspace(0.0, 2.5, 2500)

iterations = 1000
last = 100


R = []
X = []

for r in r_values:
    for x in np.random.rand(5):

        for _ in range(iterations - last):
            x = r * x * (1 - x) * (2 - x)

        for _ in range(last):
            x = r * x * (1 - x) * (2 - x)
            R.append(r)
            X.append(x)

plt.figure(figsize=(10, 6))
plt.plot(R, X, ',k', alpha=0.25)
plt.xlabel('r')
plt.ylabel('x')
plt.savefig('graf14.png', dpi=300, bbox_inches='tight')
plt.show()