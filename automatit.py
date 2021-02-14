import requests

def test():
  r = requests.get('http://ip.jsontest.com/')
  print("Response object:", r)
  print("Response Text:", r.text)

test();
