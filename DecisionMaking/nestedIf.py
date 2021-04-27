# Nested If statements

i = 10
if (i == 10):
    #  First if statement
    if (i < 15):
        print ("i is smaller than 15")
    # Nested - if statement
    if (i < 12):
        print ("i is smaller than 12 too")
    else:
        print ("i is greater than 15")

a = 10
 
# Nested if to check whether a number is divisible by both 2 and 5
if a % 2 == 0:
    if a % 5 == 0:
        print("Number is divisible by both 2 and 5")