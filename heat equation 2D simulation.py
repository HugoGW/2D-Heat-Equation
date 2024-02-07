import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 150
length = 100
time = 60
nodes = 120

dx, dy = length / nodes, length / nodes
dt = min(dx**2 / (4 * a), dy**2 / (4 * a))
t_nodes = int(time / dt)

T_max, T_min = 100, 0

center_x, center_y = nodes // 2, nodes // 2
R = 10  # Radius of the circle

# Initialization
T = np.zeros((nodes, nodes)) + 20  # Initial temperature of the plate : 15°C
T[(np.arange(nodes)[:, np.newaxis] - center_x)**2 + (np.arange(nodes) - center_y)**2 == R**2] = 100

# Boundary conditions
T[0, :] = np.linspace(T_min, T_max, nodes)
T[-1, :] = np.linspace(T_min, T_max, nodes)
T[:, 0] = np.linspace(T_min, T_max, nodes)
T[:, -1] = np.linspace(T_min, T_max, nodes)

# Plotting
fig, ax = plt.subplots(figsize=(10,8))
pcm = ax.pcolormesh(T, cmap=plt.cm.jet, vmin=T_min, vmax=T_max)
plt.colorbar(pcm, ax=ax)

# Simulation
counter = 0
while counter < time:
    for i in range(1, nodes - 1):
        for j in range(1, nodes - 1):
            d2x = (T[i - 1, j] - 2 * T[i, j] + T[i + 1, j]) / dx**2
            d2y = (T[i, j - 1] - 2 * T[i, j] + T[i, j + 1]) / dy**2
            T[i, j] = dt * a * (d2x + d2y) + T[i, j]

    counter += dt
    T[(np.arange(nodes)[:, np.newaxis] - center_x)**2 + (np.arange(nodes) - center_y)**2 == R**2] = 100
    pcm.set_array(T)
    ax.set_title("Time: {:.3f} s, Avg Temperature: {:.2f}".format(counter, np.average(T)))
    plt.pause(0.01)

plt.show()
