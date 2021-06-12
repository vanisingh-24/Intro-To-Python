## Reading a file in python 

# various ways to read the data from a file

file = open("data.txt","r+")

print(file.read())
file.seek(0)

print(file.readline())
file.seek(0)

print(file.readlines())
file.close()