

def my_function(x):
    return x[5:] # -1 Reversing backwards :wheretostart :wheretoend [start:end] or [start:end:steps]

mytxt = my_function("Hello World")

print(mytxt)

# a[5:]          # Skipps first 5 output World not Hello
# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
#   0   1   2   3   4   5
#  -6  -5  -4  -3  -2  -1