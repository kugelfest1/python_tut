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


test3()
