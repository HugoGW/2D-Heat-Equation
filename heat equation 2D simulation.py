import numpy as np
import matplotlib.pyplot as plt

# Parameters
D = 150  #Thermal diffusion coefficient
Lx = 100  #length
Ly = 100  #length
time = 60
Nx = 120  #space nodes
Ny = 120  #space nodes

dx, dy = Lx / Nx, Ly / Ny  #space steps
dt = min(dx**2 / (4 * D), dy**2 / (4 * D))  #time step
Nt = int(time / dt)  #time nodes

T_max, T_min = 100, 0

center_x, center_y = Nx // 2, Ny // 2
R = 10  # Radius of the circle

# Initialization
T = np.zeros((Nx, Ny)) + 20  # Initial temperature of the plate : 15°C
T[(np.arange(Nx)[:, np.newaxis] - center_x)**2 + (np.arange(Ny) - center_y)**2 == R**2] = 100

# Boundary conditions
T[0, :] = np.linspace(T_min, T_max, Ny)
T[-1, :] = np.linspace(T_min, T_max, Ny)
T[:, 0] = np.linspace(T_min, T_max, Nx)
T[:, -1] = np.linspace(T_min, T_max, Nx)

# Plotting
fig, ax = plt.subplots(figsize=(10,8))
pcm = ax.pcolormesh(T, cmap=plt.cm.jet, vmin=T_min, vmax=T_max)
plt.colorbar(pcm, ax=ax)

# Simulation
counter = 0
while counter < time:
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            d2x = (T[i - 1, j] - 2 * T[i, j] + T[i + 1, j]) / dx**2
            d2y = (T[i, j - 1] - 2 * T[i, j] + T[i, j + 1]) / dy**2
            T[i, j] = dt * D * (d2x + d2y) + T[i, j]

    counter += dt
    T[(np.arange(Nx)[:, np.newaxis] - center_x)**2 + (np.arange(Ny) - center_y)**2 == R**2] = 100
    pcm.set_array(T)
    ax.set_title("Time: {:.3f} s, Avg Temperature: {:.2f}".format(counter, np.average(T)))
    plt.pause(0.01)

plt.show()
