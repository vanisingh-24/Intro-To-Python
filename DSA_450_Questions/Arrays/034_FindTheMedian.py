## Given an array arr[] of N integers, calculate the median

def find_median(self, v):
	    x = len(v)
        v.sort()
 
        if x%2==1 :
            return v[x//2]
        else :
            return ((v[(x-1)//2]+v[x//2])//2)