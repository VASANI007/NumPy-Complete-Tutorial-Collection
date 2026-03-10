# difference between numpy array copy and view.
# we will make a copy, change in original array, and display both.

import numpy as np
vd = np.array([1,2,3,4,5,6])
v = vd.copy()
v[0] = 12
print(vd)
print(v)

# now we will make a view, change original, display both

import numpy as np
vd = np.array([1,2,3,4,5])
v = vd.view()
v[0] = 31
print(vd)
print(v)
