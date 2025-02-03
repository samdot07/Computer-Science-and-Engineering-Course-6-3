#########################################
########### YOU TRY IT ##################
#########################################
# Fix this buggy code so it works according to the specification:
def is_triangular(n):
    ''' 
    - n is an int > 0.
    ---
    #### Returns:
        True if n is triangular, i.e. equals a continued
        summation of natural numbers (1+2+3+...+k) .
    '''
    total = 0
    
    # Iterate over all numbers from 0 to n+1
    for i in range(n+1):
        total += i
        if total == n:
            return True
    
    return False

# start by runing it on simple test cases
print(is_triangular(4))  # print False
print(is_triangular(6))  # print True
print(is_triangular(1))  # print True

#########################################

def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x ** 3
    guess = (high+low) / 2
    
    # Loop until guess is within epsilon
    while (guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        
        else:
            high = guess
        
        guess = (high+low) / 2
    
    return guess

print(bisection_root(4))
print(bisection_root(123))

def count_nums_with_sqrt_close_to(n, epsilon):
    ''' 
    - n is an int > 2.
    - epsilon is a positive number < 1.
    ---
    #### Returns: 
        How many integers have a square root within epsilon of n.
        '''
    count = 0
    
    # Iterate over all numbers from 0 to n^3
    for i in range(n**3):
        sqrt = bisection_root(i)
        if abs(n - sqrt) < epsilon:
            count += 1
            print(i ,sqrt)
    
    return count

print(count_nums_with_sqrt_close_to(10, 0.1))

#########################################

def apply(criteria,n):
    ''' 
    - criteria is a function that takes in a number and returns a Boolean.
    - n is an int.
    ---
    #### Returns:
        How many ints from 0 to n (inclusive) match the criteria 
        (i.e. return True when criteria is applied to them).
    ''' 
    count = 0
    
    # Iterate over all numbers from 0 to n+1
    for i in range(n+1):
        if criteria(i):
            count +=1
    
    return count

def is_even(x):
    return x%2==0

how_many = apply(is_even,10)
print(how_many)

#########################################

def max_of_both(n, f1, f2):
    ''' 
    - n is an int.
    - f1 and f2 are functions that take in an int and return a float.
    --- 
    #### Returns: 
        The maximum value of all these results.
    ---
    #### Note:
    Applies f1 and f2 on all numbers between 0 and n (inclusive).
    '''
    return max(n, f1(n), f2(n))

print(max_of_both(2, lambda x:x-1, lambda x:x+1))  # prints 3
print(max_of_both(10, lambda x:x*2, lambda x:x/2))  # prints 20

#########################################
################ AT HOME ################
#########################################
def is_palindrome(s):
    ''' 
    - s is a string.
    ---
    #### Returns:
        True if s is a palnidrome and False otherwise. 
    ---   
    #### Note:
    A palindrome is a string that contains the same 
    sequence of characters forward and backward.
    '''
    return s[::] == s[::-1]

# For example:
print(is_palindrome("222"))   # prints True
print(is_palindrome("2222"))   # prints True
print(is_palindrome("abc"))   # prints False

#########################################

def f_yields_palindrome(n, f):
    ''' 
    - n is a positive int.
    - f is a function that takes in an int and returns an int.
    #### Returns:
    True if applying f on n returns a number that is a
    palindrome and False otherwise.  
    '''
    return is_palindrome(str(f(n)))

# For example:
def f(x):
    return x+1

def g(x):
    return x*2

def h(x):
    return x//2

print(f_yields_palindrome(2, f))   # prints True
print(f_yields_palindrome(76, f))   # prints True
print(f_yields_palindrome(11, g))   # prints True
print(f_yields_palindrome(123, h))   # prints False