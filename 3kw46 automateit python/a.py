# automateit / needs python 2.7
# 23-11-14

from lxml import html
import requests

def test1():
    r=requests.get('http://ip.jsontest.com')
    print("Response object:",r)
    print("Response text:",r.text)

def test2():
    payload={'q':'chetan'}
    r=requests.get('https://github.com/search',params=payload)
    print('Request URL:',r.url)

def test3():
    payload={'key1':'value1'}
    r=requests.post('http://httpbin.org/post',data=payload)
    print("response statuscode:",r.status_code)
    print("response json:",r.json)
    print("response text:",r.text)
    print("response content:",r.content)
    print("response url:",r.url)

def test4():
    try:
        r=requests.get('http://www.google.com')
    except requests.exceptions.RequestException as e:
        # no internet will trigger this exception
        print('Error response:', e.message)


from lxml import html
import requests

def test5():
    page=requests.get('https://github.com/pricing')
    tree=html.fromstring(page.content)
    print('page object:', tree)
    plans=tree.xpath('//h2[@class="mb-2 h5-mktg"]/text()')
    pricing=tree.xpath('//span[@class="js-computed-value"]/text()')
    pricing2=pricing[1:6:2] # take the first 3 odd elements, which correspond to the plan prices..
    print("Plans:",plans, "\nPricing:",pricing2)

# experiment with scraping https://myrient.erista.me/files/Redump/
# 23-12-03
def myrient():
    page=requests.get('https://myrient.erista.me/files/Redump')
    tree=html.fromstring(page.content)
    print(tree)
    rig=tree.xpath('//td[@class="link"]/text()')
    print("rig:",rig)


myrient()
