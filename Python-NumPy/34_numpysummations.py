# summations: difference: addition is done between 2 arguments whereas summation happens over n elements.
# adding the 2 array.
import numpy as np
vd1 = np.array([1,2,3])
vd2 = np.array([1,2,3])
vdnew = np.add(vd1, vd2)
print(vdnew)
# sum the values in 2 array:
import numpy as np
vd1 = np.array([1,2,3])
vd2 = np.array([1,2,3])
vdnew = np.sum([vd1, vd2])
print(vdnew)
# summation over an axis: if you specify axis=1, numpy will sum the number in each array.
import numpy as np
vd1 = np.array([1,2,3])
vd2 = np.array([1,2,3])
vdnew = np.sum([vd1, vd2], axis=1)
print(vdnew)
# cummulative sum: means partially adding thr element in array.
# example: [1,2,3,4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1,3,6,10] represent by cumsum()
import numpy as np
vd = np.array([1,2,3])
vdnew = np.cumsum(vd)
print(vdnew)