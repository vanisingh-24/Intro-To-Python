'''
https://codeforces.com/problemset/problem/791/A
Solution: Nothing fancy. Just run a loop till Limak's weight surpasses that of Bob's. Keep incrementing year in every
iteration. 
'''

def fun(w1, w2):
  years = 0
 
  while w1 <= w2:
    w1 *= 3
    w2 *= 2
    years += 1
 
  return years
 
if __name__ == "__main__":
  w1, w2 = map(int, input().split(' '))
  print(fun(w1, w2))