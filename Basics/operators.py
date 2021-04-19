# Arithmetic Operator 
a = 9
b = 4
   
# Addition of numbers 
add = a + b 
# Subtraction of numbers  
sub = a - b 
# Multiplication of number  
mul = a * b 
# Division(float) of number  
div1 = a / b 
# Division(floor) of number  
div2 = a // b 
# Modulo of both number 
mod = a % b 
   
# print results 
print(add) 
print(sub) 
print(mul) 
print(div1) 
print(div2) 
print(mod)


#Relational Operators 
a = 13
b = 33
   
# a > b is False 
print(a > b) 
   
# a < b is True 
print(a < b) 
   
# a == b is False 
print(a == b) 
   
# a != b is True 
print(a != b) 
   
# a >= b is False 
print(a >= b) 
   
# a <= b is True 
print(a <= b)


# Logical Operator 
a = True
b = False
   
# Print a and b is False 
print(a and b) 
   
# Print a or b is True 
print(a or b) 
   
# Print not a is False 
print(not a)


# Bitwise operators 
a = 10
b = 4
   
# Print bitwise AND operation   
print(a & b) 
   
# Print bitwise OR operation 
print(a | b) 
   
# Print bitwise NOT operation  
print(~a) 
   
# print bitwise XOR operation  
print(a ^ b) 
   
# print bitwise right shift operation  
print(a >> 2) 
   
# print bitwise left shift operation  
print(a << 2)


# Membership operator
x = 'Geeks for Geeks'
y = {3:'a',4:'b'}
  
  
print('G' in x)
  
print('geeks' not in x)
  
print('Geeks' not in x)
  
print(3 in y)
  
print('b' in y)

# Identity operators
a1 = 3
b1 = 3
a2 = 'GeeksforGeeks'
b2 = 'GeeksforGeeks'
a3 = [1,2,3]
b3 = [1,2,3]
  
print(a1 is not b1)
  
print(a2 is b2)
  
# Output is False, since lists are mutable.
print(a3 is b3)

