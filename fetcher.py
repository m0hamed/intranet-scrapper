#!/usr/bin/env python2
import requests, sys
from Crypto.Cipher import AES
from Crypto import Random
from requests_ntlm import HttpNtlmAuth
from BeautifulSoup import BeautifulSoup as bs

BASE_URL = "http://student.guc.edu.eg/intranet/Faculties/Media%20Engineering%20Technology/Berlin/Winter%202013/7th%20Semester/CSEN%20704%20-%20Advanced%20Computer%20Lab/"

def get_credentials():
  global PASS, USER
  USER = raw_input("Enter your GUC username: ")
  PASS = raw_input("Enter your GUC password: ")

def check_page(url=BASE_URL):
  r = requests.get(url, auth=HttpNtlmAuth('guc\\%s' % (USER, ), PASS))
  page = bs(r.content)
  links = page.findAll("a")
  if links > 1:
    return True
  else:
    return False

def get_url(number):
  url = BASE_URL + "Lab%%20%i/" % (number, )
  return url

def usage():
  print """No lab number specified!
  Usage: %s <lab-number>""" % (sys.argv[0], )

def found():
  pass

if __name__ == "__main__":
  if len(sys.argv) < 2:
    usage()
    exit()
  number = int(sys.argv[1])
  get_credentials()
  print "Checking if lab %i has been posted" % number
  while not check_page(get_url(number)):
    sys.stdin.write(".")
    found()
