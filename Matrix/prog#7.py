## Get Kth column of matrix

# Using list comprehension
test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]

print(test_list)

K = 2

res = [sub[K] for sub in test_list]
print("The Kth column of matrix is : " + str(res))

# Using zip()
test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
  
print("The original list is : " + str(test_list))
  
K = 2
res = list(zip(*test_list)[K])
  
print("The Kth column of matrix is : " + str(res))



