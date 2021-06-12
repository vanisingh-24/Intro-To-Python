# python program for finding summation of digit of number

li = [12,67,98,34]

res = []
for el in li:
  sum = 0
  for digit in str(el):
    sum += int(digit)
  res.append(sum)

print("List Integer Summation:" + str(res))