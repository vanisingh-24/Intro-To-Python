# Given a string, print and count all prefixes in which first alphabet has greater frequency than second alphabet.

def prefix(string1, alphabet1, alphabet2):
  count = 0
  non_empty_string = ""

  string2 = list(string1)

  for i in range(0, len(string2)):
    non_empty_string = non_empty_string + (string2[i])

    if(non_empty_string.count(alphabet1) > non_empty_string.count(alphabet2)):
      print(non_empty_string)
      count += 1

  return(count)

# Driver Code
print(prefix("geeksforgeeks", "e", "g"))