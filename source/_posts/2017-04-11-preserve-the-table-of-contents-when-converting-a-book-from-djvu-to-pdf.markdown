---
layout: post
title: "Preserve the table of contents when converting a book from Djvu to PDF"
date: 2017-04-11 20:47:57 -0400
comments: true
categories: Technology
published: true
---

There are many readily available softwares (e.g. [DjVu2PDF]) for converting a book from `.djvu` to `.pdf` format, but none of those will preserve the table of contents in the output PDF.

<!--more-->

[DjVu2PDF]: https://itunes.apple.com/us/app/djvu2pdf/id629039447?mt=12

Having a table of contents is very handy. For example when viewing a book in Preview, the table of contents works like a multi-level bookmark, you can simply click on any link in the sidebar to jump to any chapter/section of the book.

{% img /images/blog_figures/toc_in_preview.png 600 %}

So I Googled and found [this quetion] on StackExchange that asked exactly my question. Here is a summary of the accepted answer on how you can preserve (or more precisely, create) the table of contents in a PDF converted from Djvu.

[this quetion]: https://superuser.com/a/915399

## 1. Preliminary

You will need to install [pdftk] \(part of PDFtk Server) and [djvused] \(part of DjVuLibre)

[pdftk]: https://www.pdflabs.com/tools/pdftk-server/
[djvused]: https://sourceforge.net/projects/djvu/

**Note 1:** pdftk for Mac OS X 10.11 and above. I found in [this answer] on Stack Overflow that the developer of PDFtk provides an installer for PDFtk Server on OS X 10.11 and above. It is kind of strange that the [official website] only provides the installer for OS X up to 10.8. (This older version can be installed, but won't run. When you type pdftk commands in the Terminal, it will make you wait forever.) 

[this answer]: http://stackoverflow.com/a/33248310/4608899
[official website]: https://www.pdflabs.com/tools/pdftk-server/

**Note 2:** About djvused command line setup on OS X. After installing DjVuLibre, in order to use djvused in command line, you need to run 

``` bash
eval '/Applications/DjView.app/Contents/setpath.sh'
```

If this doesn't add the correct path, you can also manually add the following line into `~/.bash_profile`

``` vim
PATH="/Applications/DjView.app/Contents/bin:${PATH}"
```

## 2. Convert the Table of Contents

(Note: all materials in this section follow closely the [original answer] on StackExchange, except I did a very simple python program in Step 2.)

[original answer]: https://superuser.com/a/915399

Suppose now you have converted `book.djvu` into `book.pdf`, the former has a table of contests but the latter doesn't.

### Step 1. extract Djvu outline

Use the following command to extract the table of contents from `book.djvu`

``` bash
djvused "book.djvu" -e 'print-outline' > bmarks.out
```

The output file `bmarks.out` lists the table of contents in a serialized tree format using [SEXPR], which can be summarized as:

``` 
file ::= (bookmarks
           <bookmark>*)
bookmark ::= (name
               page
               <bookmark>*)
name ::= "<character>*"
page ::= "#<digit>+"
```

[SEXPR]: https://en.wikipedia.org/wiki/S-expression

Notice that under this format, you can append a "child bookmark" inside a "parent bookmark". For example, a `bmarks.out` may look like this

``` 
(bookmarks
  ("bmark1"
    "#1")
  ("bmark2"
    "#5"
    ("bmark2subbmark1"
      "#6")
    ("bmark2subbmark2"
      "#7"))
  ("bmark3"
    "#9"
    ...))
```

### Step 2. translate the Djvu outline to PDF metadata format

Now, Djvu and PDF store the bookmark data in different formats. While Djvu uses SEXPR, PDF uses metadata, which looks like this:

``` 
file ::= <entry>*
entry ::= BookmarkBegin
          BookmarkTitle: <title>
          BookmarkLevel: <number>
          BookmarkPageNumber: <number>
title ::= <character>*
```

The example in Step 1 when translated into PDF metadata will look like

``` 
BookmarkBegin
BookmarkTitle: bmark1
BookmarkLevel: 1
BookmarkPageNumber: 1
BookmarkBegin
BookmarkTitle: bmark2
BookmarkLevel: 1
BookmarkPageNumber: 5
BookmarkBegin
BookmarkTitle: bmark2subbmark1
BookmarkLevel: 2
BookmarkPageNumber: 6
BookmarkBegin
BookmarkTitle: bmark2subbmark2
BookmarkLevel: 2
BookmarkPageNumber: 7
BookmarkBegin
BookmarkTitle: bmark3
BookmarkLevel: 1
BookmarkPageNumber: 9
...
```

It is a fun exercise to work out the correspondence of the two formats. 

**Note:** I have written a python program to automatically convert the Djvu SEXPR `bmarks.out` into the PDF metadata form `bmarks2.txt`

{% include_code Convert Djvu outline into PDF metadata bmarkDjvu2pdf.py %}

### Step 3. modify PDF metadata to include the bookmark data

Extract PDF metadata with this command:

``` bash
pdftk "book.pdf" dump_data > pdfmetadata.out
```

Open the `pdfmetadata.out` file, and find the line that begins with `NumberOfPages:`, and insert your list of bookmarks after this line. Save the new file as `pdfmetadata.in`. Now run this command:

``` bash
pdftk "book.pdf" update_info "pdfmetadata.in" output newbook.pdf
```

The output `newbook.pdf` is your new `book.pdf` equiped with a convenient table of contents. Happy reading!

