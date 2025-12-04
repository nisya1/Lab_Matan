import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def lamerey_stairs_single(r, x0, n_steps, ax):
    x = np.linspace(0, 1, 200)
    y = r * x * (1 - x)

    ax.plot(x, y, 'b-', linewidth=1.2)
    ax.plot(x, x, 'k--', linewidth=1, alpha=0.5)

    x_vals = [x0]
    y_vals = [0]
    current_x = x0

    for i in range(n_steps):
        next_y = r * current_x * (1 - current_x)
        x_vals.extend([current_x, current_x])
        y_vals.extend([y_vals[-1], next_y])
        x_vals.append(next_y)
        y_vals.append(next_y)
        current_x = next_y

    ax.plot(x_vals, y_vals, 'ro-', linewidth=1, markersize=2, alpha=0.8)
    ax.set_title(f'$r = {r}$', fontsize=11)
    ax.set_xlabel('$x_n$')
    ax.set_ylabel('$x_{n+1}$')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)


fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

lamerey_stairs_single(2.0, 0.4, 10, axes[0])
lamerey_stairs_single(3.2, 0.4, 12, axes[1])
lamerey_stairs_single(3.5, 0.4, 16, axes[2])
lamerey_stairs_single(3.55, 0.4, 20, axes[3])
lamerey_stairs_single(3.565, 0.4, 25, axes[4])
lamerey_stairs_single(3.7, 0.4, 30, axes[5])

plt.suptitle('Лестница Ламерея', fontsize=14)
plt.tight_layout()
plt.savefig('graf7.png', dpi=300, bbox_inches='tight')
plt.show()