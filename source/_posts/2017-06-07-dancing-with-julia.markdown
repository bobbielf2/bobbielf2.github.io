---
layout: post
title: "Dancing With Julia"
subtitle: "a powerful new language for scientific computing"
author: "波儿比 Bobbie"
date: 2017-06-07 16:39:19 -0400
comments: true
categories: [Computation, Technology]
---

I have been having fun with [the Julia language][julia] lately. It is a new programming language for scientific computing. You may wonder, why do we need a new language at all? Don't we already have MATLAB, Mathematica, Python with NumPy and SciPy, etc., are't those enough?

Well, it is true that those are awesome softwares for scientific computing, they have all the necessary functionalities and powerful libraries, and they are easy to learn. But there is a common (fatal) issue that prevents them from creating industrial quality codes -- speed. We want faster speed! The Julia language is developed specifically for this.

[julia]: https://julialang.org/

<!--more-->

## 1. The Julia Language

What is the Julia language? According to its [official page][julia]

> Julia a high-level, high-performance dynamic programming language for numerical computing.

There are two keywords here: **high-performance** and **dynamic programming**. These two words don't usually come together! If you have written some program for numerical computations, you probably have noticed:

* **Dynamic programming** languages like Python and MATLAB are very handy and human-friendly. Each such language has a [REPL] that allows you to see the effects of your code immediately, so the workflow is interactive. You can easily explore ideas, quickly prototype a new software. The syntax is simple which allows for fast development.
* However, when you finally decide to write some software for practical use, all these dynamic programming languages suffer from slow running speeds. Then you have to switch to a **high-performance** programming language like C/C++ and Fortran. These languages are static, use a classic edit-compile-run-debug (ECRD) cycle in contrast to REPL. It takes a lot of time to write the code and debug.

[REPL]: https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop

This is called the **Two-language problem**: efficiency for human or efiiciency for the machine, pick one. There have been efforts trying to resolve this problem, for example, by linking the C libraries in a Python code, but such usage of multi-language programming quickly makes the code really complex and hard to maintain.

### 1.1 Solving the two-language problem

This is exactly where Julia kicks in.

Julia is a dynamic programming language as MATLAB or Python, making it easy to use. But Julia also runs [very fast][bench], comparable to the performance of C codes. How could a dynamic language run fast? It does so by using the [LLVM]-based [just-in-time][jit] (JIT) compiler. In fact Julia is designed for JIT from the very beginning!

[bench]: https://julialang.org/benchmarks/
[LLVM]: https://en.wikipedia.org/wiki/LLVM
[jit]: https://en.wikipedia.org/wiki/Just-in-time_compilation

### 1.2 Want to try Julia?

If you would like to try out the Julia language, I recommend this quick hands-on approach: firstly, you learn the basics by going through some short tutorial found [here][tutorial]; after having some familiarity with the syntax, you start some programming with your field of study with the help of some [existing packages][packages]. For example, I work on numerical analysis and spectral methods, so I started with the [ApproxFun] package under the [JuliaApproximation] project; or if you have done some statistics programming with languages like R, there is a collection of statistics packages under the [Julia Statistics] project; or if you are an algebraist, you may have done some symbolic programming with languages like REDUCE, there is also a [Reduce] package for you. Check the [list of available packages][packages], no matter what you work on, you are likely to find something that suits your need.

[tutorial]: https://julialang.org/learning/#tutorials
[packages]: http://pkg.julialang.org/
[ApproxFun]: https://github.com/JuliaApproximation/ApproxFun.jl
[JuliaApproximation]: https://github.com/JuliaApproximation
[Julia Statistics]: https://github.com/JuliaStats
[Reduce]: https://github.com/chakravala/Reduce.jl

Next, I am going to talk about an experience I had when coding Julia. It will be an example with very technical details, so you may stop reading at this point if all you want is just some general information about Julia.

## 2. Testing my code: why can't I redefine my test functions?

(**Note:** the issue mentioned in this note pertains to julia version `v0.5`, there will be a change/fix of the behavior in `v0.6`; see the P.S. in the end.)

### 2.1 Redefine test functions that will be called by a high-order function: the failure

In scientific computing, we often need to test a function by feeding it different parameters to see if the behaviors are as expected.

``` julia
julia> function myFun1(value)
           return value + 1
       end

julia> v = 1; myFun1(v)    #test case 1
2

julia> v = pi; myFun1(v)    #test case 2
4.141592653589793

julia> v = -e; myFun1(v)    #test case 3
-1.718281828459045
```

This is completely fine with a simple function. But if you are debugging a **high-order function**, i.e. a function whose input (or output) is also a function:

{% codeblock lang:julia %}
julia> function myFun2(f)
           return f(2)
       end

