import matplotlib
from numpy import arange

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from random import choice


def logshow(r, x):
    return r * x * (1 - x)


# x_zero = choice([i for i in arange(0.1, 1, 0.1)]).round(1)
x_zero = 0.4
r_list = [0.2, 0.4, 0.7]
# r_list = [0.6, 1, 1.4, 2.1, 2.7, 2]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes = axes.flatten()

for idx, r in enumerate(r_list):
    x_list = [x_zero]
    for i in range(1, 20):
        x_list.append(logshow(r, x_list[-1]))

    n_list = list(range(20))

    axes[idx].plot(n_list, x_list, 'bo-', linewidth=1.5, markersize=3)
    axes[idx].set_title(f'r = {r}', fontsize=12)
    axes[idx].set_xlabel('n')
    axes[idx].set_ylabel('x_n')
    axes[idx].grid(True, alpha=0.3)
    axes[idx].set_ylim(-0.1, 1.1)

plt.suptitle(f'Логистическое отображение значений r для x = {x_zero}', fontsize=16)
plt.tight_layout()
plt.savefig('graf3.png', dpi=300)
plt.show()

