# Python program to check the validity of a password

# Primary conditions for password validation :

# 1. Minimum 8 characters.
# 2. The alphabets must be between [a-z]
# 3. At least one alphabet should be of Upper Case [A-Z]
# 4. At least 1 number or digit between [0-9].
# 5. At least 1 character from [ _ or @ or $ ].

import re
password = "R@m@_f0rtu9e$"
flag = 0
while True:
  if(len(password)<8):
    flag = -1
    break
  elif not re.search("[a-z]", password):
    flag = -1
    break
  elif not re.search("[A-Z]", password):
    flag = -1
    break
  elif not re.search("[0-9]", password):
    flag = -1
    break
  elif not re.search("[_@$]", password):
    flag = -1
    break
  else:
    flag = 0
    print("Valid password")
    break

if flag == -1:
  print("Invalid Password")

