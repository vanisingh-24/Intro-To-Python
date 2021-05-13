# Given a list of strings, find all palindromes.

my_list = ["geeks", "geeg", "keek", "practice", "aa"]

result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))

print(result)