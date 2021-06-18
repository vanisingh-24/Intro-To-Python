## Frequently used methods:

# 1. re.findall()

import re

string = """ Hello my Number is 123456789 and 
             my friend's number is 987654321"""

regex = '\d+'

match = re.findall(regex, string)
print(match)

# 2. re.complie()

import re

p = re.compile('[a-e]')
print(p.findall("Aye, said Mr. Gibenson Stark"))

# 3. re.match()

def findMonthAndDate(string): 
       
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string) 
       
    if match == None:  
        print("Not a valid date")
        return
   
    print("Given Data: % s" % (match.group()))
    print("Month: % s" % (match.group(1)))
    print("Day: % s" % (match.group(2)))
   
       
# Driver Code 
findMonthAndDate("Jun 24") 
print("") 
findMonthAndDate("I was born on June 24")

# 4. re.search()

import re

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24")

if match != None:
  print("Match at index %s, %s" %(match.start(), match.end()))

  # this will print "June 24" 
  print("Full match: % s" % (match.group(0)))
   
  # this will print "June" 
  print("Month: % s" % (match.group(1)))
   
  # this will print "24" 
  print("Day: % s" % (match.group(2)))

else:
  print("The regex pattern does not match")


