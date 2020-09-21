'''
Given an integer n, reverse digits in pairs.
if the number of digits is odd, last digit shoudl remain in the same position.
i/p = 123456 o/p = 214365
i/p = 72328 o/p = 27238
'''



def reverseDigitsInPairs(n):
    temp = str( n )
    final = ""
    substr = ""
    #print ("temp is {}".format(temp))
    i = 0
    for i in range( 0, len( temp ) - 1 ):
        #print( "sub is {}".format(sub ))
        if not i%2:
            substr = temp[i:i + 2]
            substr = substr[::-1]
            #print ("sub is {}".format(substr))
            final += substr
            substr = ""
    if len(final) < len(temp):
        final += temp[-1]
    return (int( str(final) ))

# Driver code  
if __name__ == "__main__" : 
    res = reverseDigitsInPairs(72328)
    print(f"Reversed String is {res}" )
