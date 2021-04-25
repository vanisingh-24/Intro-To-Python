## String Interpolation

#1 %-formatting

n1 = 'Hello'
n2 ='GeeksforGeeks'

print("%s ! This is %s."%(n1,n2))

variable = '15'
variable = int(variable)

string = "Variable as integer = %d" %(variable)
print(string)

# printing as any string or char after a mark 

print ("Variable as printing with special char = %cmayank" %(variable)
print(string)

#2 str.format()

n1 = 'Hello'
n2 ='GeeksforGeeks'

# for single substitution
print('Hello, {}'.format(n1))
  
# b1 and b2 are formal parameters 
# n1 and n2 are actual parameters
print("{b1}! This is {b2}.".format(b1 = n1, b2 = n2))
  
# else both can be same too
print("{n1}! This is {n2}.".format(n2 = n2, n1 = n1))

# formatting a string using a numeric constant
print("Hello! I am {} years old".format(19))

# Positional arguments
print("{1} love {0}!!".format("GeeksforGeeks","Geeks"))

# Keyword arguments
print("{gfg} is a {0} science portal for {1}".format("computer", "geeks", gfg ="GeeksforGeeks"))

# Convert base-10 decimal integers to floating point numeric constants
print ("This site is {0:f}% securely {1}!!".format(100, "encrypted"))

# To limit the precision
print("My average of this {0} was {1:.2f}".format("semester", 78.234876))

# For no decimal places
print ("My average of this {0} was {1:.0f}%".format("semester", 78.234876))

# Convert an integer to its binary orwith other different converted bases.
print("The {0} of 100 is {1:b}".format("binary", 100))
         
print("The {0} of 100 is {1:o}".format("octal", 100))

# To demonstrate spacing whenstrings are passed as parameters
print("{0:4}, is the computer science portal for {1:8}!".format("GeeksforGeeks", "geeks"))
 
# To demonstrate spacing when numeric constants are passed as parameters.
print("It is {0:5} degrees outside !".format(40))
 
# To demonstrate both string and numeric constants passed as parameters
print("{0:4} was founded in {1:16}!".format("GeeksforGeeks", 2009))
 
# To demonstrate aligning of spaces
print("{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009))
 
print("{:*^20s}".format("Geeks"))

#3 f-strings

n1 = 'Hello'
n2 ='GeeksforGeeks'
  
print(f"{n1}! This is {n2}")
  
print(f"(2 * 3)-10 = {(2 * 3)-10}")

# Printing today's date
import datetime
today = datetime.datetime.today()
print(f"{today is: %B %d, %Y}")

#4 String Template Class

from string import Template

n1 = 'Hello'
n2 ='GeeksforGeeks'

n = Template('$n3 ! This is $n4')

print(n.substitute(n3 = n1, n4= n2))

#  import names and marks of students from a list and print them using template.
# substitute method

from string import Template

Student = [('Ram',90), ('Ankit',78), ('Bob',92)]

t = Template('Hi $name , you have got $marks marks')

for i in Student:
    print(t.substitute(name = i[0],marks= i[1]))

# safe_substitute method

from string import Template

t = Template('$name is the $job of $company')

string = template.safe_substitute(name='Steve',job='TCS')
print(string)

# Printing the template String

t = Template('I am $name from $city')
print('Template String =', t.template)

# Escaping $ Sign


template = Template('$$ is the symbol for $name')
string = template.substitute(name='Dollar')
print(string)

# The ${Identifier}

template = Template( 'That $noun looks ${noun}y')
string = template.substitute(noun='Fish')
print(string)

