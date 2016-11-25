---
layout: post
title: "不要计算"
subtitle: "-关于计算（Computation）的思考"
author: "波儿比 Bobbie"
date: 2016-08-17 13:01:14 -0400
comments: true
categories: [science, computation]
---


计算是一种需要被抵制的诱惑。有经验的人对于计算这个工具，都持谨慎的态度：

> A computation is a temptation that should be resisted as long as possible.  
> - John P. Boyd (Michigan)  


> Never do a calculation until you already know the answer.  
> - John Wheeler

更有甚者，以反讽态度强调理论之于计算的重要性。

>  Six months in the lab can save you a day in the library.  
> - Albert Migliori

<!--more-->

后人补充

> Six months in the lab will save you: Half a day in the library or 30 minutes searching online.  
> - Paul G. Kotula

好像大家都在贬低计算的作用，尽管我的爱豆 Trefethen 说过计算是一门伟大的科学：

> There are three great branches of science: theory, experiment, and computation.

传说中的 Knuth 也以计算作为验证科学的标准：

> Science is what we understand well enough to explain to a computer. Art is everything else we do.

正如所有科学家一样，大家都明白计算机是现代科学一个最最重要的发明。因为计算机导致计算能力的提升，我们可以用前所未有的方法去进行科学研究：计算卫星轨道，模拟湍流，模拟黑洞，挑战人类顶尖棋手。不敢想像没有发明计算机的世界会是怎么样的。如果说中世纪宗教统治的欧洲是“黑暗中世纪”，那以前没有计算机的所有时代就是“黑暗蜗牛时代”。

*既然计算这么好，为什么前辈们都在“贬低”计算呢？*

所有认真写过代码的人，无论是在学校学习的学生还是在业界工作的程序猿，都尝过 debug 的痛苦，著名的“九十-九十法则”说过：

> **Ninety-ninety rule**:
> The first 90% of the code takes 90% of the time. The remaining 10% takes the other 90% of the time.

代码纠错是任何项目中最最烦人的过程。而“贬低”计算的前辈们就是那些成功打败各种 bug 生存下来的佼佼者。说到底，他们强调了一件事：**理解**与**计算**的关系。

### 理解 — 计算

- 计算是用来验证你是不是理解一个概念或者方法的。如果你已经理解，计算的成功验证可以给你更多的信心；如果计算没有验证成功，你也找不出 bug 在哪里，那只说明一件事，你还没有完全理解。所以**理解是计算的前提**。
- 计算是运用理解力去实践创造的过程。理解一个理论之后，你就可以通过计算让理论在现实中派上用场。比如理解了建筑学和材料科学，就可以用模拟地震来研究建筑结构的薄弱部分；但是模拟出残垣断壁，并不能反过来让你自动学会材料科学。又比如理解了椭圆积分，就可以运用 AGM 算法来轻易算出 $\pi$ 到数亿位的精度；但是通过读 AGM 算法那几行简单的代码，并不能反过来告诉你它为什么这么有效，也不能教会你椭圆积分。**理解是计算的前提**。

> 附上计算 $\pi$ 的 AGM 算法，看看代码简单到什么程度，看看光看代码你能学会什么。

```matlab 
% MATLAB code: compute Pi via AGM
y = sqrt(sqrt(2));
x = (y+1/y)/2;
p = 2+sqrt(2);
for i = 1:6
    fprintf('%21.16g\n',p)
    p = p*(1+x)/(1+y);
    s = sqrt(x);
    y = (y*s+1/s)/(1+y);
    x = (s+1/s)/2;
end
```

所以，当你的程序有 bug 时，你应该做的不是死抠每一行代码，而是停止 debug，回去审视这些代码所基于的理论，让理论告诉你问题在哪里。这里再次引用那句话：

> Never do a calculation until you already know the answer.

真正的理解会告诉你答案，计算能做的只是验证和运用你的理解。

>  Things may seem magical, but to the people who understand math there is no magic. - Bobbie
