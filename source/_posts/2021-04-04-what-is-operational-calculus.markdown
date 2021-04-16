---
layout: post
title: "What is operational calculus? Finite differences and the Euler-Maclaurin formula"
date: 2021-04-04 23:45:42 -0500
comments: true
categories: [math, yq]
---



When we first learned ordinary differential equations (ODEs) in class, we were told that the solution of

$$
f'(x)=f(x)
$$

is $f(x)=Ce^x$ for an arbitrary constant $C$. We were told that this solution can be obtained either by observation and guessing (then it's easy to verify solution), or by a separation of variable (e.g. integrate $dy/y=dx$). But these approaches don't tell us what to do for higher-order equations, such as $f'\'-3f'+2f=0$.

The **operational calculus** provides a convenient way to algebraically derive the solution to these linear ODEs. The derivation goes as follows.

<!--more-->

- We want to solve the ODE $f'(x)=f(x)$, or equivalently $(\frac{d}{dx}-1)f(x)=0$.
- Define the differential operator $D:=\frac{d}{dx}$, then the equation becomes $(D-1)f(x)=0$.
- Define the integral operator $J$ such that $Jf(x):=\int_0^xf(t)dt$. (Therefore by the fundamental theorem of calculus, for any smooth function $g(x)$ we have $DJg(x)= g(x)$ and $JDg(x)=g(x)+C$, where the constant $C=-g(0)$. In particular, if $g(0)=0$ then we have $DJg(x)=JDg(x)=g(x)$, so we can write $J=D^{-1}$.)
- Rewrite the ODE as $\frac{1-D^{-1}}{D^{-1}}f(x)=0$, so $f(x)=\frac{D^{-1}}{1-D^{-1}}0 = \frac{1}{1-J}(D^{-1}0)$
- Suppose the above $0$ function is the derivative of some constant $C$, that is, $D^{-1}0=C$, then $f(x)=\frac{1}{1-J}C=C\left(\frac{1}{1-J}1\right)$
- By the Taylor series we have $\frac{1}{1-J}=1 + J+J^2+\dots=\sum_{n=0}^\infty J^{n}$, we can write $f(x)=C\sum_{n=0}^\infty J^{n}1$
- By induction, $J1=\int_0^x1\,dt=x,\; J^21=\int_0^xt\,dt=\frac{x^2}{2},\dots,J^n1=\frac{x^n}{n!}$. Therefore $f(x)=C\sum_{n=0}^\infty \frac{x^n}{n!}=C e^x$.

Similarly we can show that $(D-a)f(x)=0$ has a solution $f(x)=Ce^{ax}$. Then for a higher-order equation such as $f'\'-3f'+2f=0$, we can rewrite it as $(D^2-3D+2)f=0$ which can be then factored into $(D-1)(D-2)f(x)=0$, implying either $(D-1)f=0$ or $(D-2)f=0$. 

Operational calculus reduces a differential equation into an algebraic equation, which is often much easier to solve.

### The calculus of finite differences

The calculus of finite differences is a brilliant extension of the operational calculus to discrete quantities. The most important observation is that, given the *shift operator*

$$
Ef(x):=f(x+h),
$$

there is this remarkable *exponential map*, $E=\exp(hD)$, that connects the continuous and discrete worlds. This exponential map is simply a different way of writing the Taylor series expansion:

$$
Ef(x)=\exp(hD)f(x)=\left(1+hD+\frac{(hD)^2}{2!}+\frac{(hD)^3}{3!}+\dots\right)f(x)
$$

From here, a lot of the great things can happen. For example, if we want to derive a *forward difference* formula such as

$$
f'(x)\approx \frac{f(x+h)-f(x)}{h},
$$

we can define the forward difference operator

$$
\Delta f(x):=f(x+h)-f(x)=(E-1)f(x)
$$

and write down the relationship

$$
\Delta+1=E=\exp(hD).
$$

Then it follows naturally that

$$
D=\frac{1}{h}\log(1+\Delta)=\frac{1}{h}\left(\Delta - \frac{\Delta^2}{2} + \frac{\Delta^3}{3} - \dots\right)
$$

Truncating this series at the first term gives back the first-order difference formula $f'(x)\approx\frac{1}{h}\Delta f(x)$ as before; truncating at the second term gives the second-order formula

$$
f'(x)\approx\frac{1}{h}(\Delta-\Delta^2/2)f(x)=\frac{1}{h}\left(-\frac{1}{2}f(x+2h)+2f(x+h)−\frac{3}{2}f(x)\right)
$$

and so on.

### The Euler-Maclaurin formula

Another striking application of such finite difference calculus is to derive the more advanced [*Euler-Maclaurin formula*](https://en.wikipedia.org/wiki/Euler%E2%80%93Maclaurin_formula), which is in some sense a discrete version of the fundamental theorem of calculus.

As we have mentioned in the first part of this article, the fundamental theorem of calculus can be written in terms of operators as

$$
D^{-1}f(x)=Jf(x)+C=\int_0^xf(t)\,dt+C
$$

So we would like to know if we replace the differential operator $D$ with the difference operator $\Delta$, how would this relationship change? What is $\Delta^{-1}f(x)$?

We have shown previously that $1+\Delta=\exp(hD)$, so it would be naturaly to write

$$
\Delta^{-1}=\frac{1}{\exp(hD)-1}.
$$

However, the above right-hand side corresponds to the function $1/(e^x-1)$ which is singular at the origin, so instead we write

$$
\Delta^{-1}=\frac{hD}{\exp(hD)-1}(hD)^{-1}=\sum_{n=0}^{\infty}\frac{B_n}{n!}(hD)^{n}(hD)^{-1}.
$$

Here we have used the fact that

$$
\frac{x}{e^x-1}=\sum_{n=0}^{\infty}\frac{B_n}{n!}x^n
$$

where $B_n$ are the [Bernoulli numbers](https://en.wikipedia.org/wiki/Bernoulli_numbers). Notice that with our notations, we have

$$
(hD)^{-1}f(x)=\frac{1}{h}\int_0^xf(t)\,dt+C
$$

and

$$
(hD)^{n}(hD)^{-1}f(x)=h^{n-1}f^{(n-1)}(x)
$$

therefore

$$
\Delta^{-1}f(x)=\frac{1}{h}\int_0^xf(t)\,dt+C+\sum_{n=1}^{\infty}\frac{B_n}{n!}h^{n-1}f^{(n-1)}(x)
$$

Now apply $\Delta$ on both sides, we have

$$
f(x)=\frac{1}{h}\int_x^{x+h}f(t)\,dt+\sum_{n=1}^{\infty}\frac{B_n}{n!}h^{n-1}(f^{(n-1)}(x+h)-f^{(n-1)}(x))
$$

This is one version of the Euler-Maclaurin formula. Finally, if we replace $x$ by $a,\;a+h,\;a+2h,\;\dots,\;a+(m-1)h$, one-by-one, and sum all the resulting formulae together, we get

$$
\sum_{k=0}^{m-1}f(a+kh)=\frac{1}{h}\int_a^bf(t)\,dt+\sum_{n=1}^{\infty}\frac{B_n}{n!}h^{n-1}\left(f^{(n-1)}(b)-f^{(n-1)}(a)\right)
$$

where $b:=a+mh$. So here we are, this gives us the usual form of the Euler-Maclaurin formula.