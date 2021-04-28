## While Loops
# SYNTAX - while expression:
#             statement(s)

count = 0
while(count < 3):
    count = count + 1
    print("Heelo World")

a = [1,2,3,4]
while a:
    print(a.pop())

# Single statement while block

count = 0
while (count < 5): count = count + 1; print("Hello Geeks")


## While-Else Loop

# Executed because no break 
i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("No Break")

# Not executed as there is a break 
i = 0 
while i < 4: 
    i += 1
    print(i) 
    break
else: 
    print("No Break")








