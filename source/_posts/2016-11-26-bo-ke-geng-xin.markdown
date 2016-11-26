---
layout: post
title: "博客更新"
subtitle: "中途出家的码农之挣扎系列（一）"
date: 2016-11-26 15:24:57 -0500
comments: true
categories: [science, computation]
---

我对最开始的两编博客内容进行了更新。因为经过这段时间的学习，我的电脑水平有所增长，回头看当时写的东西不禁发现了各种不严谨和各种 bug，忍不修补了一下。

好了，本篇的主要内容完毕，以下完全是跑题的内容，是我对这个学期所学的一门课的吐嘈，可以随意忽略。。

<!--more-->

最近在忙学业。这个学期选修了一门 Scientific Computing 的课（简称 SC 课），是 [MICDE](http://micde.umich.edu/) 开的第一门课。对于一个编程一直只用 Matlab，没有开发经验，不怎么 geek 的伪码农，我表示这门课又让我体验了一次被虐的快感。所以我决定小小吐嘈一下，就以“中途出家的码农之挣扎系列”为副标题，以后说不定这个系列还会更新。

吐嘈开始，首先看看这门课的大纲：

| Week |                            Topic                            |
|------|:-----------------------------------------------------------:|
| 1    | Introduction to Linux                                       |
| 2    | Programming Langues: C, C++, Fortran                        |
|      | Linux Bash Scripting & Introduction to Python               |
| 3    | Elements of Development: Configuring, Compiling, Linking    |
|      | Tools of the Trade: Version Control, Text Editors, Dev. Env |
| 4    | Algorithms for Numerical Linear Algebra                     |
|      | Sci. Computing Libs: BLAS, LAPACK, PETSc, Trilinos          |
| 5    | Software Engineering Practices & Development Workflows      |
|      | Object-Oriented Programming, Design Patterns, UML           |
| ...  | ...                                                         |
| 8    | Serial Optimization Techniques                              |
|      | Parallel Programming Models                                 |
| ...  | ...                                                         |
| 11   | Data Format Libraries: HDF5, NetCDF, SILO                   |
|      | Mesh Libraries: Libmesh, Exodus, others                     |
| ...  | ...                                                         |

可以看出主题非常广泛，包括操作系统，各种语言编程，开发过程，版本控制，文本处理，数值算法，计算机工程，并行运算，数据存贮和可视化，等等。基本上每周的 topic 都足以开一门一整个学期的课，我们的任务就是尽力掌握那一周的内容，达到基础程度的理解，并且能够在上机实验环节实行简单应用。

于是每个星期对于我们来说都像一场生死循环：在课堂上尽全力去理解，然后在上机实验的时候费尽九牛二虎之力完成任务，刚觉得这周的 topic 总算是入门了，又尼玛进入下一周的主题，重新开始轮回。

但是当你尽力从这门课里活下来了，你所看到的世界都不一样了，在科学计算的方方面面都已经有所涉足，对于这个信息时代的齿轮如何运作有了全新的深度和广度的理解。当然我还远远不是任何一方面的 expert，精确的说，现在的我对科学计算这门学问有了一个比以前更清晰的整体图像（big picture），就像下面这张图所展示的第二种（progressive）进程，对整个学科有了从低像素到高像素的改善。

{% img /images/blog_figures/baseline_vs_progressive.jpg 500 %}

### 万金油技能总结

Scientific Computing 的根本目标就是通过科学方法论、高效的协作来促进科学计算的理论和技术的发展。在接触这些方法论的过程中，我觉得有一些技能是在任何地方都十分宝贵的，不局限于 SC。

1. **[RTFM](https://en.wikipedia.org/wiki/RTFM) 的能力**。在任何时候，懂得读 manual 和 documentation，都让你有了解决所有问题的利器。
2. **运用 feedback 的能力**。无论是编程 debug，还是学习别的技能，本质都是针对薄弱环节的刻意练习（deliberate practice）。刻意练习需要不断的接受 feedback 再次练习，feedback 的来源可以是程序的 compiler，老师，同学，网上练习系统等等。有效运用 feedback 本质上也是一种理解能力（动态的 RTFM）。
3. **搜索（STFW）的能力**。这个能力一说起来好像很简单，搜索谁不会嘛！但其实搜索能力是有不同级别，人人都能搜索，但是有的人是专家，有的人搜一下搜不到就放弃了。搜索能力本质上是*把碎片信息整理成系统信息的能力*。“搜”只是第一步，后续的整理信息，再搜索，再整理，再搜索……就是搜索能力的差别所在。
4. **从“术”到“道”的能力**。换个说法，就是从技术到理论，从 how 到 why，从方法到哲学，从科学到艺术的升华能力。说到底，知识是人的知识，人有强大的逻辑思维能力，但还有感情的影响和追求目标的动力。把知识学会，只需要有思维能力理解能力；把知识推向极致，运用到造福社会的程度，则需要理论和哲学的支持，需要做一件事情的意义和审美，需要影响其他人和接受他人的帮助，这些都是经过耐心的思考、实践、积累才能得到的。

回想起来，我对付 SC 课和完成一切其他任务所用到的不外乎就是这几种技能了。