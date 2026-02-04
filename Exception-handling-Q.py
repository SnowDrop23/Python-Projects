# Suppose user have to enter integer value between 5 and 9 and if it enters 'quit', the program will also run, not other than any string.
# Now write such program 

a = (input("enter any value between 5 and 9: "))

try:
    if(a == "quit") :
        print("Quit the program")
    else:
        if(a < '5' or a > '9'):
            raise ValueError('"Value should be between 5 and 9"')  
        print("Value accepted")
except ValueError as e:
    print("Error:", e)
