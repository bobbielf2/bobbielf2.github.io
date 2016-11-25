---
layout: post
title: "拥有你的个人博客"
subtitle: "基于 GitHub 和 Octopress 和 Mac OS X 10.11"
author: "波儿比 Bobbie"
date: 2016-08-06 15:57:31 -0400
comments: true
categories: technology
published: false
---


每个人或多或少，某时某地，都想表达自己，最有收益的表达方法莫过于写 Blog！

搭建个人博客一直是我想做的事。之前试过在不同的地方栖息，包括 QQ 空间和 [weebly](bobbielf2.weebly.com/index.html)，写的都是纯文字。后来想写带数学公式的文章，发觉只能把公式制作成图片插入文章，极其麻烦。然后我的好基友 Kuphrer 对我说：“没有原生latex不博客啊！”于是在他的指导下搭了一个 WordPress，又要另外弄存储空间又要备份什么的，弄得我这个网络小白晕头转向，终于还是没有坚持下去。

斗转星移，technology 一日千里，最近学习和编程的需要让我开始了解GitHub，发现这是一个大牛云集的宝地，而且只要项目是开源的就可以免费任意上传文件，而且没有广告，没有任何限制，简直就是搭建个人 Blog 的理想国。在网上搜了一下教程之后，我的博客搭建之旅开始了！

<!--more-->

### 一、 预备知识

#### 什么是 GitHub？

Git 和 GitHub 并不是同一个东西。Git 是一个版本控制软件，而 GitHub 是一个公司，他家提供基于 git 的版本托管服务。因为 GitHub 上的开源项目的托管是**免费的**，全球最著名的开源社区和大公司的程序猿都聚集在这里。比如大公司都包括：

