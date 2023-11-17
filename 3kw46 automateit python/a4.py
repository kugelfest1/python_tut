# creating gists on github.com
# token: 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

import requests
import json


gist_id=''

# 1. create the gist...
def test1():
    print('Creating gist...')

    global gist_id
    BASE_URL='https://api.github.com'
    Link_URL='https://gist.github.com'
    username='kugelfest1'
    api_token='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'
    header={'X-Github-Username': '%s' % username,
            'Content-type': 'application/json',
            'Authorization': 'token %s' % api_token,
            }
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
    print(r.json()['url'])
    gist_id=r.json()['id']
    print(gist_id)

# 2. read the gist...
def test2():
    global gist_id
    print('Reading gist %s...' % gist_id)

    BASE_URL='https://api.github.com'
    Link_URL='https://gist.github.com'
    username='kugelfest1'
    api_token='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'
#    gist_id='cd0725ef76c9bd8e3c6560e62483450d'
    header={'X-Github-Username': '%s' % username,
            'Content-type': 'application/json',
            'Authorization': 'token %s' % api_token,
            }
    url="/gists/%s" % gist_id
    r=requests.get('%s%s' % (BASE_URL, url),
                    headers=header,
                    )
    print(r.json())

# 3. update/patch the gist...
def test3():
    global gist_id
    print('Updating gist %s...' % gist_id)

    BASE_URL='https://api.github.com'
    Link_URL='https://gist.github.com'
    username='kugelfest1'
    api_token='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'
    #gist_id='cd0725ef76c9bd8e3c6560e62483450d'
    header={'X-Github-Username': '%s' % username,
            'Content-type': 'application/json',
            'Authorization': 'token %s' % api_token,
            }
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
    print('Deleting gist %s...' % gist_id)

    BASE_URL='https://api.github.com'
    Link_URL='https://gist.github.com'
    username='kugelfest1'
    api_token='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'
    #gist_id='cd0725ef76c9bd8e3c6560e62483450d'
    header={'X-Github-Username': '%s' % username,
            'Content-type': 'application/json',
            'Authorization': 'token %s' % api_token,
            }
    url="/gists/%s" % gist_id
    r=requests.delete('%s%s' % (BASE_URL, url),
                    headers=header,                    )
    print(r)



test1()
test2()
test3()
test4()

