#!/usr/bin/python

from sys import argv
import time
import os 
import urllib2

print''' 
       \033[3;37;37m Enumerating Subdomains using subfinder...  \033[3;31;31m
'''
print'''
                \033[3;37;37m By Hannan Haseeb \033[3;31;31m
'''
target = raw_input('\033[3;37;37m Enter website name : \033[3;31;31m') 
output = os.popen('subfinder -d ' + target).read()
with open('output.txt', 'w+') as f:
  f.write(output)
with open('output.txt', 'r+') as file:
  output = file.readlines()

print'''
        \033[3;37;37m Checking ClickJacking on gather subdomains... \033[3;31;31m
'''

for subdomain in output:
    newsubdomain = "http://%s" % subdomain
    try:
      a = urllib2.urlopen(newsubdomain)
      code = a.getcode();
      if a.info().getheader('X-Frame-Options')!="SAMEORIGIN" and a.info().getheader('X-Frame-Options')!="DENY":
         print "\r Domain : %s is Vulernable To ClickJacking!" % (newsubdomain)
      else:
         print "\r Domain : %s Not Vulernable To Click Jacking" % (newsubdomain)

    except urllib2.HTTPError, e:
           code = e.code
           print "\r Domain : %s Not Vulernable To Click Jacking " % (newsubdomain)
    except urllib2.URLError, e:
           print "\r Domain : %s Not Vulernable To Click Jacking" % (newsubdomain)

