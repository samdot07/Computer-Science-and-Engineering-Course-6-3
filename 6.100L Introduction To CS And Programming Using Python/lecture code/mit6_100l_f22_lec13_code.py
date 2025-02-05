#########################################
########### YOU TRY IT ##################
#########################################
def pairwise_div(Lnum, Ldenom):
    ''' 
    - Lnum and Ldenom are non-empty lists of equal lengths containing numbers.
    ---
    #### Returns:
        a new list whose elements are the pairwise 
        division of an element in Lnum by an element in Ldenom. 
    ---
    #### Note:
    Raise a ValueError if Ldenom contains 0. 
    '''
    # challenge: write this with list comprehension!
    assert len(Lnum) == len(Ldenom), 'Lists are different lenghts'
    assert len(Lnum) != 0 and len(Ldenom) != 0, 'List is empty'
    
    if 0 in Ldenom:
        raise ValueError('Cannot devide by 0')
    
    # Loop: iterate over the elements in range
    return [Lnum[x] / Ldenom[x] for x in range(len(Lnum))]
        
# For example:
L1 = [4,5,6]
L2 = [1,2,3]    
print(pairwise_div(L1, L2))  # prints [4.0,2.5,2.0]

L1 = [4,5,6]
L2 = [1,0,3]    
print(pairwise_div(L1, L2))  # raises a ValueError

## to run after introducing assertions
L1 = [4,5,6,7,8]
L2 = [1,8,3]    
# print(pairwise_div(L1, L2))  # raises an AssertionError

L1 = []
L2 = []    
# print(pairwise_div(L1, L2))  # raises an AssertionError

#########################################
################ AT HOME ################
#########################################
def pairwise_div(Lnum, Ldenom):
    ''' 
    - Lnum and Ldenom are non-empty lists of equal lengths containing numbers.
    ---
    #### Returns:
        a new list whose elements are the pairwise 
        division of an element in Lnum by an element in Ldenom. 
    ---
    #### Note: 
    Raise a ValueError if L2 contains 0 or if the code can't 
    perform the division for some reason. 
    '''
    L= []
    
    assert len(Lnum) == len(Ldenom) and Lnum != 0, 'Lists are not of equal length or empty'
    
    # Loop: iterate over the elements of Lnum and Ldenom
    for x in range(len(Lnum)):
        try:
            L.append(Lnum[x] / Ldenom[x])
        
        except:
            raise ValueError('Cannot devide by 0')
    
    return L