import urllib, sys
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的AK】&client_secret=【官网获取的SK】'
request = urllib.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.urlopen(request)
content = response.read()
if (content):
    print(content)

import http