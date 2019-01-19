import bs4
import urllib.request as url

def search():

    userInput = input("Enter movie name : ")
    userInput = userInput.replace(' ','%20')
    path = 'https://www.imdb.com/find?ref_=nv_sr_fn&q='+userInput
    page = url.urlopen(path)

    webpage = bs4.BeautifulSoup(page, 'lxml')

    td = webpage.find('td', class_='result_text')
    anchorTag = td.find('a')
    #print(anchorTag)
    href = anchorTag['href']
    newUrl = 'https://www.imdb.com'+href
    newPage = url.urlopen(newUrl)
    newWebPage = bs4.BeautifulSoup(newPage, 'lxml')

    title = newWebPage.find('div', class_='title_wrapper')
    title = title.text.replace('\n','')
    title = title.replace('  ','')
    print(title)
