# Python program to find the Second most repeated word in a sequence

from collections import Counter

def secondFrequent(input):
  dict = Counter(input)

  value = sorted(dict.values(),reverse = True)

  secondLarge = value[1]

  for (key, value) in dict.items():
    if value == secondLarge:
      print(key)
      return

# Driver Code
input = ['aaa','bbb','ccc','bbb','aaa','aaa'] 
secondFrequent(input)

# OR

def secondFrequent(input):
    from collections import Counter
  
    c = Counter(input) 
       
    print(c.most_common()[1][0])
  
# Driver code
input = ['aaa','bbb','ccc','bbb','aaa','aaa']
secondFrequent(input)