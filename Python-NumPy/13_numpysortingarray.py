# sort() - the numpy ndarray object has a function which is called sort(), and this will sort a specified array.
import numpy as np
vd = np.array([3,2,0,1])
vd1 = np.sort(vd)[::-1] # this method is like the sort() function and the [::-1] is used to reverse the sorted array.
vd2 = np.sort(vd) # this method is like the copy() and kind='mergesort' is used to specify the sorting algorithm to be used, in this case, it is the merge sort algorithm.
print(vd1)
print

# sort the array alphabetically
import numpy as np
vd = np.array(['banana', 'cherry', 'apple'])
print(np.sort(vd))

# sort the boolean array:
import numpy as np
vd = np.array([True, False, True])
print(np.sort(vd))

# sorting the 2-D array
import numpy as np
vd = np.array([[3,2,4], [5,0,1]])
print(np.sort(vd))