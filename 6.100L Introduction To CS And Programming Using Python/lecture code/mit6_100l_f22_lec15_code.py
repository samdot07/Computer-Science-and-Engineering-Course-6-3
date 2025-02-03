#########################################
########### YOU TRY IT ##################
#########################################
# Calculate n**p recursively by writing this function
def power_recur(n, p):
    if p == 0 :
        return 1
    
    elif p == 1 :
        return n
    
    # Recursive call: Multiply n by the result of n raised to the power of (p-1)
    return n * power_recur(n, p-1)
    
#########################################
################ AT HOME ################
#########################################
# Q1. Rewrite this to calculate b+b+b... a times
def mult(a, b):
    if b == 1:
        return a
    
    elif b == 0:
        return 0
    
    # Recursive call: Add a to the result of multiplying a by (b-1)
    return a + mult(a, b-1)
    
print(mult(5,4))

#########################################

# Q3. Calculate a+b recursively. Assume the only math operation
# you are allowed to do are adding and subtracting 1
def add(a, b):
    ''' 
    Uses recursion to calculate a+b as adding
    a to 1, b times. 
    '''
    if b == 0:
        return a
    
    # Recursive call: Add 1 to the result of adding a and (b-1)
    return 1 + add(a, b-1)
    
print(add(3,4))   # prints 7

#########################################

# Q4. Calculate a+b recursively by 1's. Assume the only math operation
# you are allowed to do are adding and subtracting 1
def add_by_ones(a, b):
    ''' 
    Uses recursion to calculate a+b as adding
    1, a times then adding 1, b times. 
    '''
    if b == 0:
        return a
    
    elif a == 0:
        return b
    
    # Recursive call: Add 1 to b-1, and then add a-1 to 1
    return add(1, b-1) + add(a-1, 1)

print(add_by_ones(3,4))   # prints 7