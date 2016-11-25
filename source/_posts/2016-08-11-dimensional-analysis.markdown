---
layout: post
title: "Dimensional Analysis"
author: "波儿比 Bobbie"
date: 2016-08-11 16:00:40 -0400
comments: true
categories: [fluid-dynamics, PDE]
published: true
---

Once one of my engineering friends asked me: “Why would you need all these dimensionless numbers? There are so many of them and they just complicate stuff!”

If something is not useful, it wouldn't have been invented in science; this is particularly true for dimensional analysis which has made great success across all fields of science.

To put things simple, dimensional analysis has two major fundamental applications:

- Simplify equations and lead to new scientific branches/specialties.
- Guide scientific experiments with dynamic similitude.

<!--more-->

#### Simplification of the Navier-Stokes equation

Look at the Navier-Stokes equation

$$
\rho \left(\frac{\partial \mathbf{u}}{\partial t} + \mathbf{u}\cdot\nabla\mathbf{u}\right) = -\nabla p + \mu\Delta \mathbf{u} + \rho\mathbf{g}
$$

At a particular point in a flow, We may find that some term in this equation is *orders of magnitude* bigger than others. We could simplify the N-S equation by retaining those terms that matter, and eliminating those that don't.

How do we go about to eliminate the negligible terms? To put the conclusion first, the magnitudes of each term in the N-S equation depend on both the **sturcture** of the flow and **location** in the flow -- with appropriate flow structure and at appropriate location, one can safely delete certain terms in the N-S equation. This whole process of simplfying the equations, is called **dimensional analysis**.

#### Dimensional analysis

There are three steps in performing dimensional analysis.

1. Identify **characteristic scales** of a flow.
    - characteristic length $L$ is related to the size of the boundaries
    - characteristic velocity $U$ is determined by the particular mechanism driving the flow
    - characteristic time $T$ is either imposed by external means or simply defined as $T=L/U$.   
    
    > For example:
    > 
    > 1. In the case of unidirectional flow through channel: $U = $ max velocity across channel.
    > 2. In the case of uniform flow past stationary body: $U = $ velocity of the incident flow, $L =$ diameter of the body.
    > 3. In the case of forced oscillatory flow: $T = $ period of oscillation.

2. *Nondimensionalization*: 
    - Rescale each variable in the equation into a dimensionless variable. 
    $$\hat{\mathbf{u}}:=\frac{\mathbf{u}}{U},\qquad \hat{\mathbf{x}}:=\frac{\mathbf{x}}{L},\qquad \hat{t}:=\frac{t}{T},\qquad \hat{p}:=\frac{pL}{\mu U}.$$
    - Rewrite the equation into a dimensionless form.
    $$\beta \frac{\partial \hat{\mathbf{u}}}{\partial \hat{t}} + \mbox{Re}\,\hat{\mathbf{u}}\cdot\hat{\nabla}\hat{\mathbf{u}} = -\hat{\nabla} \hat{p} + \hat{\nabla}^2 \hat{\mathbf{u}} + \frac{\mbox{Re}}{\mbox{Fr}^2}\frac{\mathbf{g}}{g}$$
    - The multiplication factors of each term are nondimensional groups, called *dimensionless numbers*
        - Frequency parameter: $\beta:=\frac{L^2}{\nu T}$, expresses the relative magnitudes of the inertial acceleration force and the viscous force
        - Reynolds number: $\mbox{Re}:=\frac{UL}{\nu}$, expresses the relative magnitudes of the inertia convective force and the viscous force
        - Froude number: $\mbox{Fr}:=\frac{U}{\sqrt{gL}}$ expresses the relative magnitudes of the inertial convective force and the body force
        - The group $\frac{\mbox{Re}}{\mbox{Fr}^2}=\frac{gL^2}{\nu U}$, expresses the relative magnitudes of the body force and the viscous force

3. Eliminate the dominated terms.
    - If $\mbox{Re}\ll 1$ and $\beta\ll1$, the dominant terms give **Stokes equation**
    $$-\nabla p + \mu \nabla^2\mathbf{u}+ \rho\mathbf{g}=\mathbf{0}$$
    where the inertia terms go away, resulting in a quasi-steady fluid. 
    - If $\mbox{Re}\gg 1$ and $\beta\gg1$, and rescale the pressure by $\hat{p}=\frac{p}{\rho U^2}$ instead, the dominant terms give **Euler's equation**
    $$ \rho \left(\frac{\partial \mathbf{u}}{\partial t} + \mathbf{u}\cdot\nabla\mathbf{u}\right) = -\nabla p + \rho\mathbf{g} $$
    where the viscous term goes away, making it behave like an inviscid fluid.
    

#### Dynamic similitude

TBA.


##### Reference:

[Pozrikidis C. (2011). Introduction to Theoretical and Computational Fluid Dynamics (2nd ed.). Oxford University Press.](https://www.amazon.com/Introduction-Theoretical-Computational-Fluid-Dynamics/dp/0199752079)

