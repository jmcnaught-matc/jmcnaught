#!/usr/bin/env python3

import bs4
myFile = open('my_web_file.html')
mySoup = bs4.BeautifulSoup(myFile.read(), features='html.parser')
titleElem = mySoup.select('title')
title = titleElem[0].getText()
print(title)
linkElem = mySoup.select('a')
for link in linkElem:
    print(link.getText())