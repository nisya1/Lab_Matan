import numpy as np
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


def logistic_map(r, x):
    return r * x * (1 - x)


r_list = [3.1, 3.3, 3.5, 3.55, 3.56, 3.568]

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
axes = axes.flatten()

for idx, r in enumerate(r_list):
    x = 0.4
    trajectory = [x]

    for i in range(50):
        x = logistic_map(r, x)
        trajectory.append(x)

    axes[idx].plot(trajectory, 'bo-', linewidth=1, markersize=2)
    axes[idx].set_title(f'r = {r}', fontsize=12)
    axes[idx].set_xlabel('n')
    axes[idx].set_ylabel('$x_n$')
    axes[idx].grid(True, alpha=0.3)
    axes[idx].set_ylim(0.3, 1)

plt.suptitle('Циклы логистического отображения при $r \\in (3, r_\\infty)$', fontsize=14)
plt.tight_layout()
plt.savefig('graf6.png', dpi=300)
plt.show()
