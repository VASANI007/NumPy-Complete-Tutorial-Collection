# reshaping - means changing the shape of an array ,like adding or removing the elements.

# reshaping from 1-D to 2-D
import numpy as np
vd = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
vd1 = vd.reshape(4, 3)
print(vd1)

# reshping from 1-D to 3-D
import numpy as np
vd = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
vd1 = vd.reshape(2, 3, 2)
print(vd1)

# Return copy or view
import numpy as np
vd = np.array([1,2,3,4,5,6,7,8])
print(vd.reshape(2, 4).base)

# unknown dimension - you are only allowed to have one unknown dimension. pass -1.

import numpy as np
vd = np.array([1,2,3,4,5,6,7,8])
vd1 = vd.reshape(2, 2, -1)
print(vd1)

# Flattening the array by converting multidimensional array in 1-D.
import numpy as np
vd = np.array([[1,2,3], [4,5,6]])
vd1 = vd.reshape(-1)
print(vd1)

# there are alot of functions for changing the shapes pf an array in numpy. like flatten, ravel and also rearranging the element rot90, flip,fliplr, flipud. they all are actually comes under advanced numpy.