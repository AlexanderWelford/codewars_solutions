#Problem #1 

""" {Write a method, that will get an integer array as parameter and will process every number from this array.

Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

Example
[4,3,9,7,2,1] -> [2,9,3,49,4,1]
Notes
The input array will always contain only positive numbers, and will never be empty or null.} """

#Solution 
import numpy as np
def square_or_square_root(arr):
    return ([int(np.sqrt(i)) if np.sqrt(i).is_integer() else np.square(i) for i in arr])

#Test
print (square_or_square_root([1,2,3,4,5,6,7,8,9]))





