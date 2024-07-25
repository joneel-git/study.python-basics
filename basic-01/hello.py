# https://www.youtube.com/watch?v=W7luvtXeQTA

#  IF Block: Executes if the condition is True.
#  ELSE Block: Executes if the condition is False.

#       and = checks (TWO) or more conditions if True
#       or  = checks if at least (ONE) condition is True
#       not = Will change the result of a condition Not True = False

#   Here we are checking values of at least (TWO) using -----AND-------
# celsius
temp = 20

if temp > 0 and temp < 30:
    print("The temperature is ideal..")
else:
    print("The temperature is NOT ideal..!!")

#  Summary
#  Ideal Temperature Range: Between 0 and 30 degrees Celsius (exclusive).
#  Output if temp is within the range: "The temperature is ideal.."
#  Output if temp is outside the range: "The temperature is NOT ideal..!!"

#  The `and` operator checks if both conditions are TRUE; 
#  if any condition is FALSE, the whole expression is FALSE.
# ----------------------------------------------------------------------------

# Here we are checking if at least ONE condition is True  ----OR------
temp2 = -1
if temp2 <= 0 or temp2 >= 30:   
    print("The Temperature is BAD ", temp2)
else:
    print("The Temperature is GOOD.. ", temp2)

#  Summary
#  If temp2 is too cold (0 or less) or too hot (30 or more), it says "The Temperature is BAD."
#  If temp2 is just right (between 0 and 30), it says "The Temperature is GOOD."
#-----------------------------------------------------------------------------

# Here we are reversing value of True to False using ------NOT----- 
temp3 = 20
sunny = True
if not sunny:
    print("It is sunny outside..")
else:
    print("It is Cloudy wheather Outside let's stay inside..")
# Summary
# not sunny: The not operator flips the value of sunny. 
# If sunny is True, not sunny becomes False. If sunny is False, not sunny becomes True.