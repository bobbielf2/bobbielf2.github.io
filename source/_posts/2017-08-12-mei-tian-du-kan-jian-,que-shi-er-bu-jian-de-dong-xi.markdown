---
layout: post
title: "每天都看见，却视而不见的东西"
author: "波儿比 Bobbie"
date: 2017-08-12 17:10:51 -0400
comments: true
categories: thoughts
---

今天无聊去搜了一下这个世界上有多少美元在流通，网上的信息来源一般说有超过一兆美金（1 后面 12 个零）。于是又不禁想到，既然最大是这个数，那最小是美元单位是多少呢？

<!--more-->

之所以想到美元的问题，是因为今天玩编程的时候研究了一下 64 位的整数 Int64，看最大能表示多少位数字。Int64 是一种专门用来表示整数的数据类型，用到 64 位的 0 和 1 二进制数。因为有一位要表示正负号，剩下 63 位可以表示最大的数是 $2^{63}-1 \approx 9.22
\times10^{18}$，是一个 19 位的数字。

有趣的是维基百科里面有这个数字的页面，其中有一栏提到了这么一则新闻，说 PayPal 在 2013 年的时候曾经系统出错了一次，给一位客户的账户打了 “\$92 quadrillion（9.2 万兆美金）” 。这是一个 17 位数，加上小数点后 2 位，一共刚刚好 19 位，就是最大的 Int64 整数 —— 所以 PayPal 是以 Int64 数据型来记账的，这是一次数据溢出的操作。

我们看到用 Int64 来记账的话，如果小数点后留两位，整数位大约可以记到 9.2 万兆美元的级别，这比起现在全世界流通的 1 兆多的美元高了五个数量级，还是绰绰有余的。

进一步，这个故事告诉我们 PayPal 上的金额最小单位是 1 美分。所以美分就是最小的美元单位了吗？于是跑到美元的维基页面瞧了一下，发现并不是 1 美分。现行最小的美元单位是 1 mill （千分之一美金），小数点后三位。这并没有让我吃惊，我真正吃惊的是，里面有一段这样的说明：

{% blockquote Wikipedia https://en.wikipedia.org/wiki/United_States_dollar United States dollar %}
... “mill” is largely unknown to the general public, though mills are sometimes used in matters of tax levies, and gasoline prices are usually in the form of \$X.XX9 per gallon, e.g., \$3.599, more commonly written as \$3.59 ⁹⁄₁₀.
{% endblockquote %}


读到这里，我不禁惊叹：这个东西我每天都见到，只不过我又理所当然地把它忽略了。

这段话在说什么呢？说的是我们平时去加油站时看到的价格板，上面的价格都是精确到小数点后三位的，像是这样：

{% img /images/blog_figures/youjia.png 400 %}

有些天天见的东西，我们也都以为自己知道那是什么意思，直到疑问被提出来。几千年前，苏格拉底式的提问让当时的人开始审视自己的知识，发现自己以往认识的界限。今天我自己经历了一番这样的感受。

--

### 后记：

1) 如果保留数点后三位而不是两位，那 Int64 还是能表示到千兆美元的级别的，没有太大影响。而且既然 PayPal 只保留两位小数，我有理由相信金融行业实际操作都是用同样的数据贮存方式的。这样保持了业界金融软件的一致性，可以节省成本。而需要用到 mill 这个单位的少数行业，只需要额外记录一位数字就好了。

2) 视而不见（英文可以说 to look without seeing it 吗？）让我想起了那首 50 多年前的经典的歌曲：

{% blockquote Simon & Garfunkel, The Sound of Silence %}
People talking without speaking  
People hearing without listening  
People writing songs that voices never share  
And no one dared  
Disturb the sound of silence. 
{% endblockquote %}

其实这首歌在美国已俨然成为一个恶搞文化的符号了。当一个人在某个情境之下想起不堪回首的过去，陷入沉思与回忆，背景音乐就会响起：“Hello darkness my old friend ...” 。网上有大量恶搞视频，都挺搞笑的。

3) 写这篇文章的时候，需要把英文计数单位翻译成中文。比如 billion 翻成十亿，trillion 翻成一兆。在这个过程中，我发现“不可思议”竟然也是一个单位，一个不可思议等于 1 后面加 64 个零。这个单位的起源是一个佛教用语，形容神通很大的意思。真是够不可思议的！

{% img /images/blog_figures/bukesiyi.png 400 %}
