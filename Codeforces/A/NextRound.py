'''
https://codeforces.com/problemset/problem/158/A
"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." - an excerpt from contest rules.
A total of n participants took part in the contest (n>=k), and you already know their scores. 
Calculate how many participants will advance to the next round
Input
The first line of the input contains two integers n and k separated by a single space.
The second line is the non-increasing score list
Output
Output the number of participants who advance to the next round.
'''

n , k = map(int,input().split())
a =list(map(int,input().split()))
count = 0
for i in range(0, n):
  if a[k-1] == 0 and a[i] == a[k-1]:
    count += 0
  elif a[k-1] <= a[i]:
    count += 1
  else:
    count += 0
print(count)