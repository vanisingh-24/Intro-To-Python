fruits = ["apple", "orange", "kiwi"]

# Creating an iterator object from that iterable i.e fruits
iter_obj = iter(fruits)

# Infinite while loop
while True:
    try:

        # Getting next item
        fruit = next(iter_obj)
        print(fruit)

        # if StopIteration is raised, break from loop
    except StopIteration:
        break

games = ['tennis', 'baseball', 'rugby', 'soccer']
iterator = iter(games)

print(next(iterator))
print(next(iterator))
print(next(iterator))

def newForLoop(iterable):

    iterator = iter(iterable)

    loopingFinished = False

    while not loopingFinished:
        try:
            nextItem = next(iterator)
        except StopIteration:
            loopingFinished = True
        else:
            print(nextItem)

# Driver's code
newForLoop([1, 2, 3, 4])

numList = [0,2,4]

# Creating a generator named "squares"
squares = (n**2 for n in numList)

print(next(squares))
print(next(squares))
print(next(squares))













