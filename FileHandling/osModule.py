## OS Module

# Get the current working directory (CWD)

import os

cwd = os.getcwd()

print("Location of current working directory",cwd)

# Changing the CWD

import os

def currentPath():
  print(os.getcwd())
  print()

currentPath()

os.chdir('../')

currentPath()

# Creating a directory

# Using mkdir
import os

directory = "geeksforgeeks"

parent_dir = "D:/pycharm projects/"

path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)

directory = "geeks"

parent_dir = "D:/Pycharm projects"

mode = 0o666

path = os.path.join(parent_dir, directory)

os.mkdir(path, mode)
print("Directory '% s' created" % directory)

# Using makedirs()
import os

directory = "Vani"

parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"

path = os.path.join(parent_dir, directory)

os.makedirs(path)
print("Directory '% s' created" % directory)

# Listing out Files and Directories with Python

import os

path = "/"
dir_list = os.listdir(path)

print(dir_list)

# Deleting Directory or Files using Python

# Using os.remove()
import os

file = 'file1.txt'

location = "D:/Pycharm projects/GeeksforGeeks/Authors/Vani/"

path = os.path.join(location, file)

os.remove(path)

# Using os.rmdir()

import os

directory = "geeks"

parent = "D:/Pycharm projects/"

path = os.path.join(parent, directory)

os.rmdir(path)

# Commonly Used Functions

# 1. os.name
import os
print(os.name)

# 2. os.error
import os

try:
  filename = 'gfg.txt'
  f = open(filename,'rU')
  text = f.read()
  f.close()

except IOError:
  print('Problem reading: ' + filename)

# 3. os.popen()
# SYNTAX - os.popen(command[, mode[, bufsize]])

import os
fd = "GFG.txt"
 
# popen() is similar to open() and provides a pipe/gateway and accesses the file directly
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

file = os.popen(fd, 'w')
file.write("Hello")

# 4. os.close()
import os
fd = 'gfg.txt'
file = open('fd, 'r)
text = file.read()
print(text)
os.close(file)

# 5. os.rename()

import os

fd = 'gfg.txt'
os.rename(fd,'New.txt')
os.rename(fd,'New.txt')

# 6. os.remove()
import os
os.remove('file.txt')

# 7. os.path.exists()

import os

result = os.path.exists('file_name')
print(result)

# 8. os.path.getsize()
import os

size = os.path.getsize('filename')
print("Size of the file is", size," bytes.")

