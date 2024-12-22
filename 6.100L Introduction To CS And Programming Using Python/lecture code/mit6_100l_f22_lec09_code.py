############### YOU TRY IT #####################
# Write a function that meets these specifications:
def char_counts(s):
    ''' 
        - s is a string of lowercase chars.
    ---
    #### Returns: 
        tuple, where the first value is the number of 
        vowels in s and the second value is the number 
        of consonants in s.
    '''
    letters = 'aeiou'
    (con, vow) = (0, 0)
    
    for c in s:
        if c not in letters:
            con += 1
        
        else:
            vow += 1
    
    return(vow, con)

print(char_counts("abcd"))  # prints (1,3)
print(char_counts("zcght"))  # prints (0,5)

##################################################

def sum_and_prod(L):
    ''' 
        - L is a list of numbers.
    ---
    #### Return: 
        tuple, where the first value is the sum of all elements 
        in L and the second value is the product of all 
        elements in L.
    '''
    (sum, prod) = (0,1)
    
    for i in L:
        sum += i
        prod *= i
    
    return(sum, prod)

print(sum_and_prod([4,6,2,5]))   # prints (17, 240)

#############################################
################## AT HOME ####################
#############################################
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

##################################################

def sublist_sum(L):
    ''' 
    - L is a list whose elements are lists with int elements.
    ---
    #### Returns: 
        The sum of all int elements. 
    '''
    tot = 0
    
    for e in L:
        tot += sum(e)
    
    return tot

print(sublist_sum([[1,2], [4,5,6]])) # prints 18