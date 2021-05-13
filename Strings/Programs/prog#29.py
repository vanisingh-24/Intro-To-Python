# Given a list of numbers, find all numbers divisible by 13.

my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]

result = list(filter(lambda x : (x%13 == 0), my_list))

print(result)