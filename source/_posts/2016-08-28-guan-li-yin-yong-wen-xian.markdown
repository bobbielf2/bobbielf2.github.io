---
layout: post
title: "管理引用文献"
subtitle: "文献管理软件 (Reference Management Software)"
author: "波儿比 Bobbie"
date: 2016-08-28 00:31:02 -0400
comments: true
categories: [Technology, LaTeX, Research]
---

管理文献对于做研究或者各种技术工程师都是很重要的事情。需要资料时要快速查得到，运用资料时要给出出处，这就要平时把文献资料整理得井井有条；尤其当文献数量达到上百甚至上千条，没有有效的管理方法简直寸步难行。

于是专业人员都会用到软件来管理文献。比如文章 [How to read a book](http://pne.people.si.umich.edu/PDF/howtoread.pdf) 就提到一些常用的文献管理软件(Reference Management Software)。

#### 市面上的文献管理软件

个人测试过以下这几个最流行的软件

- EndNote：据说挺好用，但是（1）需要花稍多一点的时间学习使用，（2）收费，差不多 80 大洋。网络 basic 版免费，但是试用了一下并不方便，也有导入数量限制。
- Papers：据说很好用，但是收费，学生版差不多 50 大洋。iPad 版免费，但是只用 iPad 版而没有桌面版也是很不方便。
- Bookends：优势是可以找 Amazon 上的书，不用费神想到底要连哪个出版商的数据库。
- Mendeley：暂时觉得最好用的一个。免费。可以把 PDF 文献原文拖入软件窗口，就会帮你自动识别 citation 信息，虽然并不总是准确，但如果知道 DOI 的话可以自动更正。在 mendeley 中可以连接到本地 PDF，并且直接打开做笔记挺方便。
- BibDesk：神器，免费，原生支持 [BibTeX](http://www.bibtex.org/) (BibTeX 是基于 [LaTeX](https://en.wikipedia.org/wiki/LaTeX) 的文献管理软件)。适合习惯用 LaTeX 写论文的人 (理工科写论文基本标配用 LaTeX )。就用它了！

> Remark: 如果不怎么用 LaTeX 写论文的话，Mendeley 就很好用。以前大部分人都用 Mendeley，现在很多科研人员不用的原因是因为“洁癖”： Mendeley 被 Elsevier (爱思唯尔出版社) 收购了，Elsevier 在学术界变得“臭名昭著”可以参考 [Wikipedia: The Cost of Knowledge](https://en.wikipedia.org/wiki/The_Cost_of_Knowledge)，中文参考 [科学网：逾万科学家联名抵制爱思唯尔](http://news.sciencenet.cn/htmlnews/2012/7/266578.shtm)。

<!--more-->

#### BibDesk

这里有一篇介绍 [为什么要用 BibDesk](http://www.mit.edu/people/lucylim/BibDesk.html) 的文章，作者是 NASA 的物理科学家 Lucy F. G. Lim。主要就是上面提到的三个优点：

- 可以做你想做的一切
- 原生支持 BibTeX
- 免费

在 BibDesk 新增文献引用信息的条目很简单：只要找到文章的 BibTeX 形式的引用信息，command-C 复制到剪贴版，然后在 BibDesk 窗口按 alt-command-L 就自动把剪贴版的信息生成新的条目了。

#### 两个很有用的在线数据库：ADS 和 arXiv

录入文献的引用信息，是整理文献的第一步，也是最机械最烦人的一步。如果有现成整理好的信息直接导入成 BibTeX 那该多好！幸好大家都是这么想的，you are not alone。早有牛人意识好这个需求，建立了收集文献信息的在线数据库，最著名的有 ADS 和 arXiv。配合 Google Scholar 的强大搜索功能，几乎所向披靡。

- [ADS (Astrophysics Data System)](http://adswww.harvard.edu/) 是由美国宇航局（NASA）开发、哈佛大学（Harvard）天体物理中心运营的在线数据库，上面保存了大量的 astronomy 和 physics 的科研论文。论文不一定是同行评审过的。论文的 abstract 和 citation 信息都完整可查，而且几乎所有文章原文都可以 GIF 或者 PDF 的形式获取。
- [arXiv.org](http://arxiv.org/) 是由物理学家 Paul Ginsparg 开发、现由康奈尔大学（Cornell）运营的在线数据库，保存科研论文的预印本（preprint），涉及的学科包括 mathematics, physics, astronomy, computer science, quantitative biology, statistics, quantitative finance。所有文章的原文都可以 PDF 形式获取，论文的 abstract 和 citation 信息都完整可查。
- [Google Scholar](https://scholar.google.com/) 可以搜索到包括上面提到的数据库在内的文献，而且自带把 Citation 输出成包括 BibTeX 在内的多种格式的功能。

> Remark: 另外也要善用学校图书馆。各个大学的图书馆都有统一订阅了主流出版社的在线数据库，学生可以免费获得大量文章和书籍。

#### 再安利一个软件：adsbibdesk 

这里再介绍多一种方式：用 [adsbibdesk](https://pypi.python.org/pypi/adsbibdesk) 软件导入 citation 到 BibDesk。顾名思义 adsbibdesk 可以把 ADS 或者 arXiv 上的数据自动整理导入到 BibDesk 中。

使用方法很简单，按照 [adsbibdesk](https://pypi.python.org/pypi/adsbibdesk) 主页指示安装好软件之后，就可以用 `adsbibdesk` 命令导入信息了。

导入时，在 BibDesk 打开想要修改的 .bib 文档，然后用 `adsbibdesk` 命令导入信息。用这个命令需要找到文章的 **ADS 识别码** (ADS bibcode)，在命令行运行

```batch
adsbibdesk 1998ApJ...500..525S
```

或者找到 **arXiv 识别码** （arXiv identifier），在命令行运行

```batch
adsbibdesk 1401.3068
```

或者找到 **DOI 码**（Digital Object Identifier），在命令行运行

```batch
adsbibdesk 10.1137/S0036144502417715
```

都可以把 citation 信息添加到 .bib 文档。

#### 后记

网上还有很多比较不同管理软件的文章，比如

- Wikipedia: [Comparison of reference management software](https://en.wikipedia.org/wiki/Comparison_of_reference_management_software)
- 密大图书馆 Research Guides: [Citation management software](http://guides.lib.umich.edu/citationmanagementoptions)
- 数据科学家 Max Masnick 的博客：
[Thoughts on Reference Management Software](https://www.maxmasnick.com/2015/02/28/reference-managers/)