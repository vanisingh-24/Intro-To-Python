## *args

def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun(arg1, *argv):
    print(arg1)
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

## **kwargs

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s", %(key, value))

myFun(first ='Geeks', mid ='for', last='Geeks')   

def myFun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

myFun("Hi", first ='Geeks', mid ='for', last='Geeks')

## Using *args and **kwargs to call a function
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
myFun(**kwargs)

## Using *args and **kwargs in same line to call a function

def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")




