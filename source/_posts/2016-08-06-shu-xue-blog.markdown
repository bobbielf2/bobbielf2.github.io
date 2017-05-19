---
layout: post
title: "写数学 Blog"
subtitle: "如何让 Octopress 支持数学公式？"
author: "波儿比 Bobbie"
date: 2016-08-06 19:11:58 -0400
comments: true
categories: [Technology, LaTeX]
published: true
---

[上一篇文章](/blog/2016/08/06/yong-you-ni-de-ge-ren-bo-ke/index.html)讲了如何用 Octopress 在 GitHub 上搭建个人主页，今天这篇写给可爱的科研狗们，介绍怎么样让网页兼容 LaTeX！首先看看效果：

- LaTeX 行间模式（displayed math）

```latex latex
$$
\begin{align}
\mbox{欧拉公式：} & e^{i\pi} + 1 = 0\\
\mbox{牛顿公式：} & x_{i+1} = \frac{1}{2}\left(x_i+\frac{2}{x_i}\right)
\end{align}
$$
```
	
$$
\begin{align}
\mbox{欧拉公式：} & e^{i\pi} + 1 = 0\\
\mbox{牛顿公式：} & x_{i+1} = \frac{1}{2}\left(x_i+\frac{2}{x_i}\right)
\end{align}
$$

<!--more-->

- LaTeX 内嵌模式（inline math）

```latex latex
爱因斯坦说过：$E = mc^2$
```
	
爱因斯坦说过：$E = mc^2$

#### 让 Markdown 显示数学公式：kramdown 和 MathJax

##### 1, 用 kramdown 代替 rdiscount

Octopress 中默认的 rdiscount 不支持把 Markdown 中的 LaTeX 公式呈现出来，所以要换成 [kramdown](http://kramdown.gettalong.org/)（这个 Markdown 转换器也是开源的，他家号称全球最快）。

* 安装 kramdown（假设你已经有 rbenv，参考[上一篇文章](/blog/2016/08/06/yong-you-ni-de-ge-ren-bo-ke/index.html) ），运行命令

```bash
gem install kramdown
```

* 修改 Octopress 的`_config.yml`配置文件，把全部`rdiscount`都改成`kramdown`
* 修改 Octopress 的`Gemfile`，把里面的`gem 'rdiscount', '~> 2.0'`改成`gem 'kramdown'`

#### 2, 配置 MathJax

在`/source/_includes/custom/head.html`文件里添加

```html head.html
<!-- mathjax config similar to math.stackexchange -->
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  jax: ["input/TeX", "output/HTML-CSS"],
  tex2jax: {
    inlineMath: [ ['$', '$'] ],
    displayMath: [ ['$$', '$$']],
    processEscapes: true,
    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
  },
  messageStyle: "none",
  "HTML-CSS": { preferredFont: "TeX", availableFonts: ["STIX","TeX"] }
});
</script>
<script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML" type="text/javascript"></script>
```

**2017/5/19 update:** MathJax 最近[更改了他们 CDN 的提供商](https://www.mathjax.org/cdn-shutting-down/),所以上面这个 script 里最后一行的 cdn 地址很快就会不适用了，新的地址变成下面这个（注：我还把`http`改为`https`，保证在安全模式下看到数学公式）：

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML" type="text/javascript"></script>
```

#### 3, 修复 MathJax 在页面中右键变白屏的 bug

修改 Octopress 的`/sass/base/_theme.scss`文件，把代码中的

```sass _theme.scss
//...
> div {
     background: $sidebar-bg $noise-bg;
     border-bottom: 1px solid $page-border-bottom;
     > div {
//...
```

加入`#main`，变成

```sass sass
//...
> div#main {
     background: $sidebar-bg $noise-bg;
     border-bottom: 1px solid $page-border-bottom;
     > div {
//...
```

#### 4, 修复 Pygments 的问题

这个是新版本出现的问题。使用 kramdown 之后，以前写的博客突然编译不出来了；当你运行 rake generate 时候，会报错：

```
Error: Pygments can't parse unknown language: </p>
```

原因是最新版的 Pygments 这个插件对于 Markdown 的书写要求更严格了。

为了找出原来，可以修改 Pygments 的报错代码，在`/plugins/pygments_code.rb`文件中:

```ruby pygments_code.rb
def self.pygments(code, lang)
    if defined?(PYGMENTS_CACHE_DIR)
      path = File.join(PYGMENTS_CACHE_DIR, "#{lang}-#{Digest::MD5.hexdigest(code)}.html")
      if File.exist?(path)
        highlighted_code = File.read(path)
      else
        begin
          highlighted_code = Pygments.highlight(code, :lexer => lang, :formatter => 'html', :options => {:encoding => 'utf-8', :startinline => true})
        rescue MentosError
          raise "Pygments can't parse unknown language: #{lang}."
        end
        File.open(path, 'w') {|f| f.print(highlighted_code) }
      end
```

把这里的

```ruby
raise "Pygments can't parse unknown language: #{lang}."
```

修改成

```ruby
raise "Pygments can't parse unknown language: #{lang}#{code}."
```

可以使得`rake generate`编译时，把有问题的部分抛出来。

通过这个方法，我最终确定了我这里的情况是，用来标记 code block 的```` ``` ````符号和段落符号`</p>`放在一起时产生某种错误（反正我是试不出怎么回事）。最后我用`~~~`代替了```` ``` ````（同样是 Markdown 标记代码的符号），终于没有编译错误了。

**2017/1/12 update:** 更新到 python 3 之后，pygments 又出错了，不能 parse language。原因就是因为 pygments 只支持 python 2。**解决方法：** 用 anaconda 建立一个 python 2 的 environment:

``` bash 
conda create -n py27 python=2.7 anaconda
```

安装好 python 2.7 后，激活这个 environment:

``` bash 
source activate py27
```

这样就能正常编译了。


#### 后记

写这篇文章的时候，遇到一个问题，就是不知道怎么让 Markdown 显示 `` ` ``这个符号，后来发现了解决方法：

显示一个撇`` ` ``，可以用两个撇来包裹

~~~
`` ` ``(两撇，空格，一撇，空格，两撇)  
~~~

显示两个撇``` `` ```，可以用三个撇来包裹

~~~
``` `` ```(三撇，空格，两撇，空格，三撇)
~~~

以此类推。

#### 参考：

构建：[Octopress中使用Latex写数学公式](http://dreamrunner.org/blog/2014/03/09/octopresszhong-shi-yong-latexxie-shu-xue-gong-shi/)  
修复：[配置Octopress支持LaTex数学公式](http://lvraikkonen.github.io/blog/2015/08/08/adding-support-for-math-formula/)