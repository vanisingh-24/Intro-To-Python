# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

def swap(list, pos1, pos2):

  list[pos1], list[pos2] = list[pos2], list[pos1]

  return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3

print(swap(list, pos1, pos2))
