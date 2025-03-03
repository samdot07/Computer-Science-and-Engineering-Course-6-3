def keys_with_value(aDict, target):
    '''
    - aDict: a dictionary.
    - target: an integer or string.
    ---
    #### return: 
        Sorted list of the keys in aDict with the value target.
    ---
    #### Note:
        Assume that keys and values in aDict are integers or strings.
        If aDict does not contain the value target, return an empty list.
    '''
    # Loop: iterate over all (k, v) pairs in the dictionary
    return sorted([k for k, v in aDict.items() if v == target])

# Examples:
aDict = {1:2, 2:4, 5:2}
target = 2   
print(keys_with_value(aDict, target)) # prints the list [1,5]

def all_positive(d):
    '''
    - d is a dictionary that maps int:list.
    ---
    #### return: 
        Sorted list of all k whose v elements sums up to a positive value.
    ---
    #### Note:
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    '''
    # Loop: iterate over all (k, v) pairs in the dictionary
    return [k for k, v in d.items() if sum(v) > 0]

# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]