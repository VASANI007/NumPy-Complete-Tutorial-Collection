# arithemtic operators: +, -, / , *
# by using ufunc additional arguments like, where, dtype and out.
# here now we will use add()
import numpy as np
vd = np.array([10,11,12,13,14,15])
vd2 = np.array([20,21,22,23,24,25])
print(np.add(vd, vd2))
#  example of substracting the value
import numpy as np
vd = np.array([10,11,12,13,14,15])
vd2 = np.array([20,21,22,23,24,25])
vdnew = np.subtract(vd, vd2)
print(vdnew)

# example of multipication
import numpy as np
vd = np.array([10,11,12,13,14,15])
vd2 = np.array([20,21,22,23,24,25])
vdnew = np.multiply(vd, vd2)
print(vdnew)

# example of divide()
import numpy as np
vd = np.array([10,11,12,13,14,15])
vd2 = np.array([20,21,22,23,24,25])
vdnew = np.divide(vd, vd2)
print(vdnew)

# power() function raises the value from the 1st array to the power of the values of the 2nd array and return the results in a new array.

import numpy as np
vd = np.array([10,20,30,40,50,60])
vd2 = np.array([3,5,6,8,2,33])
vdnew = np.power(vd, vd2)
print(vdnew)

# reminder- mod() and reminder() fucntions return the reminder of the 1st array corrosponding to the 2nd array, and result in the new array.
import numpy as np
vd = np.array([10,20,30,40,50,60])
vd2 = np.array([3,7,9,8,2,33])
vdnew = np.mod(vd, vd2)
print(vdnew)

# by using reminder()
import numpy as np
vd = np.array([10,20,30,40,50,60])
vd2 = np.array([3,7,9,8,2,33])
vdnew = np.remainder(vd, vd2)
print(vdnew)

# quotient and mod(reminder)
# the divmod() function return both the quotient and mod.
import numpy as np
vd = np.array([10,20,30,40,50,60])
vd2 = np.array([3,7,9,8,2,33])
vdnew = np.divmod(vd, vd2)
print(vdnew)

# absolute() and abs()- do the same operation but here we should use absolute() to avoid confusion with python inbuilt function math.abs().
import numpy as np
vd = np.array([-1,-2,-3,-4,-5])
vdnew = np.absolute(vd)
print(vdnew) 
