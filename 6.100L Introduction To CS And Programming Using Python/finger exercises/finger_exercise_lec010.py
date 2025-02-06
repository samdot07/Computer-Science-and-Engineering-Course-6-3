# Implement the function that meets the specifications below:
def all_true(n, Lf):
    ''' 
    - n is an int.
    - Lf is a list of functions that take in an int and return a Boolean.
    ---
    #### Return: 
        True if each and every function in Lf returns True when called 
        with n as a parameter. Otherwise returns False. 
    '''
    return all(f(n) for f in Lf)
    
# Examples: 
Lf = [lambda x: x%2 == 0, lambda y: y > 0]
print(all_true(5, Lf))