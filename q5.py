def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not isinstance(num, (float, int)) and isinstance(num, (float, int)): #check if they are not numbers
        return False 
    if divisor == 0: #check if divisible by 0 to not cause that error
        return False
    if num % divisor == 0: #check the remainder to see if it is perfectly divisable
        return True
    else:
        return False
    


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print(check_divisibility(10, 2))
print(check_divisibility(7, 3))
