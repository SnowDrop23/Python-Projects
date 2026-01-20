#------------- Question-------------
# Create a python program capable of greeting you
# with Good morning, Good afternoon, Good evening, Good night. 
# Your program should use the time module to get the current hour

import time

current_hour = int(time.strftime("%H"))

if 5 <= current_hour < 12 :
    print("Good Morning!")

elif 12 <= current_hour < 17 :
    print("Good Afternoon!")

elif 17 <= current_hour <= 21 :
    print("Good Evening!")

else :
    print("Good night")
