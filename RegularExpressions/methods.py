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

import re

# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# \d+ will match a group on [0-9], group of one or greater size
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

import re

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))

# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))

import re

p  = re.compile('ab*')
print(p.findall("ababbaabbb"))

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

# 5. re.escape()
# SYNTAX - re.escape(string)

import re

print(re.escape("This is Awseome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))

# 6. re.sub()
# SYNTAX - re.subn(pattern, repl, string, count=0, flags=0)

import re

print(re.sub('ub', '~*','Subject has Uber booked already', flags = re.IGNORECASE))

print(re.sub('ub','~*','Subject has Uber already booked'))

print(re.sub('ub', '~*' , 'Subject has Uber booked already', count=1, flags = re.IGNORECASE))

print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags = re.IGNORECASE))

# 7. re.subn()
# SYNTAX - re.subn(pattern, repl, string, count=0, flags=0)

import re

print(re.subn('ub','~*' , 'Subject has Uber booked already'))
t = re.subn('ub','~*','Subject has Uber booked already', flags = re.IGNORECASE)
print(t)
print(len(t))
print(t[0])

