## labmda function 

# Cube using lambda
cube = lambda x: x*x*x
print(cube(3))

# List Comprehension using lambda
a = [(lambda x: x*2)(x) for x in range(5)]
print(a)




