## With statement
# SYNTAX - with open filename as file

# # write data to a file using with statement

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

with open("file.txt", "w") as file1:
    file1.write("Hello \n")
    file1.writelines(L)

with open("file.txt", "r") as file1:
    print(file1.read())

# Using with statement with user defined objects

class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self):
        self.file.close()

with MessageWriter('my_file.txt') as xfile:
    xfile.write('Helloooooo')

# The contextlib module

from contextlib import contextmanager

class messageWriter(object):
    def __init__(self, filename):
        self.file_name = filename

    def open_file(self):
        try:
            file = open(self.file_name, 'w')
            yield file
        finally:
            file.close()

message_writer = MessageWriter('hello.txt')
with message_writer.open_file() as xfile:
    xfile.write('Helloooooo')