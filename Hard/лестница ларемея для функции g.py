import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


def variant_map(r, x):

    return r * x * (1 - x) * (2 - x)


def plot_lamerey_grid():
    r_values = [2.0, 3.2, 3.5, 3.55, 3.565, 3.7]
    x0 = 0.4

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()

    for idx, r in enumerate(r_values):
        ax = axes[idx]

        x = np.linspace(0, 1, 200)
        y = variant_map(r, x)
        ax.plot(x, y, 'b-', linewidth=1.5)
        ax.plot(x, x, 'k--', linewidth=1, alpha=0.5)

        steps = 15 if r < 1.5 else 20
        x_points = [x0, x0]
        y_points = [0, variant_map(r, x0)]

        current_x = x0
        for i in range(steps - 1):
            new_x = y_points[-1]
            x_points.extend([new_x, new_x])
            y_points.extend([y_points[-1], y_points[-1]])

            new_y = variant_map(r, new_x)
            x_points.extend([new_x, new_x])
            y_points.extend([y_points[-1], new_y])

            current_x = new_x

        ax.plot(x_points, y_points, 'ro-', linewidth=1, markersize=2, alpha=0.8)
        ax.set_title(f'$r = {r}$', fontsize=12)
        ax.set_xlabel('$x_n$')
        ax.set_ylabel('$x_{n+1}$')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 1)
        ax.set_ylim(-2, 2)

    plt.suptitle('Лестница Ламерея для варианта 4: $g(x) = r x (1-x)(2-x)$', fontsize=14)
    plt.tight_layout()
    plt.savefig('graf8.png', dpi=300, bbox_inches='tight')
    plt.show()

plot_lamerey_grid()