# Given a name, print the initials of a name(uppercase) with last name(with first alphabet in uppercase) written in full separated by dots.

def name(s):
  w = s.split()
  new = ""

  for i in range(len(w) - 1):
    s = w[i]

    new += (s[0].upper()+'.')

  new += w[-1].title()

  return new

# Driver Code
s ="mohandas karamchand gandhi" 
print(name(s)) 


