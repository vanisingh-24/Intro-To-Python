## Loop Control Statements

#1 Continue Statement

for letter in 'geeksforgeeks':
    if letter='e' or letter = 's':
        continue
    print(letter)

i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i =+ 1
        continue
    print(a[i])
    i += 1

#2 Break Statement

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
print(letter)

#3 Pass Statement

for letter in 'geeksforgeeks':
    pass
print(letter)

