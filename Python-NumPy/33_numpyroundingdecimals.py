# rounding decimals: there are 5 ways of rounding off the decimals in numpy: truncation, fix, rounding, floor, ceil.

# truncation: trunc() and fix()
# here we are truncating the below array, these command remove the decimals and return the float number closest to zero.
import numpy as np
vd = np.trunc([-3.1666, 3.6667])
print(vd)

# fix() example
import numpy as np
vd = np.fix([-3.1666, 3.6667])
print(vd)

# rounding: the around() function increments preceding digit or decimal by nearest to 1: if n>5 =1 or n<5 =0.
import numpy as np
vd = np.around(3.1666, 2)
print(vd)

# floor() - round off decimals to the lower integer.
import numpy as np
vd = np.floor([-3.1666, 3.6667])
print(vd)

# ceil(): round off decimals to the upper integer.
import numpy as np
vd = np.ceil([-3.1666, 3.6667])
print(vd)