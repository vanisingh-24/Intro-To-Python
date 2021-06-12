# Break a list into chunks of size N in Python

my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky','nerdy', 'geek', 'love',
               'questions','words', 'life']

def chunks(l,n):
  for i in range(0, len(l), n):
    yield l[i:i+n]

n = 5
x = list(chunks(my_list, n))
print(x)

# OR

l = [1,2,3,4,5,6,7,8,9]

n = 4

x = [l[i:i+n] for i in range(0, len(l),n)]
print(x)


