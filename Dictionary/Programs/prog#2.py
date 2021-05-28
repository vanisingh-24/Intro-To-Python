# Zip function in Python to change to a new character set

def newString(charSet, input):
  origCharSet = 'abcdefghijklmnopqrstuvwxyz'
  mapChars = dict(zip(charSet, origCharSet))

  changeChars = [mapChars[chr] for chr in input]

  print(''.join(changeChars))

# Driver Code
charSet = 'qwertyuiopasdfghjklzxcvbnm'
input = 'utta'
newString(charSet,input)