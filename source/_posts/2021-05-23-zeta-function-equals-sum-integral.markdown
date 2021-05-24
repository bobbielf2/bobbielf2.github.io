---
layout: post
title: "Zeta Function = Sum - Integral"
date: 2021-05-23 22:57:33 -0400
comments: true
categories: math
---


Recently I saw some memes about the peculiar "sum"

$$
1+2+3+4+\dots = -1/12
$$

{% img center /images/blog_figures/zeta_simpsons.jpeg 400 %}

{% img center /images/blog_figures/zeta_trolley_problem.jpeg 400 %}

These memes are inspired by the Riemann zeta function

$$
\zeta(s) := \sum_{n=1}^\infty\frac{1}{n^s},\qquad (s>1)
$$

in which directly substituting $s=-1$ gives the $-\tfrac{1}{12}$ "sum" above.

<!--more-->

This $1+2+3+4+\dots = -1/12$ joke was first popularized by the 2014 [numberphile video](https://youtu.be/w-I6XTVZXww). The video went viral and caused a lot of confusions due to the lack of proper explanations. 

Indeed, adding $1+2+3+4+\dots$ will blow up to infinity in the usual sense. The definition of $\zeta(s)$ by summing $1/n^s$ only makes sense for $s>1$; when $s<1$, the value $\zeta(s)$ is in fact obtained by [analytic continuation](https://en.wikipedia.org/wiki/Analytic_continuation). Later in 2018, Mathologer gave an [accessible clarification](https://youtu.be/YuIIjLr6vUA) which only requires a minimal background in calculus to understand.

### A New Perspective on the Zeta Function

Here, I will provide another interesting perspective on the continuation of $\zeta(s)$, which I think is quite beautiful and deserves more attentions. This is stated in the title of this article:

> zeta function $=$ sum $-$ integral.

Specifically, 

$$
\zeta(s) = \sum_{n=1}^\infty\frac{1}{n^s} - \int_0^\infty\frac{1}{x^s}\,dx.
$$

This relationship holds for any $s$ in the complex plane $\mathbb{C}$, provided we define this expression appropriately.

### The Proof

For simplicity, let's start with $-1<\mathrm{Re}(s)<1$, which is a vertical strip in $\mathbb{C}$ where both the sum and the integral diverge. Then an appropriate zeta-sum-integral connection can be written as

$$
\zeta(s) = \lim_{N\to\infty}\Big(\sum_{n=1}^N\frac{1}{n^s} - \int_0^{N+\frac{1}{2}}\frac{1}{x^s}\,dx\Big),\qquad -1<\mathrm{Re}(s)<1
$$

To paint a clearer picture, let's use some visual help and consider the above limit on the real line:

{% img center /images/blog_figures/zeta_proof_visual.png 500 %}

Here, the red dots are the integer points $n = 1, 2, 3,\dots$, and the blue bars divide the real line into boxes of unit length $[\frac12, \frac32], [\frac32, \frac{5}{2}], [\frac{5}{2}, \frac{7}{2}], \dots$

Based on this picture, let's first define some quantities of interest:

- Define the partial sum $S_N(s) := \sum_{n=1}^N\frac{1}{n^s}$	which is a sum on the first $N$ red dots in the picture above.
- Define the finite integral $I_N(s) := \int_{\frac12}^{N+\frac12}\frac{1}{x^s}\,dx$	which is an integral in the first $N$ boxes defined by the blue bars in the picture.
- Define the difference $Z_N(s) := S_N(s) - I_N(s)$, then 

$$Z_N(s) = \sum_{n=1}^N\Big(\frac{1}{n^s} - \int_{n-\frac12}^{n+\frac12}\frac1{x^s}\,dx\Big)$$ 

is a sum of $N$ items in the first $N$ boxes. The $n$th item $\Delta Z_n(s):=\frac{1}{n^s} - \int_{n-\frac12}^{n+\frac12}\frac1{x^s}\,dx$ is the difference between a term at the $n$th red dot and an integral over the containing blue box.

Next, we realize some nice properties of the sum $Z_N(s)$

- Looking at each term in the sum $Z_N(s)$

	$$ \Delta Z_n(s) := \frac{1}{n^s} - \int_{n-\frac12}^{n+\frac12}\frac1{x^s}\,dx = \int_{-\frac12}^{\frac12}\Big(\frac{1}{n^s}-\frac{1}{(n+x)^s}\Big)dx,$$
	
	we find that for any fixed $n$, $\Delta Z_n(s)$ is an analytic function of $s\in\mathbb{C}$.

- By a comparison with $\sum_{n=1}^\infty\frac{1}{n^{s+2}}$, it is not hard to establish the convergence of $Z_\infty(s) = \sum_{n=1}^\infty\Delta Z_N(s)$ for all $\mathrm{Re}(s)>-1$. This indicates that $Z_\infty(s)$ is an analytic function for all $\mathrm{Re}(s)>-1$.

With these setup, let's start our proof, which will be very straightforward.
	
- We first notice that

	$$\begin{aligned}I_0(s)&:=\int_0^{\frac12}\frac{1}{x^s}\,dx = \frac{2^{s-1}}{1-s},\qquad \mathrm{Re}(s)<1,\\ J_0(s)&:=\int_{\frac12}^\infty\frac{1}{x^s}\,dx = -\frac{2^{s-1}}{1-s},\qquad \mathrm{Re}(s)>1, \end{aligned}$$
	
	So $I_0(s)$ and $-J_0(s)$ are analytic continuations of each other to the respective half-planes. Consequently, the following two functions are also analytic continuations of each other
	
	$$\begin{cases}Z_\infty(s)-I_0(s), &-1<\mathrm{Re}(s)<1\\ Z_\infty(s) + J_0(s), &\mathrm{Re}(s)>1\end{cases}$$

- Our goal is to show that 

	$$\zeta(s) = Z_\infty(s) - I_0(s),\qquad-1<\mathrm{Re}(s)<1,$$

	therefore we will be done once it is shown that $\zeta(s) = Z_\infty(s) + J_0(s)$ for $\mathrm{Re}(s)>1$. This can be shown simply:

	$$\begin{aligned}Z_\infty(s) + J_0(s) &= \lim_{N\to\infty}\Big(\sum_{n=1}^N\frac{1}{n^s} - \int_{\frac12}^{N+\frac{1}{2}}\frac{1}{x^s}\,dx\Big)+\int_{\frac12}^\infty\frac{1}{x^s}\,dx \\ &=\sum_{n=1}^\infty\frac{1}{n^s} + \lim_{N\to\infty}\int_{N+\frac{1}{2}}^\infty\frac{1}{x^s}\,dx\\ &=\zeta(s)+0 \end{aligned}$$
	
	Q.E.D.

### Euler-Maclaurin Formula and the Zeta Function

The famous Euler-Maclarin formula is an important tool for approximating integrals on a uniform grid. Probably lesser-known is its connection to the zeta function.

The typical Euler-Maclaurin formula on the integer grid $n=0,1,2,\dots,N$ is

$$\sum_{n=1}^{N-1}f(n)+\frac{f(0)+f(N)}{2} = \int_0^Nf(x)\,dx+\sum_{m=2}^\infty\frac{B_{m}}{m!}\Big(f^{(m-1)}(N)-f^{(m-1)}(0)\Big)$$

Using the relationship between the the Bernoulli numbers and the zeta function, we can rewrite this as

$$
\begin{aligned}
\sum_{m=0}^\infty\frac{\zeta(-m)}{m!}\Big(f^{(m)}(0)+(-1)^mf^{(m)}(N)\Big) = \sum_{n=1}^{N-1}f(n) - \int_0^Nf(x)\,dx
\end{aligned}
$$

It is remarkable that we once again return to the "zeta = sum - integral" relation. 

Let's simplify this further. If we substitute $f(x) = x^k$ into the formula, a lot of the terms become zero and we get

$$
\begin{aligned}
\zeta(-k) + \sum_{m=0}^k\frac{\zeta(-m)}{m!}(-1)^mf^{(m)}(N) = \sum_{n=1}^{N-1}n^k - \int_0^Nx^k\,dx
\end{aligned}
$$

Then we let $N\to\infty$ and think of the limiting integral as a [Hadamard finite part integral](https://en.wikipedia.org/wiki/Hadamard_regularization) (f.p.), this yields

$$
\begin{aligned}
\zeta(-k) = \sum_{n=1}^\infty\frac{1}{n^{-k}} - f.p.\int_0^\infty\frac{1}{x^{-k}}\,dx
\end{aligned}
$$

This is exactly the "zeta = sum - integral" relation! So the Euler-Maclaurin formula is just a special case of this connection after all. (Alternatively, one can think of the finite part integral as two integrals $\int_0^1x^k\,dx$ and $\int_1^\infty x^k\,dx$, then use the analytic continuation idea, like for the $I_0$ and $J_0$ integrals in the above proof, to show that they add to $0$.)

We see that using appropriate notions, the relation

$$
\zeta(s) = \sum_{n=1}^\infty\frac{1}{n^s} - \int_0^\infty\frac{1}{x^s}\,dx.
$$

holds for all values of $s\in\mathbb{C}$.

I have written before about [integrating singular functions](/blog/2021/01/24/regular-and-singular-numerical-integration/) using this zeta relation, but the Euler-Maclarin formula shows that such relation also works for regular integrals. So, and here is the punchline, an even more beautiful fact is that we can handle both singular and regular integrals categorically using just one zeta relation![^sidi]

[^sidi]: For more general zeta function connections, see the recent [book chapter](http://www.cs.technion.ac.il/~asidi/Sidi_Journal_Papers/P130_AQC.Asymp_Expansions.pdf) by Avraham Sidi.
