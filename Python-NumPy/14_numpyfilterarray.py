# Getting some elements out of an existing array and creating a new array is called filtering.
# A boolean index list is a list ofboolean corresponding to indexes in the array. (True and False)
# create an array from the element on index 0 to 2:
import numpy as np
vd = np.array([41,42,43,44])
vd1 = [True, False, True, False]
finalvd = vd[vd1]
print(finalvd)

# now we will create a filter array
# that will return only values higher than 42.
import numpy as np
vd = np.array([41,42,43,44])
emptyvd = []
for element in vd:
    if element > 42:
        emptyvd.append(True)
    else:
        emptyvd.append(False)
vdnew = vd[emptyvd]
print(emptyvd)
print(vdnew)

# Create a filter array that will return only even elements from the original array.
import numpy as np
vd = np.array([1,2,3,4,5,6,7])
vdempty = []
for i in vd:
    if i%2 == 0:
        vdempty.append(True)
    else:
        vdempty.append(False)
vdnew = vd[vdempty]
print(vdempty)
print(vdnew)

# Yes, you can also create filter directly from array
# that will return only values higher than 42.
import numpy as np
vd = np.array([41,42,43,44])
vdempty = vd > 42
vdnew = vd[vdempty]
print(vdempty)
print(vdnew)

# Yes, you can also create filter directly from array
# Create a filter array that will return only even elements from the original array.
import numpy as np
vd = np.array([1,2,3,4,5,6,7])
vdempty = vd % 2 == 0
vdnew = vd[vdempty]
print(vdempty)
print(vdnew)