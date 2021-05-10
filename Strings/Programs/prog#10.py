# Swap commas and dots in a String

def replace(str):
  str = str.replace(', ', 'temp')
  str = str.replace('.', ', ')
  str = str.replace('temp', '.')
  return str

string = '14, 625, 498.002'
print(replace(string))



