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



----

### (Updates on 2019-11-20) Using `rbenv` on MacOS Catalina

After I upgraded my MacOS to 10.15 Catalina, I encountered troubles again. This time, when I do `rake` commands, I got the error message: 

```
You must use Bundler 2 or greater with this lockfile.
```

So I need to update the `bundler` to version 2 or higher. 

However, when I did `gem install bundler`, I got permission error again -- this means that `gem` is trying to install bundler on Mac's default system ruby, in other words, `rbenv` is broken.

So I tried to reinstall `rbenv` :

```bash
brew reinstall rbenv
rbenv init
```

and then install a custom `ruby` (version 2.6.5):

```bash
rbenv install 2.6.5
```

However, in this last step, I constantly ran into troubles. It was a long debugging process, so I am just going to list the hurdles that I have gone through, which maybe helpful to others.

**Hurdle #1**: `openssl` overhead

 `rbenv` keep trying to first install `openssl` before actually installing `ruby 2.6.5`, this is taking a lot of time and greatly reducing my debugging efficiency. I checked `which openssl` and confirmed that my system has already had `openssl` installed. So I need to tell `rbenv` to use my system's `openssl`. I do this with the command:

```bash
RUBY_CONFIGURE_OPTS=--with-openssl-dir=/opt/local CC=/usr/bin/gcc rbenv install 2.6.5
```

**Hurdle #2**: incorrect C compiler

After many fails, I finally found out in the error log that `rbenv` is using `CC=x86_64-apple-darwin13.4.0-clang` as C compiler and therefore has not been able to compile and install ruby. This can be resolved by explicitly telling `rbenv` to use the system compiler `/usr/bin/gcc`.

```bash
CC=/usr/bin/gcc RUBY_CONFIGURE_OPTS=--with-openssl-dir=/opt/local rbenv install 2.6.5
```

**Hurdle #3**: anaconda gets in the way

After the previous two fixes, I am still unable to install ruby. This time I found the following lines in the error log:

```
/anaconda3/bin/x86_64-apple-darwin13.4.0-ar: illegal option -- n
usage:  ar -d [-TLsv] archive file ...
```

It turns out that `rbenv` is using anaconda's `ar` function instead of the system's own `ar`. So I need to disable anaconda in my system as follows:

* Open the `~/.bash_profile` file, remove/comment out any lines that have to do with anaconda/conda
* Restart terminal
* Try install ruby again:

```bash
RUBY_CONFIGURE_OPTS=--with-openssl-dir=/opt/local rbenv install 2.6.5
```

Finally, I was able to install ruby on `rbenv`! Notice that in the last command I have removed `CC=/usr/bin/gcc`, because disabling anaconda also resolves the problem in Hurdle #2.

#### Final Steps

After installing a custom ruby, I need to first tell the system to use that version of ruby

```bash
rbenv global 2.6.5
```

Then I can go back to my Octopress blog folder and install the newest bundler

```bash
gem install bundler
bundle install
```

However, there is still a final small hurdle for me:

**Hurdle #4**: rake version

When I tried to create a new blog post via `rake new_post['title']`, I got the following error message:

```
rake aborted!
Gem::LoadError: You have already activated rake 12.3.2, but your Gemfile requires rake 10.5.0. Prepending `bundle exec` to your command may solve this.
```

So I just open the `Gemfile` in my Octopress folder, find the line with `gem 'rake', '~> 10.5'`, change it to `gem 'rake', '~> 12.3'`, and then `bundle install` again. Now it's all set.