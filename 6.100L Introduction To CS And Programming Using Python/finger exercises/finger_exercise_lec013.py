def sum_str_lengths(L):
    '''
    - L is a non-empty list containing either: 
        - string elements or 
        - a non-empty sublist of string elements.
    ---
    #### Returns: 
        sum of the length of all strings in L and lengths of 
        strings in the sublists of L.
    ---
    #### Note:
    If L contains an element that is not a string or a list, 
    or L's sublists contain an element that is not a string, 
    raise a ValueError.
    '''
    tot_len = 0
       
    # Iterate through the elements of L
    for i in L:
        if isinstance(i, str):
            tot_len += len(i)
        
        # Recursively call the function to handle nested sublists
        elif isinstance(i, list):
            tot_len += sum_str_lengths(i)
            
        else:
            raise ValueError(f'Invalid element {i}. Expected string or list.')
    
    return tot_len

# Examples:
print(sum_str_lengths(['abcd', ['e', 'fg']]))  # prints 7
print(sum_str_lengths([12, ['e', 'fg']]))      # raises ValueError
print(sum_str_lengths(['abcd', [3, 'fg']]))    # raises ValueError