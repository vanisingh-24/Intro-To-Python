# Python code to demonstrate length of list Performance Analysis

from operator import length_hint
import time

li = [1,2,3,4,5]

start_time_naive = time.time()
counter = 0
for i in li:
  counter = counter + 1
end_time_naive = str(time.time() - start_time_naive)

start_time_len = time.time()
list_len = len(li)
end_time_len = str(time.time() - start_time_len)

start_time_hint = time.time()
list_len_hint = length_hint(li)
end_time_hint = str(time.time() - start_time_hint)

print ("Time taken using naive method is : " + end_time_naive)
print ("Time taken using len() is : " + end_time_len)
print ("Time taken using length_hint() is : " + end_time_hint)



