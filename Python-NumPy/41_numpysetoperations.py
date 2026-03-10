# what is set? : a set is a collection of unique elements

# for creating the set we use numpy's unique() method to find the unique elements from any array:
# here we will convert the array with repeted elements to a set
import numpy as np
vd = np.array([1,1,1,2,3,4,5,5,6,7])
vdnew = np.unique(vd)
print(vdnew)

# to find the unique values of 2 1D array, we will use union1d() method
import numpy as np
vd1 = np.array([1,2,3,4])
vd2 = np.array([3,4,5,6])
vdnew = np.union1d(vd1, vd2)
print(vdnew)

# to find the only values tat are present in both array, we will use intersect1d() method.
import numpy as np
vd1 = np.array([1,2,3,4])
vd2 = np.array([3,4,5,6])
vdnew = np.intersect1d(vd1, vd2, assume_unique=True)
print(vdnew)

# to find the only values that are in 1st set and NOT present in the 2nd set: use setfdiff1d()
import numpy as np
vd1 = np.array([1,2,3,4])
vd2 = np.array([3,4,5,6])
vdnew = np.setdiff1d(vd1, vd2, assume_unique=True)
print(vdnew)

# to find the only values that are NOT present in BOTH the sets, use setxor1d() method:
import numpy as np
vd1 = np.array([1,2,3,4])
vd2 = np.array([3,4,5,6])
vdnew = np.setxor1d(vd1, vd2, assume_unique=True)
print(vdnew)