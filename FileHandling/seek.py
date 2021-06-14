## Python seek() function
# SYNTAX - f.seek(offset, from_what), f is file pointer

f= open('gfg.txt', 'r')

f.seek(20)

# prints current position
print(f.tell())

print(f.readline())
f.close()

# negative offset works in binary mode only
f = open('gfg.txt', 'rb')

f.seek(-10, 2)

print(f.tell())
print(f.readline())
f.close()

# Python tell() function
# SYNTAX - file_object.tell()

f = open('file.txt', 'r')

print(f.tell())
f.close()

f = open('file.txt', 'r')
f.read(8)

print(f.tell())
f.close()

# position of handle before writing and after writing to binary file

f = open('file.txt', 'wb')
print(f.tell())

f.write(b'1010101')
print(f.tell())

f.close()