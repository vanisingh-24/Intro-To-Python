# Defining strings
var1 = "Hello "
var2 = "World"
  
##Concatenation of Strings 

# 1. Using + Operator 
var3 = var1 + var2
print(var3)

# 2. Using join() method 
print("".join([var1, var2]))
  
var3 = " ".join([var1, var2])
  
print(var3)

list1 = ['1','2','3','4']  
s = "-"
s = s.join(list1)
print(s)

list1 = ['g','e','e','k', 's'] 
print("".join(list1))

# 3. Using % Operator
print("% s % s" % (var1, var2))

# 4. Using format() function 
print("{} {}".format(var1, var2))

var3 = "{} {}".format(var1, var2)
  
print(var3)