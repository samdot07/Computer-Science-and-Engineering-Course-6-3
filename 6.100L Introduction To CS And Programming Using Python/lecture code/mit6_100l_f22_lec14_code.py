#########################################
########### YOU TRY IT ##################
#########################################
def find_grades(grades, students):
    ''' 
    - grades is a dict mapping student names (str) to grades (str) students is a list of student names.
    ---
    #### Returns: 
        list containing the grades for students (in the same order).
    '''
    # Iterate through each key-value pair in the dictionary 'grades'
    return [v for k, v in grades.items() if k in students]

d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']

#########################################

def find_in_L(Ld, k):
    ''' 
    - L is a list of dicts.
    - k is an int.
    ---
    #### Returns: 
        True if k is a key in any dicts of L and False otherwise.
    '''
    # Iterate through each dict pair in the list
    return any(k in d for d in Ld)

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}

print(find_in_L([d1, d2, d3], 2))  # returns True
print(find_in_L([d1, d2, d3], 25))  # returns False

#########################################

def count_matches(d):
    '''
    - d is a dict.
    #### Returns: 
        how many entries in d have the key equal to its value.
    '''
    count = 0
    
    # Iterate through each key-value pair in the dictionary 'd'
    for k, v in d.items():
        if k == v:
            count += 1
    
    return count

d = {1:2, 3:4, 5:6}
print(count_matches(d))   # prints 0

d = {1:2, 'a':'a', 5:5}
print(count_matches(d))   # prints 2

#########################################
################ AT HOME ################
#########################################

def is_inverse(d1, d2):
    ''' 
    - d1 and d2 are dicts.
    ---
    #### Returns: 
        True if d1's keys are values in d2 and d1's values are keys in d2.
    ---
    #### Note:
    Assume values of d1 and d2 are unique and immutable.
    '''
    
    # Iterate through each key-value pair in the dictionary 'd1'
    for k1, v1 in d1.items():
        if k1 not in d2.values() or v1 not in d2.keys():
            return False
    
    # Iterate through each key-value pair in the dictionary 'd2'
    for k2, v2 in d2.items():
        if k2 not in d1.values() or v2 not in d1.keys():
            return False
    
    return True

d1 = {1:2, 3:4}
d2 = {2:1, 4:3}
print(is_inverse(d1, d2))  # prints True

d1 = {1:2, 3:4}
d2 = {2:1, 4:3, 5:6}
print(is_inverse(d1, d2))  # prints False
 
d1 = {1:2, 3:4}
d2 = {1:2, 2:1}
print(is_inverse(d1, d2))  # prints False

#########################################

def add_to_d(d, L):
    ''' 
    - d is a dict.
    - L is a list of tuples.
    ---
    #### Returns:
        None.
    ---
    #### Note:
    Mutates d with new entries whose key is the first element of a tuple in L and the associated value is the second element of a tuple in L.\n
    If the key is already in d, do nothing to its value.\n
    If the key cannot be added, raise a ValueError. 
    '''
    # Iterate through each tuple in the list
    for t in L:
        try:
            if t[0] not in d:
                d.update({t})
        
        except:
            raise ValueError('Key cannot be added')
    
d = {}
L = [(1,2), (3,4)]
add_to_d(d, L)
print(d)   # d is mutated to be {1: 2, 3: 4}

d = {1:1}
L = [(1,2), (3,4)]
add_to_d(d, L)
print(d)   # d is mutated to be {1: 1, 3: 4}

d = {1:1}
L = [(3,4), ([1,2,3], 5)]
add_to_d(d, L)   
# raises a ValueError because its trying to add a list (mutable obj) as key