# Joining the numpy array - here for this we will pass concatenate()

import numpy as np
vd = np.array([1,2,3])
vd1 = np.array([4,5,6])
vd2 = np.concatenate((vd, vd1))
print(vd2)

# Joining of 2-D arrays along with rows(axis = 1)
import numpy as np
vd = np.array([[1,2],[3,4]])
vd1 = np.array([[5,6], [7,8]])
vd2 = np.concatenate((vd, vd1), axis=1)
print(vd2)

# Joining array using the stack function:
import numpy as np
vd = np.array([1,2,3])
vd1 = np.array([4,5,6])
vd2 = np.stack((vd, vd1), axis=1)
print(vd2)

# Stacking along with rows: hstack()
import numpy as np
vd = np.array([1,2,3])
vd1 = np.array([4,5,6])
vd2 = np.hstack((vd, vd1))
print(vd2)

# Stacking along with column
import numpy as np
vd = np.array([1,2,3])
vd1 = np.array([4,5,6])
vd2 = np.vstack((vd, vd1))
print(vd2)

# Stacking along with height(depth)
# import numpy as np
vd = np.array([1,2,3])
vd1 = np.array([4,5,6])
vd2 = np.dstack((vd, vd1))
print(vd2)