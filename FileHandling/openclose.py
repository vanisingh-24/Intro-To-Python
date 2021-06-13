## Opening a File

file1 = open('file.txt', 'r')

file2 = open(r"D:\Text\MyFile2.txt", "r+")

## Closing the file

file1 = open('file.txt', 'a')
file1.close()

## split() using file handling

with open('file.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)


