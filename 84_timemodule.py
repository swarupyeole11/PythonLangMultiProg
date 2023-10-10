# The se module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time
# ‘conversions. This module is part of the Python Standard Library and is available n all Python installations, making it a convenient and essential
# tool for a wide range of applications. In this day 84 tutorial, we'l explore the time module in Python and see how it can be used in different scenarios.

import time 
import json


# the strf time is used to format the tome accordig to the need 
# the %character signifies different things and can be used to get he local time and all those stuff according to the format
localtime = time.localtime()
formatedlocaltime = time.strftime("%Y:%m:%d , %H:%m:%s",localtime)
print(formatedlocaltime)


#time.sleep() is used to stop the execution for a short period of time 

dicty = {1 : "Swarup", 2 : "Yeole", 3 : "Ahmednagar"}

val = json.dumps(dicty)

print(val)

for key,value in dicty.items() :
     time.sleep(0.5)
     dicty[key] += "x"

for x,y in dicty.items():
     print(x,y)


# the time.time() gives the current time in python in seconds since 1970 
print(time.time())