---
layout: post
title: "Beamer video tutorial"
subtitle: "how to embed videos in a presentation slides"
date: 2017-01-12 16:04:51 -0500
comments: true
categories: [Technology, LaTeX]
---

As a researcher, I often need to make presentation slides, and want to embed movies in my slides for better illustrations. After doing a little research, I converged to the solution described in this article.

<!--more-->

If you want to benefit from this tutorial, here are two most important assumptions:

**1**. Slides are made with the [**LaTeX beamer**](https://en.wikipedia.org/wiki/Beamer_(LaTeX)) package.  
**2**. Movie format is assumed to be `.flv` (because I can't play `.mp4` movies on my Mac).

Accordingly, this tutorial has two parts:

**1**. How to embed `.flv` in beamer.  
**2**. How to convert movie format to `.flv`.

## Part I: Embed `.flv` movies in LaTeX

**(I have found a better option, please ignore this part and jump to Part III)**

**Step 1**: Download the `flashmovie.sty` package file from [CTAN](http://tug.ctan.org/tex-archive/macros/latex/contrib/flashmovie/)  

> Remark: The `flashmovie.sty` package is written by Professor Timo Hartmann from TU Berlin.

**Step 2**: Download the [`player.swf`](https://ia601703.us.archive.org/8/items/JwPlayerFiles/player.swf) file from <https://archive.org/details/JwPlayerFiles>. This file is needed by the JW Player engine in order to correctly compile the `.tex` file.

**Step 3**: Embed the `.flv` movie in your beamer. Here is an example `.tex` file.

``` latex 
\RequirePackage{flashmovie}
\documentclass{beamer}   
\begin{document}
\begin{frame}
\frametitle{embed a movie}
\begin{center}
\flashmovie[width=0.7\textwidth,engine=jw-player,auto=0,image=POSTER.jpg,controlbar=1,loop=0]{YOUR_MOVIE.flv}
\end{center}    
\end{frame}
\end{document}
```
    
Here `YOUR_MOVIE.flv` is the flv movie you want to embed, and `POSTER.jpg` is the image shown before the movie is played (note that the poster image is optional).

**Step 4**: Compile the `.tex` file into PDF with all the neccessary files in the same directory (i.e. `flashmovie.sty`, `player.swf`, `YOUR_MOVIE.flv`, `POSTER.jpg`). Then open the PDF file using **Adobe Reader 9 or above**

> Remark:  
> 1. more options of the `\flashmovie` command can be found in the `flashmovie.sty` file.  
> 2. there are more different player options for `engine` other than the JW Player. For example, you may instead set `engine=flv-player` which uses an open-source player from <http://flv-player.net>. For this player another `.swf` file, [`player_flv_maxi.swf`](http://flv-player.net/medias/player_flv_maxi.swf), is needed.


## Part II: Convert movie formats to `.flv`

The software used to convert movie formats is [**FFmpeg**](https://ffmpeg.org/). This is a free and open-source software.

Assuming you are using Mac OSX like me, here are the steps:

**1**. Make sure you installed **Homebrew** on your Mac, for details go to <http://brew.sh/>.  
**2**. Install **ffmpeg** by running `brew install ffmpeg` in command line.  
**3**. Convert movie formats using the `ffmpeg` command.

> An explanation of the `ffmpeg` options can be found [here](https://www.virag.si/2012/01/web-video-encoding-tutorial-with-ffmpeg-0-9/). (Also a helpful article if your are using Windows or Linux.)

An example command that I used to convert an `.mp4` file to `.flv`:

``` bash 
ffmpeg -i input_file.mp4 -c:v libx264 -vf scale=-1:270 -ar 22050 output_file.flv
```

Some explanation of the command

* **`-i input_file.mp4`**: specify the input file
* **`-c:v libx264`**: set video codec to be libx264
* **`-vf scale=-1:270`**: set resolution of output file, `-1` means to maintain aspect ratio, `270` indicates the vertical resolution is 270p. (1080p is Full HD.) If not specified, resolution remains unchanged.
* **`-ar 22050`**: set the audio sampling frequency. If don't want any sound, use `-an` flag instead.
* **`output_file.flv`**: specify output file and format

## Part III: Embed `.flv` movies in LaTeX (To replace Part I)

**(Updated 1/19/17)**

I have used the following movie embedding option a couple times before I posted this article, but I didn't summarize it back then and forgot about it. Now memory strikes back.

The [`media9` package](https://www.ctan.org/pkg/media9?lang=en) is the best option so far for embedding movies in beamer. Here is an example `.tex` file to do it:

``` latex 
\documentclass{beamer}   
\usepackage{media9}
\usepackage{graphicx}

\begin{document}

\begin{frame}{embed a movie}
\begin{center}
\includemedia[
	width=0.4\linewidth,height=0.3\linewidth,
	activate=pageopen,
	addresource=YOUR_MOVIE.flv,
	flashvars={
	   source=YOUR_MOVIE.flv
	}
]{\includegraphics[height=0.3\linewidth]{POSTER.jpg}{VPlayer9.swf}
\end{center}
\end{frame}

\end{document}
```

A couple remarks about this example:

**1.** Compile the `.tex` file into `.pdf` with all neccesary files (`YOUR_MOVIE.flv`, `POSTER.jpg`) in the same folder  
**2.** `POSTER.jpg` is the image displayed before `YOUR_MOVIE.flv` is played, and is included using the `\includegraphics` command from the `graphicx` package. The poster image is optional, you may intead use a `{}` (before the `{VPlayer9.swf}`) to leave it blank.  
**3.** `VPlayer9.swf` is the video player. You may use a fancier player `StrobeMediaPlayback.swf` and correspondingly in the `flashvars` options change `source=...` into `src=...`. Or if you are embedding audio, use `APlayer9.swf`.  
**4.** Embedding YouTube video would be a piece of cake with this package, here is an example given in the official documentation:

``` latex 
\includemedia[  width=0.6\linewidth,height=0.3375\linewidth, % 16:9  activate=pageopen,  flashvars={    modestbranding=1 % no YT logo in control bar    &autohide=1 % controlbar autohide    &showinfo=0 % no title and other info before start    &rel=0      % no related videos after end  }]{}{http://www.youtube.com/v/r382kfkqAF4?rel=0}
```
  
**5.** Go to the [CTAN](https://www.ctan.org/pkg/media9?lang=en) page to find the complete [documentation](http://mirrors.ctan.org/macros/latex/contrib/media9/doc/media9.pdf) for `media9`.

Hope this is helpful!