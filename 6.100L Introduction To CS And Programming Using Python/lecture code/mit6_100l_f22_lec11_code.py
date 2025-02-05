#########################################
########### YOU TRY IT ##################
#########################################
# This one is similar to remove_elem from lec10 except that remove_elem 
# returns a new list and this one mutates the parameter L (and returns None)
def remove_all(L, e):
    ''' 
    - L is a list.
    ---
    Mutates L to remove all elements in L that are equal to e
    #### Returns: 
        None.
    '''
    # Looop: loop While 'e' is in the list 'L'
    while e in L:
        L.remove(e)
    

Lin = [1,2,2,2]
remove_all(Lin, 2)
print(Lin)    # prints [1]

Lin = [1,2,2,2]
remove_all(Lin, 1)
print(Lin)    # prints [2, 2, 2]

Lin = [1,2,2,2]
remove_all(Lin, 0)
print(Lin)    # prints [1, 2, 2, 2]

#########################################
################ AT HOME ################
#########################################
def repeat(L, n):
    ''' 
    - L is a list of ints.
    - n is a positive int.
    ---
    Mutates L to contain whatever elements L has right now repeated n times. 
    '''
    L_copy = L[:]
    
    # Loop: iterate over each number in range
    for i in range(n-1):
        L.extend(L_copy)
    
    return L
    
Lin = [1,2,3]
repeat(Lin, 3)
print(Lin)    # prints [1, 2, 3, 1, 2, 3, 1, 2, 3]