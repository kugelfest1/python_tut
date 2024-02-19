# creating gists on github.com
# token: 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

# hint: need to create a token in github.com: go to https://github.com/settings/token, and check gists

import requests
import json


BASE_URL='https://api.github.com'
Link_URL='https://gist.github.com'
username='kugelfest1'
api_token='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'
header={'X-Github-Username': '%s' % username,
        'Content-type': 'application/c
        ',
        'Authorization': 'token %s' % api_token,
        }
gist_id=''

# 1. create the gist...
def test1():
    global gist_id
    global BASE_URL
    global Link_URL
    global username
    global api_token
    global header
    print('Creating gist...')

    
    url="/gists"
    data={
        "description":"the description for this gist",
        "public": True,
        "files": {
            "file1.txt": {
                "content": "String file contents"
            },
            "file2.txt": {
                "content": "String file contents too"
            }
        }
    }
    r=requests.post('%s%s' % (BASE_URL, url),
                    headers=header,
                    data=json.dumps(data))
    print(r.json())
    print(r.json()['url'])
    gist_id=r.json()['id']
    print(gist_id)

# 2. read the gist...
def test2():
    global gist_id
    global BASE_URL
    global Link_URL
    global username
    global api_token
    global header
    print('Reading gist %s...' % gist_id)

    url="/gists/%s" % gist_id
    r=requests.get('%s%s' % (BASE_URL, url),
                    headers=header,
                    )
    print(r.json())

# 3. update/patch the gist...
def test3():
    global gist_id
    global BASE_URL
    global Link_URL
    global username
    global api_token
    global header
    print('Updating gist %s...' % gist_id)

    data={
        "description":"updating the description for this gist",
        "files": {
            "file1.txt": {
                "content": "Updating file contents"
            },
        }
    }
    url="/gists/%s" % gist_id
    r=requests.patch('%s%s' % (BASE_URL, url),
                    headers=header,
                    data=json.dumps(data)
                    )
    print(r.json())

# 4. deleting the gist...
def test4():
    global gist_id
    global BASE_URL
    global Link_URL
    global username
    global api_token
    global header
    print('Deleting gist %s...' % gist_id)

    url="/gists/%s" % gist_id
    r=requests.delete('%s%s' % (BASE_URL, url),
                    headers=header,                    )
    print(r)

# 5. list all my gist...
def test5():
    global gist_id
    global BASE_URL
    global Link_URL
    global username
    global api_token
    global header
    print('List gists...')

    url="/users/%s/gists" % username
    r=requests.get('%s%s' % (BASE_URL, url),
                    headers=header,                    )
    gists=r.json()
    for g in gists:
#        data=g['files'].values()[0]
 
 #       print(data['filename'],
 #           data['raw_url'],data['language']
 #       )
        print(g)


#test1()
#test2()
#test3()
#test4()
test5()

