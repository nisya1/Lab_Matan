import matplotlib
from numpy import arange
import numpy as np
from random import choice

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def logistic_map(r, x):
    return r * x * (1 - x)


def variant_map(r, x):
    return r * x * (1 - x) * (2 - x)

n = 20

x_zero = 0.2
r_list = [0.5, 1.0, 1.5, 2.0, 2.3, 2.5]
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, r in enumerate(r_list):
    x_logistic = [x_zero]
    x_variant = [x_zero]

    for i in range(1, n):
        x_logistic.append(logistic_map(r, x_logistic[-1]))
        x_variant.append(variant_map(r, x_variant[-1]))

    n_list = list(range(n))

    axes[idx].plot(n_list, x_logistic, 'bo-', linewidth=1.5, markersize=3, alpha=0.7, label='Логистическое')
    axes[idx].plot(n_list, x_variant, 'ro-', linewidth=1.5, markersize=3, alpha=0.7, label='Вариант 4')

    axes[idx].set_title(f'r = {r}', fontsize=12)
    axes[idx].set_xlabel('n')
    axes[idx].set_ylabel('x_n')
    axes[idx].grid(True, alpha=0.3)
    axes[idx].set_ylim(-0.1, 1.5) 
    axes[idx].legend(fontsize=8)

plt.suptitle(f'Сравнение логистического отображения и варианта 4 (x₀ = {x_zero})', fontsize=16)
plt.tight_layout()
plt.savefig('graf2.png', dpi=300)
plt.show()
