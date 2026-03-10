# data types in python: string, integer, float, boolean, complex
# data type in numpy 
# i for integer
# b for boolean
# u for unsigned integer
# f for float
# c for complex float
# m for timedelta
# M for datetime
# O for object
# S for string
# U for unicode string
# V - memory

# checking the data type of numpy array -dtype
import numpy as np
vd = np.array([1, 2, 3, 4])
print(vd.dtype)

# checking the data type of numpy array - string

import numpy as np
vd = np.array(['apple', 'banana', 'cherry'])
print(vd.dtype)

# creating array with a defined data type:

import numpy as np
vd = np.array([1, 2, 3, 4], dtype='S')
print(vd)
print(vd.dtype)

# now we will create an array with data type of 4 byte int:
import numpy as np
vd = np.array([1, 2, 3, 4], dtype='i4')
print(vd)
print(vd.dtype)

# if a type is given in which the elements cannot be casted then numpy will raise error. what if a value cannot be converted?

'''import numpy as np
vd = np.array(['a', '2', '3'], dtype='i')
print(vd.dtype)'''

#Converting data type in existing array - astype()
import numpy as np
vd = np.array([1.1, 2.1, 3.1, 4.1])
vd1 = vd.astype('i')
print(vd1)
print(vd1.dtype)

#Converting data type from integer to boolean
import numpy as np
vd = np.array([1, 0, 3])
vd1 = vd.astype(bool)
print(vd1)
print(vd1.dtype)
