# Python program to check for URL in a string

import re

def findUrl(string):

  regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(regex, string)
  return [x[0] for x in url]

string = 'My Profile: https://github.com/vanisingh-24'
print("Urls: ", findUrl(string))
















