# automateit tut
# py -2 -m pip install beautifulsoup4

import bs4

def test():
    pass

def test2():
    myfile=open('a2.html')
    soup=bs4.BeautifulSoup(myfile,"lxml")
    # Making the soup
    print('Beautifulsoup object:', type(soup))    

    #find elemsnts by tags
    print(soup.find_all('a'))
    print(soup.find_all('strong'))
    # find elements by id
    print(soup.find('div',{"id":"inventor"}))
    print(soup.select('#inventor'))
    # find element by css print
    soup.select('.wow')
    print("Facebook URL:",soup.find_all('a')[0]['href'])
    print("Inventor:",soup.find('div',{'id':'inventor'}).text)
    print("Span content:", soup.select('span')[0].getText())

test2()