- [Google](https://github.com/google)
- [Apple](https://github.com/apple)
- [Facebook](https://github.com/facebook)
- [Twitter](https://github.com/twitter)
- [Microsoft](https://github.com/microsoft)
- [阿里巴巴](https://github.com/alibaba)
- ...

开源项目包括

- [Linux](https://github.com/torvalds/linux)
- [Swift](https://github.com/apple/swift)
- [Ruby](https://github.com/ruby/ruby)
- ...

#### 什么是 Octopress

Octopress 是一个基于 **Jekyll** 的*静态博客架构*（static blogging framework）。换句话说就是有个人使用 Jekyll 这个东西建了一个叫做 Octopress 的博客模版，我们可以修改它来建自己的博客，免去很多从头建设的技术上的麻烦。那 Jekyll 又是什么东东？

Jekyll 是一个对写作者友好的*网页模版系统*（web template system），能够处理文本文档生成*静态网站*（static site, 访问速度远远快于动态网站，因为动态网站是每次访问都重新生成的）。按它开发者的话来说，Jekyll 具有 “blog-aware（博客意识）” 的特点，意思是说它是为博客而生的，写作者用它来发布文章时，只需要处理好文字，而不用费神去处理数据库和网页内容管理之类的技术问题。当然，“好用”是基于不同人的体验的，对于我这种技术小白来说，学会 Jekyll 还是有点麻烦的，所以才要用 Octopress 这个现成模版。

> Remark: Jekyll 是用 [Ruby 编程语言](<https://en.wikipedia.org/wiki/Ruby_(programming_language)>)写出来的软件。
> <br />
> 所有用 Ruby 写出来的软件都是用 [RubyGems](https://en.wikipedia.org/wiki/RubyGems) 这个*软件包管理系统*（package manager）分发安装的。在 RubyGems 中，一个封装好的软件叫 Gem。RubyGems 的命令一般是用 `gem` 开头的。当需要安装不止一个软件甚至一些第三方软件包的时候，可以用 Bundler（另一个 Ruby 软件）来批量处理，命令以 `bundle` 开头，被执行的命令写在一个 Gemfile 里面。
> <br />
> Ruby 和其他编程语言一样可以执行脚本，叫做 Rakefile（类似 C 语言里面的 Makefile），方便编译运行 Ruby 程序。Rakefile 用 `rake` 执行（类似 Makefile 用 `make` 执行）。
> <br />
> 综上所述，等下安装 Jekyll 和 Octopress 时首先要安装 Ruby， RubyGems 和 Bundler。

### 二、 安装博客的流程

#### 1. 安装 Git 和 Ruby (以及 RubyGems)

如果用 Mac 的话有自带的 Git 和 Ruby 2.0，不需要安装。需要的话 git 可以从[这里](http://git-scm.com/downloads)下载和安装。用 `ruby -v` 可以查询当前 Ruby 版本。新版的 Ruby 自带 RubyGems，所以也不用特别安装，如果没有的话可以在[这里](https://rubygems.org/)安装。

#### 2. 安装 Jekyll 和 Bundler

一般在 Mac 上，可以运行以下命令

```bash
$ gem install jekyll
$ gem install bundler
```

但是！更新到 Mac OS X 10.11 (El Capitan) 之后, 系统安全系数升级导致你不能直接更改 `/Library/Ruby/Gems/` 里面的东西（用 `sudo` 也不行！）于是只好更改安装目录，到 `/usr/local/bin` 上，命令变成：
	
```bash
$ gem install -n /usr/local/bin jekyll
$ gem install -n /usr/local/bin bundler
```

#### 3. 安装 Octopress

用 Rake（也就是 Ruby 的 Make）来安装 Octopress。再次，本来在以前的 Mac OS 可以直接这样安装：

```bash
$ bundle install
$ rake install
```

然而！刚才说过新的系统不能改 `/Library/Ruby/Gems/`，于是只好 bundle 到别的目录了
	
```bash
$ bundle install --path vendor/bundle
```
然后由于 bundle 改了目录，想用 rake 命令也只能增加额外的指令，变成 `bundle exec rake`，让系统找到位置：
	
```bash
$ bundle exec rake install
```

> Remark: 后面我都会用 `bundle exec rake`。如果你没有更新到最新的 OS X 10.11，仍然有权限改系统的 Ruby 目录的话，可以省些事用回 `rake`。

	
#### 4. 关联 GitHub

终于！到了建立 Octopress 的时候了。 首先为你的网站文档新建一个文件夹，假设是 `/Users/YOURNAME/Sites`，然后把 Octopress 的文档载到里面，放在比如说 `mysite` 文件夹：

```bash
$ cd ~/Sites
$ git clone git://github.com/imathis/octopress.git mysite
$ cd mysite
```

接着去 [GitHub](https://github.com/new) 建一个新的 repository，名字要起成这样 `USERNAME.github.io`，比如我的就是 `bobbielf2.github.io`。然后用以下命令来建立 Octopress 和 GitHub 的连接：

```bash
$ bundle exec rake setup_github_pages
```

执行这个命令，会让你输入 Repository url，把刚在 GitHub 建的 repository 地址输进去就好了，以下两种格式任选一个都可以

```
$ https://github.com/USERNAME/USERNAME.github.io #格式1  
$ git@github.com:USERNAME/USERNAME.github.io.git #格式2  
```

例如我就输入  

```
$ https://github.com/bobbielf2/bobbielf2.github.io  
```

接着按照提示输入密码之类的，就完成和 GitHub 的关联了。

#### 5. 生成和部署博客网站

连接完成之后，继续可以生成和部署网站：

```bash
$ bundle exec rake generate
$ bundle exec rake deploy
```

把文件同步 push 到 GitHub 上
	
```bash
$ git add .
$ git commit -m 'create blog'
$ git push origin source
```

现在可以去你的 GitHub 网址看自己的网页了，比如我的就是 [https://bobbielf2.github.io/](https://bobbielf2.github.io/)。
	
接着可以修改网页配置，位置在 `mysite/_config.yml`。
	
```yaml
url:                # For rewriting urls for RSS, etc
title:              # Used in the header and title tags
subtitle:           # A description used in the header
author:             # Your name, for RSS, Copyright, Metadata
simple_search:      # Search engine for simple site search
description:        # A default meta description for your site
date_format:        # Format dates using Ruby's date strftime syntax
subscribe_rss:      # Url for your blog's feed, defauts to /atom.xml
subscribe_email:    # Url to subscribe by email (service required)
category_feeds:     # Enable per category RSS feeds (defaults to false in 2.1)
email:              # Email address for the RSS feed if you want it.
```

编辑完成后再 push 更新一次

```bash
bundle exec rake generate

git add .
git commit -m "settings" 
git push origin source
	
bundle exec rake deploy
```

> Remark: 每次 commit 来确认改变之前，都要 add 来更新索引。最终 push 来把所有变化应用到当前的 branch 中。所以 commit 之前可以 add 很多次，push 之前也可以 commit 很多次。 


### 三、 写博客

终于！搭建好博客，就可以开始写文章了！GitHub 上的文章严重推荐用 [Markdown](https://en.wikipedia.org/wiki/Markdown) 写。

> 题外话：Markdown 是当今很多网络写作者和程序员最爱用的格式。这种语言就一个字：简单！纯文本编辑，用简单的额外符号设置文字格式，没有像 MS Word 或者 Apple Pages 那样，不同版本不同平台就打不开文档的问题；然而又基本没什么学习成本，就能写出漂亮的排版。推荐看这个速成：
> <br />
> [献给写作者的 Markdown 新手指南](http://www.jianshu.com/p/q81RER)。

#### 1. 创建新的文章

用这个命令生成新的 Blog artcle 
  
```bash
bundle exec rake new_post['title']
``` 
  
生成的 Markdown 文件在 `mysite/source/_posts` 目录下

#### 2. 编辑文章

用 Markdown 语言写好文章，保存后可以预览： `bundle exec rake preview `，然后发布：

```
bundle exec rake generate
```

```
git add .
git commit -m "new post"
git push origin source
```

```
bundle exec rake deploy
```

### 四、 使用不同的主题。

网上有很多人制作不同的网页主题（theme）。举例安装第三方主题：
	
```
#这里以安装allenhsu定制的greyshade主题为例，原作者是shashankmehta
git clone git@github.com:allenhsu/greyshade.git .themes/greyshade
```
```
#Substitue 'color' with your highlight color
echo "\$greyshade: color;" >> sass/custom/_colors.scss 
```
```
bundle exec rake "install[greyshade]"
bundle exec rake generate
```
```
git add .
git commit -m "theme" 
git push origin source
```
```
bundle exec rake deploy
```
 
安装完 greyshade，你会发现左方导航栏上的 About me 是指向原作者的主页的，可以这样改回来：在 `/source/_includes/custom/navigation.html` 中记录了导航栏的内容

```html
<li><a href="/">Blog</a></li>
<li><a href="http://about.me/shashankmehta">About</a></li>
<li><a href="/blog/archives">Archives</a></li>
```  

把里面的网址 `http://about.me/shashankmehta` 改成别的东西就好了。


#### 后续参考：

[设置头像，文章以摘要形式显示，评论功能](http://zwgithub.github.io/2016/06/14/%E7%94%A8Octopress%E6%90%AD%E5%BB%BA%E5%B1%9E%E4%BA%8E%E8%87%AA%E5%B7%B1%E7%9A%84github%E5%8D%9A%E5%AE%A2/)

[生命之氢 - Octopress 教程目录](https://shengmingzhiqing.com/blog/octopress-tutorials-toc.html/)  
