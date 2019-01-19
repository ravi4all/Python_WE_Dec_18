import bs4
import urllib.request as url

page = url.urlopen('https://www.imdb.com/list/ls052958717/')

webpage = bs4.BeautifulSoup(page, 'lxml')

'''
title = webpage.find('h3', class_='lister-item-header')
print("Movie - ",title.text.replace('\n',''))

rating = webpage.find('span', class_='ipl-rating-star__rating')
print("Rating - ",rating.text)

div = webpage.find('div', class_='ipl-rating-widget')
p = div.findNextSibling()
print("Summary - ",p.text.replace('\n','').strip())
'''

title = webpage.findAll('h3', class_='lister-item-header')
for m in title:
    print(m.text.replace('\n',''))
