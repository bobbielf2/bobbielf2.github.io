---
layout: post
title: "Remote Access to Linux-based Computing Resources with Graphical Interface (for UM students)"
author: "波儿比 Bobbie"
date: 2017-09-07 15:25:54 -0400
comments: true
categories: technology
---

> Note: this note is about University of Michigan computing resources.

People working on numerical analysis often need to develop efficient code by doing multi-language programming, e.g. MATLAB/C++ or MATLAB/Fortran. Linux operating system is needed to have the best programming experience. (Mac OS has all sorts of compatibility issues.) For UM people who are using a Mac, I have explore the following four options for remotely accessing Linux-based computing resources.

<!--more-->

### 1. Use the ITS Statistics and Computation Service (SCS)

The [ITS SCS](http://www.itcs.umich.edu/scs/) provides the easiest way to certain computational resources, no extra permissions/purchases needed. But the software may not be up-to-date, e.g. MATLAB version on this server is relatively old (MATLAB R2012b).

Steps:

1. Install [XQuartz](https://www.xquartz.org/) on your Mac (See [info](http://www.itcs.umich.edu/scs/x11.php))
2. Connect to server by typing `ssh -Y uniqname@scs.dsc.umich.edu` in terminal.
3. Upon successful connection, type `matlab` to run the program. XQuartz graphics will be invoked.


### 2. Ask LSA-IT for help

For math people, we can contact the East Hall Technical Service (EHTS) for help. They offer newer software. (The EHTS is one of the four regional support desks of the [LSA-IT](https://lsa.umich.edu/lsait)). 

Steps:

1. Install [XQuartz](https://www.xquartz.org/) on your Mac.
2. Ask EHTS techicians (Room 1069EH) to grant you access to a Linux machine. 
3. Download the [X2Go Client](https://wiki.x2go.org/doku.php/download:start).
4. Configure X2Go Client to connect to the `vulpix.math.lsa.umich.edu` server.

### 3. Use the CAEN computers

The UM Computer-Aided Engineering Network (CAEN) provides the smoothest experience for general users as well as power users. The CAEN computer operates the newest Linux and Windows systems, with newest and most complete software libraries for all sorts of computational work. **But these are only conveniently available to engineering students.**

Availability:

* If you are an engineering student, or are currently taking engineering classes, then you can [access CAEN computing resources anywhere](https://caen.engin.umich.edu/accounts/), on-site or remotely.
* All other non-engineering students have NO remote access to CAEN computers, and can only go to north campus to use the CAEN computers in the Duderstadt Center.

Steps:

1. See CAEN [Linux Login Service](https://caen.engin.umich.edu/connect/linux-login-service/)

### 4. Use the Flux HPC Cluster

This option builds connections using [VNC](https://en.wikipedia.org/wiki/Virtual_Network_Computing) (instead of XQuartz) is faster and more stable, can disconnect and **resume** right where you left at any time.

Info about Flux:

* The [ARC-TS](http://arc-ts.umich.edu/)'s Flux HPC Cluster provides high performance computing service and has its own professional technical help.
* LSA people can use the [public LSA allocations](http://arc-ts.umich.edu/document/lsas-public-flux-allocation/) on Flux. These allocations are free, but take longer for jobs to start.
* If you or your advisor has purchased [private allocation](http://arc-ts.umich.edu/flux/managing-a-flux-project/) on Flux, then there is much [less wait or limitations](http://arc-ts.umich.edu/document/lsas-public-flux-allocation/).


Steps:

1. [Obtain access to Flux](http://arc-ts.umich.edu/flux-user-guide/)
2. Follow instructions [here](http://arc-ts.umich.edu/flux/vnc/) to configure a VNC server, and use a VNC client to connect.
3. Follow instructions [here](http://arc-ts.umich.edu/flux-user-guide/#document-14) to load and use softwares on Flux.


### Summary

* If eligible for a CAEN account, always use CAEN
* For general use and easy access, ask LSA-IT for help
* For serious programming, use Flux HPC Cluster
* For not-so-serious purpose, use the ITS SCS
