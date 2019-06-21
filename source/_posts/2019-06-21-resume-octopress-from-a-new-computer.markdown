---
layout: post
title: "Resume Octopress blogging from a new computer"
author: "波儿比 Bobbie"
date: 2019-06-21 12:02:54 -0400
comments: true
categories: Technology
---

I recently switched to a new computer. The switch isn't too messy because I basically have all my data backed up, either on Google Drive or on GitHub.

One thing I wanted to make sure is that I can still update this blog, which is hosted using Octopress. But to be honest, until recently I am not really good at using git and GitHub, so it took me some time to figure out what I need to do to resume blogging with Octopress.

<!--more-->

Logically, the key concept with Octopress is that it uses a *ghost branch*. All the source files for my blog is tracked NOT by the master branch, but by a ghost branch (named "source" under the Octopress framework) that is completely unrelated to the master branch in terms of git history -- it's a hanging branch that lives in a parallel world albeit in the same repo, hence the name "ghost branch."

Another important thing with Octopress is to find out how the local blog is deployed onto [GitHub Pages](https://pages.github.com/). This also took me a little bit to figure out. It turns out that my blog is first generated under a `_deploy`  folder, and then that folder is synced to the master branch on the repo.

Summarizing the two paragraphs above, Octopress is organizing my blog in the following way:

```
MyBlog
|--source files (tracked by ghost branch)
|--_deploy
   |--github page files (tracked by master branch)
```



Apparently, it is not the best practice to use a ghost branch, also not the best practice to use the master branch to track a sub-folder of the ghost branch. These are some twisted logic puzzles for the mind. But that's how Octopress works!

Once the logic is clear, I only need to do the following three things to resume blogging:

**1. Clone source from ghost branch** (my ghost branch named `source`)

```bash
git clone -b source https://github.com/YOURNAME/YOURNAME.github.io.git
```

**2. Clone GitHub Page (to a sub-directory `_deploy`) from master branch**

```bash
cd YOURNAME.github.io
mkdir _deploy
git clone https://github.com/YOURNAME/YOURNAME.github.io.git _deploy
```

**3. Re-install the plugins for my blog**

```bash
bundle install --path vendor/bundle
```

Of course, you need to have installed the [Bundler](https://bundler.io/) to use the `bundle` command, and to do that on a Mac you will probably need to first install [rbenv](https://github.com/rbenv/rbenv) for smoothly running your blog by executing Ruby commands. In other word, you will need to set up your environment again for Octopress, which I have covered in my [first blog post](/blog/2016/08/06/yong-you-ni-de-ge-ren-bo-ke/index.html) (in Chinese).