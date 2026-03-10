# finding GCD(Gretest common denominator), also known as HCF(Highest Common Factor)

# here wew will find the HCF of the below 2 numbers:
import numpy as np
vd1 = 6
vd2 = 9
vdnew = np.gcd(vd1, vd2)
print(vdnew) # answer will be 3 because that is the highest number  and both umber can be divided by (6/3=2 and 9/3=3)

# finding the GCD in an array
# the reduce() method will use the ufunc, in this case the gcd() function on each elemtn and it will reduce the array by 1 dimension.
import numpy as np
vd = np.array([20,8,32,16,36])
vdnew = np.gcd.reduce(vd)
print(vdnew)
# it will return 4 because 4 is the highest number of all values that can be divided in between array.