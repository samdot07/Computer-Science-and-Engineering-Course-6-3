def flatten(L):
    ''' 
    - L: a list 
    ---
    #### Returns:
        a copy of L, which is a flattened version of L 
    '''
    if not L:
        return []
    
    if isinstance(L[0], list):
        # Recursion: flatten the first list and the rest of the list
        return flatten(L[0]) + flatten(L[1:])
    
    # Recursion: return the first element and flatten the rest
    return [L[0]] + flatten(L[1:])

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]