# automatit
# 2021-02-14, created

import requests

def test():
  r = requests.get('http://ip.jsontest.com/')
  print("Response object:", r)
  print("Response Text:", r.text)


def test2():
  payload = {'q': 'chetan'}
  r = requests.get('https://github.com/search', params=payload)
  print("Request URL:", r.url)

def test3():
  payload = {'key1': 'value1'}
  r = requests.post("http://httpbin.org/post", data=payload)
  print("Response text:", r.json())


from lxml import html
import requests
def test4():
  page = requests.get('https://github.com/pricing/')
  tree = html.fromstring(page.content)
  print("Page Object:", tree)
  plans = tree.xpath('//h2[@class="pricing-card-name alt-h3"]/text()')
  pricing = tree.xpath('//span[@class="defaultcurrency"]/text()')
  print("Plans:", plans, "\nPricing:", pricing)

def test5():
  import bs4
  myfile = open('automatit.html')
  soup = bs4.BeautifulSoup(myfile, "lxml") #Making the soup
  print "BeautifulSoup Object:", type(soup)

  #Find Elements By tags
  print soup.find_all('a')
  print soup.find_all('strong')
  #Find Elements By id
  print soup.find('div', {"id":"inventor"})
  print soup.select('#inventor')
  #Find Elements by css print
  soup.select('.wow')

  print "Facebook URL:", soup.find_all('a')[0]['href']
  print "Inventor:", soup.find('div', {"id":"inventor"}).text
  print "Span content:", soup.select('span')[0].getText()

def test6():
  from bs4 import BeautifulSoup
  import re
  import urllib2
  import os
  ## Download paramters
  image_type = "Project"
  movie = "Avatar"
  movie = "avengers"
  url = "https://www.google.com/search?q="+movie+"&source=lnms&tbm=isch"

  header = {'User-Agent': 'Mozilla/5.0'}
  soup = BeautifulSoup(urllib2.urlopen (urllib2.Request(url,headers=header)))

  images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})][:5]
  for img in images:
    print "Image Source:", img

  for img in images:
    raw_img = urllib2.urlopen(img).read()
    cntr = len([i for i in os.listdir(".") if image_type in i]) + 1
    f = open(image_type + "_"+ str(cntr)+".jpg", 'wb')
    f.write(raw_img)
    f.close()



test6()
