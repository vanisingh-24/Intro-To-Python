# Python Program for compound interest

def compoundInterest(p,r,t):
   amount = p* (pow((1+r/100), t))
   CI = amount - p
   print(CI)

# Driver Code
compoundInterest(10000, 10.25, 5)