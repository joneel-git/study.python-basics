# DataTypes 
# This is a variable with an integer dataType (INTEGER)
a=100
print(type(a))

# This is a variable containig plain text as data called (STRING)
b="secuence of characters"
print(type(b)) # Output class string

# This is how we do float values a number with a comma  (FLOAT)
c=1.2
print(type(c)) # Output class float

# We can also create complex values in a variable like this: (Complex)
d=100+3j
print(type(d)) # Output class complex

# We can also do whats called Boolean values which evaluates either to True or False like a light switch
# That can be either on or off.

isLightSwitchON = True
if isLightSwitchON:
    print("yes we have light...")
else:
    print("You have to turn on the light..")

print("---")
print(type(isLightSwitchON))


lightSwitchOff= False
if not lightSwitchOff:  # False switched to True
    print("The Lightswitch is On..") 
else:
    print("The lightSwitch is Off") 

# Summary in this scenario we have the lightswitch on this whole time...

# Operator	Logical Operation
# and	    Conjunction
# or	    Disjunction
# not	    Negation