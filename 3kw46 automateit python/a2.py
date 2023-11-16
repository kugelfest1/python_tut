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

test2()
