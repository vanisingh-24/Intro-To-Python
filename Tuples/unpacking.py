## unpacking of tuples

a = ("MNNIT Allahabad", 5000, "Engineering") 
 
# this lines UNPACKS values 
(college,student,type_ofcollege) = a 
print(college)
print(student)
print(type_ofcollege)

## unpacking tuple using *

# remaining will be assined to y
x, *y, z = (10, "Geeks ", " for ", "Geeks ", 50)

print(x)
print(y)
print(z)

## unpacking tuple using function

def result(x,y):
    return x*y
print(result(10,100))

z = (10,100)
print(result(*z))



