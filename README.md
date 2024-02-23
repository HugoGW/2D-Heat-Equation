# 2D-Heat-Equation
Simulation of the 2D diffusion equation of heat

In the first step, the aim is to numerically determine a solution of the one-dimensional Fourier heat equation using Fourier series with some approximations, and then we want to numerically solve this equation in 2D.

$\textbf{Solving the 1D heat equation}$

We have a 1D rod of length $L$, and we want to know the evolution of temperature $T$ as a function of time $t>0$ and position $x \in [0,L]$. The evolution of temperature with respect to position and time follows the 1D Fourier heat equation, which is given by:

$\displaystyle (E) : ~~~~ \frac{\partial T}{\partial t} - D \frac{\partial^2 T}{\partial x^2} = 0$

We make the assumption regarding the boundary conditions: $T(0,t) = T(L,t) = 0$, as well as regarding the initial condition : $T(x,0) = f(x) \forall x \in [0,L]$.

Fourier hypothesized that heat could be interpreted as small waves of heat. Building on this, we assume that the temperature $T$ can be interpreted as a Fourier series (to simplify matters, we can assume that $T(x,t)$ is a function $C^{\infty}$) :

$\displaystyle T(x,t) = a_0 + \sum_{n=0}^{\infty} a_n(t) \cos \Big( \frac{\pi n}{L} x \Big) + b_n(t) \sin \Big( \frac{\pi n}{L} x \Big)$

But we recall that $T(0,t) = T(L,t) = 0$, and only the odd part of the series satisfies this condition because $\displaystyle \sin \Big( \frac{\pi n}{L} 0 \Big) = \sin \Big( \frac{\pi n}{L} L \Big) = 0$ so we have :

$\displaystyle T(x,t) =  \sum_{n=0}^{\infty} b_n(t) \sin \Big( \frac{\pi n}{L} x \Big)$

that we will inject into the equation $(E)$ :

$\displaystyle \frac{\partial T}{\partial t} - D \frac{\partial^2 T}{\partial x^2} = 0$

$\displaystyle \frac{\partial }{\partial t} \sum_{n=0}^{\infty} b_n(t) \sin \Big( \frac{\pi n}{L} x \Big) - D \frac{\partial^2 }{\partial x^2} \sum_{n=0}^{\infty} b_n(t) \sin \Big( \frac{\pi n}{L} x \Big) = 0$

$\displaystyle \sum_{n=0}^{\infty} b_n'(t) \sin \Big( \frac{\pi n}{L} x \Big) + D \frac{\pi^2 n^2}{L^2} b_n(t) \sin \Big( \frac{\pi n}{L} x \Big) = 0$

$\displaystyle \sum_{n=0}^{\infty} \Big( b_n'(t) + D\frac{\pi^2 n^2}{L^2} b_n(t) \Big) \sin \Big( \frac{\pi n}{L} x \Big)  = 0$

For a fixed $n$, we have the differential equation $\displaystyle b_n'(t) + D\frac{\pi^2 n^2}{L^2} b_n(t) = 0$, admitting an infinite number of solutions of the form : $b_n(t) = b_n(0) e^{-\frac{D \pi^2 n^2}{L^2} t}$.

So, we have as a solution :

$\displaystyle T(x,t) = \sum_{n=0}^{\infty} b_n(0) e^{-\frac{D \pi^2 n^2}{L^2} t} \sin \Big( \frac{\pi n}{L} x \Big)$

We can then determine $b_n(0)$ using the initial condition : $\displaystyle T(x,0) = f(x) = \sum_{n=0}^{\infty} b_n(0) \sin \Big( \frac{\pi n}{L} x \Big)$

Since we are dealing with a Fourier series, we can calculate the coefficients $b_n(0)$ using the formulas for the Fourier coefficients :

$\displaystyle b_n(0) = \frac{2}{L} \int_0^L f(x) \sin \Big( \frac{\pi n}{L} x \Big) dx$


$\textbf{Solving numerically the 2D heat equation}$

First thing first, we define our parameters for the equation : 

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


I initialize my temperature by creating a matrix of coordordinates 

\begin{equation*}
A_{m,n} = 
\begin{pmatrix}
a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
\vdots  & \vdots  & \ddots & \vdots  \\
a_{m,1} & a_{m,2} & \cdots & a_{m,n} 
\end{pmatrix}
\end{equation*}

      T = np.zeros((Nx, Ny)) + 20  # Initial temperature of the plate : 15°C

Next, my goal is to fixed the initial conditions and boundary conditions. All the map is at 15K (because it's impossible to reach 0K). 
Thus, I want to create a circle at 100K at the center of the map and few elements at 100K too at the edge of the map :

    T[(np.arange(Nx)[:, np.newaxis] - center_x)**2 + (np.arange(Ny) - center_y)**2 == R**2] = 100

    # Boundary conditions
    T[0, :] = np.linspace(T_min, T_max, Ny)
    T[-1, :] = np.linspace(T_min, T_max, Ny)
    T[:, 0] = np.linspace(T_min, T_max, Nx)
    T[:, -1] = np.linspace(T_min, T_max, Nx)



We now come to the heart of the work. We aim to simulate the heat equation using the finite difference method. Therefore, we will discretize this equation as follows: : 

$\frac{\partial T}{\partial t} - D \frac{\partial^2 T}{\partial x^2} = 0$








