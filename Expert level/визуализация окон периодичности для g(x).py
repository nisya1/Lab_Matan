import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def resize_graf(x1, x2, plt1):
    r_values = np.linspace(x1, x2, 2000)
    iterations = 1000
    last = 100

    x0_values = np.random.rand(1)

    R = []
    X = []

    for r in r_values:
        for x0 in x0_values:
            x = x0
            for i in range(iterations - last):
                x = r * x * (1 - x) * (2 - x)
            for i in range(last):
                x = r * x * (1 - x) * (2 - x)
                R.append(r)
                X.append(x)

    plt1.plot(R, X, ',k', alpha=0.4)


fig, axes = plt.subplots(1, 2)
axes = axes.flatten()

resize_graf(2.32, 2.36, axes[0])
axes[0].set_xlabel('r')
axes[0].set_ylabel('x')

resize_graf(2.42, 2.44, axes[1])
axes[1].set_xlabel('r')
axes[1].set_ylabel('x')

plt.tight_layout()
plt.savefig('graf15.png', dpi=300)
plt.show()
