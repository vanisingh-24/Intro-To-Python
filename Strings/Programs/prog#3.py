# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python

def print_full_name(first, second):
    print("Hello " + first + " " + second + "! You just delved into python.")

firstname = input()
lastname = input()
print_full_name(firstname,lastname)