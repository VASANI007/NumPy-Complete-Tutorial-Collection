# products: use prod() function.
# here we will find the product of the element of the below array:
import numpy as np
vd = np.array([1,2,3,4]) # 1*2*3*4 = 24
vdnew = np.prod(vd)
print(vdnew)

# here we will find the product of elemets in 2 different array:
import numpy as np
vd1 = np.array([1,2,3,4])
vd2 = np.array([5,6,7,8])
vdnew = np.prod([vd1, vd2]) # 1*2*3*4*5*6*7*8 = 40320
print(vdnew)

# product over an axis
import numpy as np
vd1 = np.array([1,2,3,4])
vd2 = np.array([5,6,7,8])
vdnew = np.prod([vd1, vd2], axis=1) 
print(vdnew)

# cummulative product:
# example  the partial product of [1,2,3,4] is [1,1*2,1*2*3,1*2*3*4] = [1,2,6,24] represented by cumprod().
import numpy as np
vd = np.array([5,6,7,8])
vdnew = np.cumprod(vd)
print(vdnew)