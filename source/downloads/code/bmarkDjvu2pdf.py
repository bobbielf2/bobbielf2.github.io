#! /usr/bin/env python
metadata = '' # string to be written into PDF metadata
f = open("bmarks.out") # open input file: djvu outline
line = f.readline().strip()
if line.startswith('(bookmarks'):
    level = 0

while (level >= 0):
    line = f.readline().strip()
    if line.startswith('("'):
        level = level + 1
        metadata = metadata + "BookmarkBegin\nBookmarkTitle: "+line.strip('("')+"\nBookmarkLevel: "+str(level)+'\n'
        line = f.readline().strip()
        while line.endswith(')'):
            level = level - 1
            line = line[:-1].strip()
        metadata = metadata + "BookmarkPageNumber: "+line.strip('"#')+'\n'
    else:
        while line.endswith(')'):
            level = level - 1
            line = line[:-1].strip()

f.close()
f = open("bmarks2.txt",'w') # output file: for PDF metadata
f.write(metadata)
f.close()
