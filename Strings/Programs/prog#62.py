# Given a string, the task is to check if that string contains any special character (defined special character set).
# If any special character found, don’t accept that string.

import re

def run(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if(regex.search(string) == None):
        print("String is accepted")
    else:
        print("String not accepted")

if __name__ == "__main__":
    string = "Geeks$For$Geeks"

    run(string)