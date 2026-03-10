# hyperbolic function: numpy provides the ufuncs line sinh(), cosh() and tanh() that takes values in radians and produce the corresponding sinh, cosh and tanh values.
# here we will find the value of sinh of pi/2
import numpy as np
vd = np.sinh(np.pi/2)
print(vd)

# we will now find cosh values in array
import numpy as np
vd = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
vdnew = np.cosh(vd)
print(vdnew)

# finding angles:
# here we can also find angles : arcsinh(), arccosh() and arctanh() that takes values in radians and produce the corresponding sinh, cosh and tanh values.
# we will now find the angle of 1.0
import numpy as np
vd = np.arcsinh(1.0)
print(vd)

# angles of each tanh values in an array:
import numpy as np
vd = np.array([0.1, 0.2, 0.5])
vdnew = np.arctanh(vd)
print(vdnew)