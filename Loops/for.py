## For Loop
# SYNTAX - for var in iterable:
               # statements

# Iterating over a list
l = ["geeks", "for", "geeks"]

for i in l:
    print(i)

# Iterating over a tuple

t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Iterating over a String

s = "Geeks"
for i in s:
    print(i)

# Iterating over dictionary

d = dict()
d['xyz'] = 123
d['abc'] = 456
for i in d:
    print("%s %d" %(i, d[i]))


##  For-Else Loop

# Executed because no break
for i in range(1,4):
    print(i)
else:
    print("No Break")

# Not executed as there is a break

for i in range(1, 4):
    print(i)
    break
else: 
    print("No Break")


## range() function

for i in range(10):
    print(i,end=" ")

l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end=" ")

sum = 0
for i in range(1,10):
    sum = sum + i
print(sum)






