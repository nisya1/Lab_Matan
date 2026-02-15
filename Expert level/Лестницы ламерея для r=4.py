import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def two_lamerey_stairs(r, x0, yo, plot):
    x = np.linspace(0, 1, 200)
    y = r * x * (1 - x)

    plot.plot(x, y, 'b-', linewidth=1.2)
    plot.plot(x, x, 'k--', linewidth=1)

    lamerey_stairs(r, x0, plot, "red")
    lamerey_stairs(r, yo, plot, "green")


def lamerey_stairs(r, x0, plot, color):
    x_vals = [x0]
    y_vals = [0]
    current_x = x0

    n_steps = 5
    for i in range(n_steps):
        next_x = r * current_x * (1 - current_x)
        x_vals.append(current_x)
        y_vals.append(next_x)

        x_vals.append(next_x)
        y_vals.append(next_x)
        current_x = next_x

    plot.plot(x_vals, y_vals, color, linewidth=1, markersize=2, alpha=0.8)


r = 4
x0 = 0.1
e = 0.01
y0 = x0 + e
two_lamerey_stairs(r, x0, y0, plt)

plt.suptitle('Лестница Ламерея', fontsize=14)
plt.savefig('graf9.png', dpi=300, bbox_inches='tight')
plt.show()
