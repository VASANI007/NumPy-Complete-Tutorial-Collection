# spliting arrays in numpy- it is reverse to joining, breaking the array.
# array_split()

# split the array in 3 parts:
import numpy as np
vd = np.array([1,2,3,4,5,6])
print(np.array_split(vd, 3))

# now we will split this array in 4 parts
import numpy as np
vd = np.array([1,2,3,4,5,6])
vdnew = np.array_split(vd, 4)
print(vdnew)

# split into array with index

import numpy as np
vd = np.array([1,2,3,4,5,6])
vdnew = np.array_split(vd, 3)
print(vdnew[0])
print(vdnew[1])
print(vdnew[2])


# splitting the 2-D array
import numpy as np
vd = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]])
vdnew = np.array_split(vd, 3)
print(vdnew)

# split the 2-D array into three 2-D arrays
import numpy as np
vd = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
vdnew = np.array_split(vd, 3)
print(vdnew)

# spliting the 2-D into three 2-Dalong with rows
import numpy as np
vd = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
vdnew = np.array_split(vd, 3, axis=1)
print(vdnew)

#alternate solution is using the hsplit(), opposite hstack()
import numpy as np
vd = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
vdnew = np.hsplit(vd, 3)
print(vdnew)