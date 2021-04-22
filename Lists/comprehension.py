## List Comprehension
# SYNTAX - newList = [ expression(element) for element in oldList if condition ]

#square of all odd numbers from range 1 to 10 
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print (odd_square)




