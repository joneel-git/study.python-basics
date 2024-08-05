# https://learnerspoint.org/blog/7-python-code-challenges-for-beginners

# 1. Converting Radians into Degrees
# What are radians and degrees they are different ways of messuring an angle.
# Radian = An angle made by unit Radius...
# 6.28 Rad = 2*(pi)

# I =   90   Deg (pi)/2 Rad
# II =  180  Deg (pi) Rad
# III = 270  Deg 3*(pi)/2 Rad
# IV =  360  Deg 0/2*(pi) Rad

import math as mathfunction

# Asking the user to input a deg number
_degrees_ = float(input("Enter a number in degrees.. "))

# Converting deg to rad (180 deg = pi(rad))
result = mathfunction.radians(_degrees_)

# Printing the number in Rad
print("The number in radians is: ", result)