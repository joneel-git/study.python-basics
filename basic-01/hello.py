# https://www.youtube.com/watch?v=H2EJuAcrZYU 3.39



x = True
y = False
z = True

# Here we are saying y is NOT true
print(not y)  # Output: True

# The 'and' keyword returns the second value only if the first value is True
print(x and y)  # Output: False (because y is False)

# The 'and' operator requires both values to be True to return True.
# If the first value is False, it returns the first value (False) 
# and doesn't evaluate the second value.

# The 'or' keyword returns the second value only if the first value is False
print(y or z)  # Output: True (because y is False, so it evaluates z)

# The 'or' operator returns the first value if it is True; 
# otherwise, it returns the second value.