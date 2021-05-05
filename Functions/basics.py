## Defining Functions

def ask_user():
    print("Hello")

def my_func():
    a = 0
    for i in range(1,11):
        a = a+i
    return a

ask_user()
res = my_func()
print(res)