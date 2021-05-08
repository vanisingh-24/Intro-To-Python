## Inner or Nested Functions

def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()

if __name__ == '__main__':
    outerFunction('Hey')

def f1():
    s = 'I love gfg'

    def f2():
        print(s)

    f2()
f1()

def f1():
    s = 'I love gfg'

    def f2():
        s = 'Me too'
        print(s)

    f2()
    print(s)

f1()

# Using an iterable to change the value of the variable of the outer function.

def f1():
    s = ['I love gfg']

    def f2():
        s[0] = 'Me too'
        print(s)

    f2()
    print(s)

f1()

# Using non local keyword to change the value of the variable of the outer function.

def f1():
    s = 'I love gfg'

    def f2():
        nonlocal s
        s = 'Me too'
        print(s)

    f2()
    print(s)

f1()

def f1():
    f1.s = 'I love gfg'

    def f2():
        f1.s = 'Me too'
        print(f1.s)

    f2()
    print(f1.s)

f1()

