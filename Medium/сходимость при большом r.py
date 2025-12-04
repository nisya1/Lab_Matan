import matplotlib
from numpy import arange

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from random import choice


def logshow(r, x):
    return r * x * (1 - x)


# x_zero = choice([i for i in arange(0.1, 1, 0.1)]).round(1)
x_zero = 0.7
r = 2.6
long = 30
# r_list = [0.6, 1, 1.4, 2.1, 2.7, 2]


x_list = [x_zero]
for i in range(1, long):
    x_list.append(logshow(r, x_list[-1]))

n_list = list(range(long))

x1 = [x_list[i] for i in range(long) if i % 2 == 0]
y1 = [n_list[i] for i in range(long) if i % 2 == 0]

x2 = [x_list[i] for i in range(long) if i % 2 != 0]
y2 = [n_list[i] for i in range(long) if i % 2 != 0]

plt.plot(y1, x1, 'bo-', linewidth=1.5, markersize=3)
plt.plot(y2, x2, 'bo-', linewidth=1.5, markersize=3)
# plt.plot(n_list, x_list, 'bo-', linewidth=1.5, markersize=3)

plt.title(f'r = {r}', fontsize=12)
plt.xlabel('n')
plt.ylabel('x_n')
plt.grid(True, alpha=0.3)
plt.ylim(-0.1, 1.1)

plt.tight_layout()
plt.savefig('graf4.png', dpi=300)
plt.show()
