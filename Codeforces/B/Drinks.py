'''
http://codeforces.com/problemset/problem/200/B
Solution: Important is to accept inputs in float. Add all the percentages as fractions to a total. Divide it with
the number of drinks. Also, take care to have 12 places of decimals in the answer. Use format for it.
'''

def solve(n,p):
    total_sum = 0
    
    for i in p:
 
        total_sum += i
    
    return "{0:.12f}".format((total_sum/n))
 
 
 
if __name__ == "__main__":
 
    n = float(input())
    p = map(float, input().split(" "))
 
    print (solve(n,p))