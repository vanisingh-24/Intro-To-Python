# Python program to Find the k most frequent words from data set in Python

from collections import Counter

data_set = "Welcome to the world of Geeks " \
"This portal has been created to provide well written well" \
"thought and well explained solutions for selected questions " \
"If you like Geeks for Geeks and would like to contribute " \
"here is your chance You can write article and mail your article " \
" to contribute at geeksforgeeks org See your article appearing on " \
"the Geeks for Geeks main page and help thousands of other Geeks. " \

words = data_set.split()

Counter = Counter(words)

most_occur = Counter.most_common(4)

print(most_occur)

