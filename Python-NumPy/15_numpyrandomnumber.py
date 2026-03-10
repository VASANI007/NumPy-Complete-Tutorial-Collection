# Random meaning - something that cannot be predicted logically.
# Now we will generate a random number from 0 to 100
from numpy import random 
vd = random.randint(100)
print(vd) 

# You can also genetrate float() via rand() from 0 to 1
from numpy import random 
vd = random.rand()
print(vd) 

# You can also generate random Array.
# we will generate a 1-D array containing 5 random int from 0 to 100:
from numpy import random 
vd = random.randint(100, size=(5))
print(vd) 

# You can also generate random Array.
# we will generate a 2-D array with 3 rows, each row  containing 5 random int from 0 to 100:
from numpy import random 
vd = random.randint(100, size=(3, 5))
print(vd) 

# You can also generate random Array.
# we will generate a 1-D array containing 5 random float:
from numpy import random 
vd = random.rand(5)
print(vd) 

# You can also generate random Array.
# we will generate a 2-D array with 3 rows, each containing 5 random float:
from numpy import random 
vd = random.rand(3, 5)
print(vd) 

# you can also generate random numbers from an array
# choice()

from numpy import random 
vd = random.choice([3,5,7,9,1,4,6])
print(vd) 

# you can also generate random numbers from an 2-D array
# choice()

from numpy import random 
vd = random.choice([3,5,7,9,1,4,6], size=(3,2,5))
print(vd) 
print("\n")

# ===============================
# NumPy Random Functions Demo
# ===============================
print("NumPy Random Functions Demo\n")
import numpy as np

# 1️⃣ seed() → same output पाने के लिए
np.random.seed(10)
print("Seed set to 10\n")

# 2️⃣ rand() → 0 से 1 के बीच random float values
print("rand():")
print(np.random.rand(5))     # 5 random float numbers
print()

# 3️⃣ randn() → Normal distribution (mean=0, std=1)
print("randn():")
print(np.random.randn(5))    # 5 random normal values
print()

# 4️⃣ randint() → random integers (low include, high exclude)
print("randint():")
print(np.random.randint(1, 10, 5))   # 1 to 9 ke beech 5 numbers
print()

# 5️⃣ random() → rand() jaisa hi
print("random():")
print(np.random.random(4))   # 4 random float values
print()

# 6️⃣ choice() → list/array se random value choose karna
print("choice() single value:")
print(np.random.choice([10, 20, 30, 40]))
print()

print("choice() multiple values:")
print(np.random.choice([1, 2, 3, 4], size=3))
print()

# 7️⃣ shuffle() → original array ko shuffle karta hai
a = np.array([1, 2, 3, 4, 5])
np.random.shuffle(a)
print("shuffle():")
print(a)     # original array change ho gaya
print()

# 8️⃣ permutation() → new shuffled array deta hai
b = np.array([10, 20, 30, 40])
print("permutation():")
print(np.random.permutation(b))   # original safe
print()

# 9️⃣ uniform() → given range me random float
print("uniform():")
print(np.random.uniform(10, 20, 5))   # 10 se 20 ke beech
print()

# 🔟 normal() → custom mean aur std deviation
print("normal():")
print(np.random.normal(50, 5, 6))   # mean=50, std=5
print()

# ===============================
# END OF PROGRAM
# ===============================
