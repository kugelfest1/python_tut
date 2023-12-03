# needs python 2.7, to invoke: py -2 a3.py

from bs4 import BeautifulSoup
import re
import urllib2
import os
import time
import sys

HEADER={'User-Agent':'Mozilla/5.0'}

def test():
    global HEADER
    # download parameters
    image_type='Project'
    movie='Avatar'
    url="https://www.google.com/search?q="+movie+"&source=lnm&tbm=isch"
    soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=HEADER)))

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
    global HEADER
    url='https://myrient.erista.me/files/Redump/'
    soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=HEADER)),features="lxml")
    ls=soup.find_all("table",{"id":"list"})
    # find all 'a' elements which contain a nonempty "title" attribute
    rigs=ls[0].find_all("a",{"title":re.compile("\w")})
    for i in rigs:
        print(i.get('href'),i.get('title'))

    print('-'*80)

    # scrape list from each rig element..
    for i in rigs[:1]:
#        print(i.get('href'))
        url2=url+i.get('href')
        print(url2)
        soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url2,headers=HEADER)),features="lxml")
        # find all 'a' elements which contain a nonempty "title" attribute
        zz=soup.find_all("a",{"title":re.compile("\w")})
        for i in zz:
            print(i.get('href'),i.get('title'))
        print('-'*80)


# tidy test2
def test3():
    global HEADER
    url='https://myrient.erista.me/files/Redump/'
    soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=HEADER)),features="lxml")
    ls=soup.find_all("table",{"id":"list"})
    # find all 'a' elements which contain a nonempty "title" attribute
    rigs=ls[0].find_all("a",{"title":re.compile("\w")})
    for i in rigs:
        print(i.get('href'),i.get('title'))
#        print(i.get('href'))
        url2=url+i.get('href')
        print(url2)
        soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url2,headers=HEADER)),features="lxml")
        # find all 'a' elements which contain a nonempty "title" attribute
        zz=soup.find_all("a",{"title":re.compile("\w")})
        for i in zz:
            print(i.get('href'),i.get('title'))
        print('-'*80)

    print('-'*80)

# scrape directory listing
def test3a():
    global HEADER
    url='https://myrient.erista.me/files/Redump/'
    soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=HEADER)),features="lxml")
    ls=soup.find_all("table",{"id":"list"})
    # find all 'a' elements which contain a nonempty "title" attribute
    rigs=ls[0].find_all("a",{"title":re.compile("\w")})
    for i in rigs:
        print(i.get('title'))

# scrape all zip urls under 'https://myrient.erista.me/files/Redump/'
def test3b():
    global HEADER
#    url='https://myrient.erista.me/files/No-Intro/'
    url='https://myrient.erista.me/files/Redump/'
    try:
#        f=open("nointro.txt","w",buffering=0)    # unbuffered
        f=open("redump.txt","w",buffering=0)    # unbuffered
        soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=HEADER)),features="lxml")
        ls=soup.find_all("table",{"id":"list"})
        # find all 'a' elements which contain a nonempty "title" attribute
        rigs=ls[0].find_all("a",{"title":re.compile("\w")})
        for i in rigs:
    #        print(i.get('href'),i.get('title'))
    #        print(i.get('href'))
            url2=url+i.get('href')
            sys.stdout.write(i.get('title'))

            # try max x times
            for i in range(5):
                try:
                    soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url2,headers=HEADER)),features="lxml")
                    # find all 'a' elements which contain a nonempty "title" attribute
                    zz=soup.find_all("a",{"title":re.compile("\w")})
                    for i in zz:
                        f.write(url2+i.get('href')+'\n')
                        sys.stdout.write('.')
                except:
                    sys.stdout.write("-%-retrying.. \n")
                    time.sleep(2**i)
                    continue
                break
    #        print('-'*80)
    except:
        sys.stdout.write("-%-buggered\n")

    f.close()

test3b()