import sys
import re
from selenium import webdriver
from random import randint
from time import sleep

dr = webdriver.PhantomJS()

p=''
for l in sys.stdin:
    l=l.strip()
    while 'ENSG' not in p:
        dr.get('http://www.genecards.org/cgi-bin/carddisp.pl?gene=%s' % l)
        dr.get_cookies()
        p=dr.page_source
        sleep(randint(1,10))
    print(l, re.compile('gene=(ENSG.*?)"').search(p).group(1))
    p=''

