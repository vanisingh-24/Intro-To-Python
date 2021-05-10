# Count and display vowels in a string

def check_vowel(string, vowels):
  result = [i for i in string if i in vowels]
  print(len(result))
  print(result)

string = 'Geeks For Geeks'
vowels = 'AaEeIiOoUu'
check_vowel(string, vowels)

# OR
# Dictionary Way

def check_vowel(string, vowels):
  string = string.casefold()

  count = {}.fromkeys(vowels,0)

  for i in string:
    if i in count:
      count[i] += 1
  return count

vowels = 'aeiou'
string = 'Geeks For Geeks'
print(check_vowel(string,vowels))


