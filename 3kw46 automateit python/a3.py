# needs python 2.7, to invoke: py -2 a3.py

from bs4 import BeautifulSoup
import re
import urllib2
import os

def test():
    # download parameters
    image_type='Project'
    movie='Avatar'
    url="https://www.google.com/search?q="+movie+"&source=lnm&tbm=isch"
    header={'User-Agent':'Mozilla/5.0'}
    soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)))

    # find all img elements from the soup which contain "gstatic.com" and save the "src" attribute for each of these img elements, up to 5 times.
    images=[a['src'] for a in soup.find_all("img",{"src":re.compile("gstatic.com")})[:5]]
    for img in images:
        print "Image Source:",img
        raw_img=urllib2.urlopen(img).read()
        cntr=len([i for i in os.listdir(".") if image_type in i]) + 1
        f = open(image_type + "_"+str(cntr)+".jpg",'wb')
        f.write(raw_img)
        f.close()

# experiment with scraping https://myrient.erista.me/files/Redump/..
# 2023-12-03
def test2():
    url='https://myrient.erista.me/files/Redump/'
    header={'User-Agent':'Mozilla/5.0'}
    soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)),features="lxml")
    ls=soup.find_all("table",{"id":"list"})
    # find all 'a' elements which contain a nonempty "title" attribute
    rigs=ls[0].find_all("a",{"title":re.compile("\w")})
    for i in rigs:
        print(i.get('href'),i.get('title'))

    print('-'*80)
    
    # scrape list from each rig element..
    for i in rigs:
        url2=url+i.get('href')
        print(url2)

test2()