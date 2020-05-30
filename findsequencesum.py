''' 
Given three integers i,j,k. A sequence sum is to be value of i + (i+1) + (i+2) +.. j + (j-1) + (j-2) + ...K. 
Increment from i until it equals j, then decrements j until its equal k. 
Given values of i,k,k find sum.  
eg i = 5, j = 9, k =6. sum is 56
'''


def getSequenceSum(i,j,k):
    result = 0
    for a in range (i,j+1):
        result += a
        a+1
    for b in range (k,j):
        result += b 
    
    return result

# Driver code  
if __name__ == "__main__" : 
    res = getSequenceSum(5,9,6)
    print(f"Sum is {res}" )