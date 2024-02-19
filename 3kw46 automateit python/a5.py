# fun with automatit


import bs4

# parse a.html
def test():
    myfile=open('a.html')
    soup=bs4.BeautifulSoup(myfile,"lxml")
    # make the soup
    print("BeautifulSoup object:",type(soup))

    # find elements by tags
    print("find elements by tags..")
    print(soup.find_all('a'))
    print(soup.find_all('strong'))
    print(soup.find_all('div'))
    print(soup.find_all('p'))
    print(soup.find_all('h1'))

    # find elements by id
    print("find elements by id...")
    print(soup.find('div',{"id":"inventor"}))
    print(soup.find_all('p',{"class":"wow"}))
    print(soup.find_all('h1',{"class":"wow"}))
    print(soup.select("#inventor"))
    print(soup.select(".wow"))


from bs4 import BeautifulSoup
import re
import urllib2
import os
def test2():
    image_type="Project"
    movie="avatar"
    url="https://www.google.com/search?q="+movie+"&source=lnm&tbm=isch"
    url="https://www.google.com/search?q=avatar&source=lnm&tbm=isch"
    header={'User-Agent':'Mozilla/5.0'}
    soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),"lxml")

    print("type(soup):",type(soup))
    print("soup:",soup )

    imgs=[a['src'] for a in soup.find_all("img",{"src":re.compile("gstatic.com")})][:5]
    for img in imgs:
        print("image source:", img)

    for img in imgs:
        raw_img=urllib2.urlopen(img).read()
        cntr=len([i for i in os.listdir(".") if image_type in i]) + 1
        f=open("Project_" + str(cntr)+ ".jpg", "wb")
        f.write(raw_img)
        f.close()

def test3():
    url="https://www.immobilienscout24.de/Suche/radius/wohnung-mieten?centerofsearchaddress=M%C3%BCnchen;81829;;;;;&geocoordinates=48.13185;11.6785;5.0&enteredFrom=one_step_search"
    header={'User-Agent':'Mozilla/5.0'}
    soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),"lxml")
    print(soup)


#test()
#test2()
test3()