julia> f(x) = x; myFun2(f)    #test case 1
2

julia> f(x) = x^2; myFun2(f)    #test case 2
WARNING: Method definition f(Any) in module Main at REPL[2]:1 overwritten at REPL[3]:1.
2

julia> f(x) = exp(x); myFun2(f)    #test case 3
WARNING: Method definition f(Any) in module Main at REPL[3]:1 overwritten at REPL[4]:1.
2

julia> println([f(2), myFun2(f)])
[7.38906,2.0] #both should have returned the same value f(2)!
{% endcodeblock %}

We see that redefining a function is okay if you just want to evaluate it, but redefining for the testing of another high-order function won't work. Unless you also **redefine that high-order function to update the dependence**:

{% codeblock lang:julia %}
julia> function myFun2(f)
           return f(2)
       end
WARNING: Method definition myFun2(Any) in module Main at REPL[1]:2 overwritten at REPL[11]:2.
myFun2 (generic function with 1 method)

julia> myFun2(f)
7.38905609893065
{% endcodeblock %}

But redefining every high-order function is cumbersome, and even impractical if there is a chain of dependencies among multiple high-order functions.

### 2.2 The logic behind such failure: how the JIT compiler works

This issue received a long discussion (started a couple years ago and is still going on) on GitHub [issue #265](https://github.com/JuliaLang/julia/issues/265). This goes back to the fundamental question of how Julia's JIT compiler works (under the hood) in real time. 

* The JIT compiler would compile a custom function (high-order or not) when it is executed for the first time. So you see behavior like this

{% codeblock lang:julia %}
julia> function f1()
           2;
       end
f1 (generic function with 1 method)
    
julia> function f2(f)
           f()
       end
f2 (generic function with 1 method)
    
julia> function f1()
           3;
       end
WARNING: Method definition f1() in module Main at REPL[1]:2 overwritten at REPL[3]:2.
f1 (generic function with 1 method)
    
julia> f2(f1)
3
{% endcodeblock %}

* Because `f2` is compiled when `f2(f1)` is called; before the call, `f1` is most recently defined to return `3`, so `f2(f1)` returns `3`; the first definition of `f1` that returned `2` was overwritten. 

* After the `f2(f1)` call, no matter how you overwrite the definition of `f1`, `f2(f1)` will always return `3` since that's how it was when compiled at its first call. 
  
{% codeblock lang:julia %}
julia> function f1()
           2;
       end
WARNING: Method definition f1() in module Main at REPL[3]:2 overwritten at REPL[5]:2.
f1 (generic function with 1 method)
  
julia> f2(f1)
3
{% endcodeblock %}
  
* Unless you also redefine `f2`, then `f2` becomes an uncompiled function again. The next time `f2` is called, it will be compiled again and updates its behavior.
  
{% codeblock lang:julia %}
julia> function f2(f)
           f()
       end
WARNING: Method definition f2(Any) in module Main at REPL[2]:2 overwritten at REPL[7]:2.
f2 (generic function with 1 method)
    
julia> f2(f1)
2
{% endcodeblock %}

* This experiment shows that the compilation is down to the lowest-order function, so if a high-order function is called, the JIT will compile all the functions it calls, until it hits a simple function. (Compilation can also occur when you feed a custom function with variables of different types. This is the subject of **multiple dispatch**, another great advantage of Julia).

### 2.3 Solution: using anonymous functions

I have found a solution in [a comment of issue #508](https://github.com/JuliaPlots/Plots.jl/issues/508#issuecomment-250200614), which is to use the lambda function notation `->` in Julia to define an anonymous function, and assign the anonymous function to a variable `f`. Then feed this variable into the high-order function you want to test.

{% codeblock lang:julia %}
julia> function myFun2(f)
           return f(2)
       end
myFun2 (generic function with 1 method)

julia> f = x -> x; myFun2(f)
2

julia> f = x -> x^2; myFun2(f)
4

julia> f = x -> exp(x); myFun2(f)
7.38905609893065
{% endcodeblock %}

All works well now! This is because the variable `f` is now pointing to an anonymous function. If it is later redefined to point to a different function, this pointer value is updated because every anonymous function receives a unique label. So there are no more confusions!

### P.S. Issue fixed in `v0.6`

I have downloaded the pre-released version `julia v0.6.0-rc2` to check if the issue is well handled. Apparently, the issue is well fixed in this new version:

{% codeblock lang:julia %}
julia> function myFun2(f)
           return f(2)
       end
myFun2 (generic function with 1 method)

julia> f(x) = x; myFun2(f)
2

julia> f(x) = x^2; myFun2(f)
4

julia> f(x) = exp(x); myFun2(f)
7.38905609893065
{% endcodeblock %}

