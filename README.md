# 2D-Heat-Equation
Simulation of the 2D diffusion equation of heat

Dnas un premier temps, le but est de déterminer numériquement une solution de l'équation de la chaleur de Fourier 1D avec les séries de Fourier avec quelques approximations puis on souhaite résoudre numériquement cette équation en 2D.

$\textbf{Résolution de l'équation de la chaleur 1D}
On a une barre 1D de longueur $L$ et on souhaite connaitre l'évolution de la température $T$ en fonction du temps $t>0$ et de la position $x \in [0,L]$. L'évolution de la température selon la position et selon le temps suit alors l'équation de la chaleur de fourier 1D soit :

$\displaystyle \frac{\partial T}{\partial t} - D \frac{\partial^2 T}{\partial x^2}$

On fait la suppostion quant aux conditions aux bords : $T (0,t) = T (L,t) = 0$ et également quant à la condition initiale : $T(x,0) = f(x) \forall x \in [0,L]$.

Fourier a émis l'hypothèse que la chaleur pouvait s'intepréter comme des petites ondes de chaleurs. Partant de cela, on va supposer que la température $T$ peut s'interpréter comme une série de Fourier (pour simplifier le tout, on peut supposer que $T(x,t)$ est une fonction $C^{\infty}$) :

$\displaystyle T(x,t) = a_0 + \sum_{n=0}^{\infty} a_n(t) \cos \bigg( \frac{\pi n}{L} x \bigg) + b_n(t) \sin \Big( \frac{\pi n}{L} x \Big)$

