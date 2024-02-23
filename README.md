# 2D-Heat-Equation
Simulation of the 2D diffusion equation of heat

Dnas un premier temps, le but est de déterminer numériquement une solution de l'équation de la chaleur de Fourier 1D avec les séries de Fourier avec quelques approximations puis on souhaite résoudre numériquement cette équation en 2D.

$\textbf{Résolution de l'équation de la chaleur 1D}
On a une barre 1D de longueur $L$ et on souhaite connaitre l'évolution de la température $T$ en fonction du temps $t>0$ et de la position $x \in [0,L]$. L'évolution de la température selon la position et selon le temps suit alors l'équation de la chaleur de fourier 1D soit :

$\displaystyle (E) ~~~~~~ \frac{\partial T}{\partial t} - D \frac{\partial^2 T}{\partial x^2} = 0$

On fait la suppostion quant aux conditions aux bords : $T (0,t) = T (L,t) = 0$ et également quant à la condition initiale : $T(x,0) = f(x) \forall x \in [0,L]$.

Fourier a émis l'hypothèse que la chaleur pouvait s'intepréter comme des petites ondes de chaleurs. Partant de cela, on va supposer que la température $T$ peut s'interpréter comme une série de Fourier (pour simplifier le tout, on peut supposer que $T(x,t)$ est une fonction $C^{\infty}$) :

$\displaystyle T(x,t) = a_0 + \sum_{n=0}^{\infty} a_n(t) \cos \Big( \frac{\pi n}{L} x \Big) + b_n(t) \sin \Big( \frac{\pi n}{L} x \Big)$

Mais on rappelle que $T (0,t) = T (L,t) = 0$ et il n'y a que la partie impaire de la série qui respecte cette condition car $\displaystyle \sin \Big( \frac{\pi n}{L} 0 \Big) = \sin \Big( \frac{\pi n}{L} L \Big) = 0$ donc on a :

$\displaystyle T(x,t) =  \sum_{n=0}^{\infty} b_n(t) \sin \Big( \frac{\pi n}{L} x \Big)$

qu'on va injecter dans l'équation $(E)$ :

$\displaystyle \frac{\partial T}{\partial t} - D \frac{\partial^2 T}{\partial x^2} = 0$

$\displaystyle \frac{\partial }{\partial t} \sum_{n=0}^{\infty} b_n(t) \sin \Big( \frac{\pi n}{L} x \Big) - D \frac{\partial^2 }{\partial x^2} \sum_{n=0}^{\infty} b_n(t) \sin \Big( \frac{\pi n}{L} x \Big) = 0$

$\displaystyle \sum_{n=0}^{\infty} b_n'(t) \sin \Big( \frac{\pi n}{L} x \Big) + D \frac{\pi^2 n^2}{L^2} b_n(t) \sin \Big( \frac{\pi n}{L} x \Big) = 0$

$\displaystyle \sum_{n=0}^{\infty} \Big( b_n'(t) + D\frac{\pi^2 n^2}{L^2} b_n(t) \Big) \sin \Big( \frac{\pi n}{L} x \Big)  = 0$

Pour un $n$ fixé on a l'équation différentielle $\displaystyle b_n'(t) + D\frac{\pi^2 n^2}{L^2} b_n(t) = 0$ admettant une infinité de solution du type : $b_n(t) = b_n(0) e^{-\frac{D \pi^2 n^2}{L^2} t}.

On a donc comme solution :

$\displaystyle T(x,t) = \sum_{n=0}^{\infty} b_n(0) e^{-\frac{D \pi^2 n^2}{L^2} t} \sin \Big( \frac{\pi n}{L} x \Big)$

On peut alors déterminer $b_n(0)$ grâce à la condition initiale : $\displaystyle T(x,0) = f(x) = \sum_{n=0}^{\infty} b_n(0) \sin \Big( \frac{\pi n}{L} x \Big)$

Comme on a à faire à une série de fourier alors on peut calculer les coefficients $b_n(0)$ grâce aux formules des coefficients de Fourier :

$b_n(0) = \frac{2}{L} \int_0^L f(x) \sin \Big( \frac{\pi n}{L} x \Big) dx$




