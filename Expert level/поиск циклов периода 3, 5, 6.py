import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def resize_graf(x1, x2, plt1):
    r_values = np.linspace(x1, x2, 2000)
    iterations = 1000
    last = 200

    x0_values = np.random.rand(1)

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

    plt1.plot(R, X, ',k', alpha=0.4)


fig, axes = plt.subplots(1, 3, figsize=(15, 10))
axes = axes.flatten()

# Первый график - период 3
resize_graf(3.8275, 3.85, axes[0])
axes[0].set_title('Цикл с периодом 3', fontsize=14)
axes[0].set_xlabel('r')
axes[0].set_ylabel('x')

# Второй график - период 5
resize_graf(3.7375, 3.7425, axes[1])
axes[1].set_title('Цикл с периодом 5', fontsize=14)
axes[1].set_xlabel('r')
axes[1].set_ylabel('x')

# Третий график - период 6
resize_graf(3.625, 3.635, axes[2])
axes[2].set_title('Цикл с периодом 6', fontsize=14)
axes[2].set_xlabel('r')
axes[2].set_ylabel('x')

plt.tight_layout()
plt.savefig('graf13.png', dpi=300)
plt.show()
