# Given the string, the task is to generate the same string using the random combination of special character, numbers, and alphabets

import string
import random
import time

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'

t = "geek"

attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(t)))
attemptNext = ''

completed = False
iteration = 0

while completed == False:
    print(attemptThis)

    attemptNext = ''
    completed = True

    for i in range(len(t)):
        if attemptThis[i] != t[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += t[i]

    iteration += 1
    attemptThis = attemptNext
    time.sleep(0.1)

# Driver Code
print("Target matched after" + str(iteration) + "iterations")