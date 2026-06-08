def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not isinstance(x, (float, int)) and isinstance(y, (float, int)): #check if it is not number
        print ("-1") #print -1
        return -1 #return -1
    else:
        x,y = y,x #swap both values
        print ("x = ",x ) #print x
        print ("y =", y) #print y


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
swap("Apple", 10)
swap(9,17)


