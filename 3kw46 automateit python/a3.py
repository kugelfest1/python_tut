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

test()