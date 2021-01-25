---
layout: post
title: "Regular and singular numerical integration"
date: 2021-01-24 20:49:12 -0600
comments: true
categories: math
---


The Pareto principle (a.k.a. 80/20 rule) says that for many outcomes, roughly 80% of consequences come from 20% of the causes. Qualitatively speaking, this also applies to numerical integration: most of the integral can be handled by just a few quadrature rules.

People who have learned numerical analysis all know about the [Gauss quadrature](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature) rule: for any integer $n>0$, there exist $n$ nodes $x_1,x_2,\dots,x_n\in[-1,1]$ and $n$ corresponding weights $w_1,w_2,\dots,w_n$, such that the approximation

$$
\int_{-1}^1f(x)\,dx\approx \sum_{i=1}^nf(x_i)w_i
$$

is highly accurate for any function $f$ smoothly defined on $[-1,1]$. The error of this approximation typically decays exponentially as $n$ increases. Together with scaling and shifting of variables, the Gauss quadrature efficiently handles all the regular integrals (i.e. integrals involving smooth integrands) on any interval $[a,b]\subset\mathbb{R}$.

What if the integrand is singular? How would you approximate an integral when the integrand is not smooth or even blowing up somewhere on the interval? It turns out that most of the singular integrals in practice can be handled by a few strategies (80/20 rule again!). Here they are:

<!--more-->

**1. Integration by parts.** People in calculus classes may have heard the joke: "Integrate by parts whenever you're not sure what to do." This is sometimes true for singular integrals. For example:

$$
\int_0^1e^x\ln x\,dx = (e^x-1)\ln x\Big|_{x\to0}^1 - \int_0^1\frac{e^x-1}{x}\,dx
$$

then on the right-hand side, the boundary terms evaluate to $0$ while the new integral is in fact regular, so applying the Gauss quadrature will be excellent.

**2. Integration by substitution.** Many singular integrals can be made regular after a change of variables. For example, substituting $x=\cos\theta$ in the integral below yields

$$
\int_{-1}^1\frac{f(x)}{\sqrt{1-x^2}}dx = \int_0^\pi f(\cos\theta)\,d\theta
$$

then, assuming $f$ is smooth, the Gauss quadrature will just work for the second integral.

**3. Product quadratures.** When the integrand is a product of a regular function $f(x)$ and a singular function $w(x)$ (usually refered to as "weight function"), one can often design efficient quadratures of the form

$$
\int_{-1}^1f(x)w(x)\,dx\approx\sum_{i=1}^nf(x_i)w_i
$$

For example, the [Chebyshev quadrature](https://en.wikipedia.org/wiki/Chebyshev%E2%80%93Gauss_quadrature) works perfectly for the integral in the previous example where $w(x)=(1-x^2)^{-1/2}$. On the other hand, both the Gauss quadrature and the Chebyshev quadrature are particular instances from the [Jacobi quadrature](https://en.wikipedia.org/wiki/Gauss%E2%80%93Jacobi_quadrature) family. These example quadrature rules are derived based on the theory of [orthogonal polynomials](https://en.wikipedia.org/wiki/Orthogonal_polynomials), where for each given weight $w(x)$, there is a family of polynomials $\{g_0(x),g_1(x),\dots\}$ such that any two different polynomials are "orthogonal" to each other in the sense that, for any $i\neq j$,

$$
\int_{-1}^1g_i(x)g_j(x)w(x)\,dx=0.
$$

**4. Extrapolation.** The [Romberg integration](https://en.wikipedia.org/wiki/Romberg%27s_method) is an extrapolation method that can enhance the accuracy of quadrature rules define on equally-spaced nodes. As a simple example, consider the following trapezoidal rule approximation with spacing $h=\frac{\pi}{n}$

$$
\int_{-\pi}^\pi\sin|x|\,dx = \sum_{i=-n+1}^{n-1}\sin|ih|h + \frac{\sin|-\pi|+\sin|\pi|}{2}h + E(h)
$$

where the integrand is nonsmooth at $x=0$, and where $E(h)$ is the error that depends on $h$. It turns out that this error can be written as a power series of $h$:

$$
E(h) = C_1h^2+C_2h^4+C_3h^6+\dots
$$

The leading error will be canceled if one appropriately combine an $h$-approximation with a $2h$-approxiation:

$$
E_2(h):=\frac{4E(h)-E(2h)}{3} = C_2'h^4 + C_3'h^6+\dots
$$

The new error is of size $h^4$ which is much smaller than the original $h^2$. This procedure can be done multiple times to cancel the leading errors in the expansion one at a time, such that the accuracy is substantially improved.

**5. Singularity cancellation.** Some singularities are stronger than others. For example, $x\ln x$ is less singular than $\ln x$ because the former is bounded near $x=0$. Let's consider the first example above again that integrates $e^x\ln x$. It is easy to see that the integrand near $0$ behaves like $\ln x$, so we can subtract $\int_0^1\ln x\,dx$ from the original integral and then add it back, that is

$$
\int_0^1e^x\ln x\,dx = \int_0^1(e^x-1)\ln x\,dx+\int_0^1\ln x\,dx
$$

The integral  $\int_0^1\ln x\,dx=-1$ by a simple integration by parts. Then we can apply the $n$-point Gauss quadrature to the remaining integral $\int_0^1(e^x-1)\ln x\,dx$, the error decays roughly like $1/n^4$, much faster than the $1/n^2$ decay rate that you would get if applying the same quadrature to the original integral.

These five strategies, or a combination of them, cover almost all common ways to integrate singular function. One strategy could be more efficiently than another depending on the particular application of interest.

[BOCTAOE](https://www.urbandictionary.com/define.php?term=BOCTAOE). There are situations where none of the above strategies are efficient enough. Such marginal cases attract most of the research efforts. (80/20 rule again.) For example, here is one strategy that I recently took in my research:

**6. Error correction.** Sometimes, it may be necessary to find an explicit expression for the quadrature error $E(h)$, so that you have the power to develop more sophisticated methods tailored to your application of interest. To give an example, consider the integral of $f(x)=e^{-x^2}\ln x$, its right-hand Riemann sum approximation on $[0,6]$ with $n$ subdivisions is

$$
\int_0^6e^{-x^2}\ln x\,dx = \sum_{i=1}^nf(ih)h + E(h) + \epsilon
$$

where $h=\frac{6}{n}$, $\epsilon=\int_6^\infty f(x)\,dx<10^{-16}$ is some small constant that is immaterial in practice. The error $E(h)$ has the following expansion:

$$
E(h) = \sum_{m=0}^{M-1}\frac{(-1)^m}{m!}[\zeta(-2m)\log h-\zeta'(-2m)]h^{2m+1} + O(h^{2M+1}\log h)
$$

where $\zeta(z)$ is the famous [Riemann zeta function](https://en.wikipedia.org/wiki/Riemann_zeta_function).  Such formulae could take a lot of effort to derive in general. But once available, they allow you to develop highly efficient numerical methods.