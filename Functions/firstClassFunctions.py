## First Class functions

## 1. Functions are objects

def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout
print(yell('Hello'))

## 2. Functions can be passed as arguments to other functions

def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("""Hi, I am created by a function
                    passed as an argument.""")
    print(greeting)

greet(shout)
greet(whisper)

## 3. Functions can return another function

def create_adder(x):
    def adder(y):
        return x+y
 
    return adder

add_15 = create_adder(15)
print(add_15(10))

def outer(x):
    return x*10

def my_fun():
    return outer

res = my_fun()
print(res(10))
