# parse a.html

import bs4
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

test()
