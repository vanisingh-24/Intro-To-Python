# Given a list of integers, the task is to find N largest elements assuming size of list is greater than or equal o N.

def nlargest(list, n):
  final = []

  for i in range(0, n):
    max = 0

    for j in range(len(list)):
      if(list[j]>max):
        max = list[j]

    list.remove(max)
    final.append(max)

  print(final)

# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2
nlargest(list1, N)

