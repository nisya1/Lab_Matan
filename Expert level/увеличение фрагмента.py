import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


r_values = np.linspace(3.82, 3.86, 2000)
iterations = 1000
last = 50

x0_values = np.random.rand(5)

R = []
X = []

for r in r_values:
    for x0 in x0_values:
        x = x0
        for i in range(iterations - last):
            x = r * x * (1 - x)
        for i in range(last):
            x = r * x * (1 - x)
            R.append(r)
            X.append(x)

plt.figure(figsize=(8, 5))
plt.plot(R, X, ',k', alpha=0.4)
plt.xlabel("r")
plt.ylabel("$x_n$")
plt.title("Увеличенный фрагмент бифуркационной диаграммы около $r \\approx 3.83$")
plt.savefig('graf11.png', dpi=300, bbox_inches='tight')
plt.show()