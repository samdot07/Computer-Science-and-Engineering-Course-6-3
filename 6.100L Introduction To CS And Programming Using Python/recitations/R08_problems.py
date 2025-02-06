# RECURSSION PRACTICE
# Problem 1: Write a recursive program to calculate the sum of the positive 
# integers of n+(n-2)+(n-4)... (until and not including n-x =< 0)
def sum_series(n):
    '''
    - n: int.
    ---
    #### Return:
        int, sum of the positive integers of n+(n-2)+(n-4)... 
        (until and not including n-x =< 0).
    '''
    if n <= 0:
        return 0
    
    # Recursion: call the function with (n-2) and add to the current n
    return n + sum_series(n-2)

# testing
print(sum_series(6))  # 12 
print(sum_series(10))  # 30 
print(sum_series(5))  # 9   

#########################################
# Problem 2: Write a recursive program to calculate the value of 'a' to the power 'b'
def power(a, b):
    '''
    - a: int.
    - b: int.
    ---
    #### Return:
        int, value of 'a' to the power 'b'.
    '''
    if b == 0:
        return 1
    
    # Recursion: call the function with (b-1) and multiply the result by a
    return a * power(a, b-1)

# testing
print(power(4, 3))  # 64
print(power(3, 4))  # 81

#########################################
# Problem 3: Write a recursive program to calculate the sum of a list of numbers.
def list_sum(num_List):
    '''
    - num_List: list, list of numbers.
    ---
    #### Return:
        int, sum of a list of numbers.
    '''
    if not num_List:
        return 0
    
    # Recursion: call the function with the rest of the list (num_List[1:])
    return num_List[0] + list_sum(num_List[1:])
    
# testing 
print(list_sum([2, 4, 5, 6, 7]))  # expect 24

#########################################
# Problem 4: Write a recurssive program to calculate the nth harmonic number
def harmonic(n):
    '''
    - n: int.
    ---
    #### Return:
        int, the nth harmonic number.
    '''
    if n == 1:
        return n
    
    # Recursion: add the inverse of n to the harmonic value of (n-1)
    return 1/n + harmonic(n-1)

print(harmonic(3)) # expect 1.83333333333
print(harmonic(5)) # expect 2.28333333333

#########################################
# Extra - Problem 5: Write a recursive program to find the greatest common divisor (gcd) 
# of two integers. 
def gcd(a, b):
    '''
    - a: int.
    - b: int.
    ---
    #### Return:
        int, greatest common divisor (gcd) between 'a' and 'b'.
    '''
    if b == 0:
        return a
    
    # Recursion: call the function with (b, a % b) to calculate the GCD
    return gcd(b, a % b)

# testing   
print(gcd(5, 4))  # 1 
print(gcd(15, 12))  # 3
print(gcd(12, 12))  # 12