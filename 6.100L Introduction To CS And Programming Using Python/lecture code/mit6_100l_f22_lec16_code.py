#########################################
########### YOU TRY IT ##################
#########################################
# Modify the code we wrote to return the total length 
# of all strings inside L: 
def total_len_recur(L):
    if len(L) == 1:
        return len(L[0])
    
    else:
        # Recursion: add the length of the first item to the result of the rest
        return len(L[0]) + total_len_recur(L[1:])
    
test = ["ab", "c", "defgh"]
print(total_len_recur(test)) # should print 8

#########################################
# Write a recursive function according to the specs below
def in_list_of_lists(L, e):
    '''
    - L: list, whose elements are lists containing ints.
    ---
    #### Returns: 
        True if e is an element within the lists of L and False otherwise.
    '''
    if len(L) == 1:
        return e in L[0]
    
    else:
        if e in L[0]:
            return True
        
        else:
            # Recursion: check the rest of the lists for the element
            return in_list_of_lists(L[1:], e)

test = [[1,2], [3,4], [5,6,7]]
print(in_list_of_lists(test, 0)) # prints False
test = [[1,2], [3,4], [5,6,7]]
print(in_list_of_lists(test, 3)) # prints True

#########################################
################ AT HOME ################
#########################################
# Q1. Memorize the code to find possible scores in basketball
def score_count(x, d):
    if x in d:
        return d[x]
    
    # Recursion: sum the scores for x-1, x-2, and x-3, and store the result
    score = score_count(x-1, d) + score_count(x-2, d) + score_count(x-3, d)
    d[x] = score
    return score
    
d = {1:1, 2:2, 3:3}
print(score_count(4, d))  # prints 6
print(score_count(6, d))  # prints 20
print(score_count(13, d))  # prints 1431

#########################################
# Q2. 
def in_list_of_lists_mod(L, e):
    '''
    - L is a list whose elements are either:
        - lists containing ints.
        - ints.
    ---
    #### Returns: 
        True if e is an element within L or sublists of L and False otherwise. 
    '''
    if len(L) == 1:
        if isinstance(L[0], list):
            return e in L
        
        # Recursive call for nested lists
        return in_list_of_lists_mod(L[0], e)
    
    # Recursion: check if the element is in the first part, otherwise check the rest
    if type(L[0])!=list and e==L[0] or type(L[0])==list and e in L[0]:
        return True
    
    return in_list_of_lists_mod(L[1:], e)

test = [[1,2],3,4,5,6,7]
print(in_list_of_lists_mod(test, 3))  # prints True
test = [[1,2],[3,4,5],6,7]
print(in_list_of_lists_mod(test, 3))  # prints True
test = [[1,2],[3,4,5],6,7]
print(in_list_of_lists_mod(test, 10))  # prints False

#########################################
# Q3. 
def my_deepcopy(L):
    ''' 
    - L: list, containing lists or list of lists, etc.
    ---
    #### Returns: 
        a new list with the same structure as L that 
        contains copies (recursively) of every sublist.
    '''
    if not L:
        return []
    
    # Recursion: if the element is a list, deepcopy it, otherwise just copy it
    if not isinstance(L[0], list):
        return [L[0]] + my_deepcopy(L[1:])
    
    return [my_deepcopy(L[0])] + my_deepcopy(L[1:])

myL = ["abc", ['d'], ['e', ['f', 'g']]]
my_newL = my_deepcopy(myL)
print(myL)
print(my_newL)
myL[2][1][0] = 1
print(myL)      # should be ['abc', ['d'], ['e', [1, 'g']]]
print(my_newL)  # should be ['abc', ['d'], ['e', ['f', 'g']]]

#########################################
# Q4. Here are 3 recursive functions that are incorrectly implemented.
# Debug them to have them do what the specs say.
def f(L):
    ''' 
    - L is a non-empty list of lowercase letters.
    ---
    #### Returns:
    the letter earliest in the alphabet. 
    '''
    if len(L) == 1:
        return L[0]
   
    else:
        # Recursion: compare the first letter to the result of the rest of the list
        if L[0] < f((L[1:])):
            return L[0]
        
        else:
            return f(L[1:])
        
print(f(['z', 'a', 'b', 'c', 'd']))  # should print 'a'

#########################################
def g(L, e):
    ''' 
    - L is list of ints.
    - e is an int.
    ---
    #### Returns:
    a count of how many times e occurrs in L.
    '''
    if len(L) == 0:
        return 0
    
    elif len(L) == 1:
        if e == L[0]:
            return 1
        
        else:
            return 0
    
    else:
        # Recursion: if first element equals e, count it, otherwise skip it
        if L[0] == e:
            return 1 + g(L[1:], e)
        
        else:
            return g(L[1:], e)
    
print(g([1,2,3,1], 1))     # should print 2
print(g([1,1,2,3,1,1], 1)) # should print 4

#########################################
def h(L, e):
    ''' 
    - L is list. 
    - e is an int.
    ---
    #### Returns:
        a count of how many times e occurrs in L or (recursively) any sublist of L.
    '''
    if len(L) == 0:
        return 0
    
    else:
        if type(L[0]) == int:
            # Recursion: check first element or recurse into sublist
            if L[0] == e:
                return 1 + h(L[1:], e)
            
            else:
                return h(L[1:], e)
        
        elif type(L[0]) == list:
            # Recursively search the sublist
            if e in L[0]:
                return h(L[0], e) + h(L[1:], e)
            
            else:
                return h(L[1:], e)
    
print(h([1,2,[3],1], 1))        # should print 2
print(h([1,2,[3,1,[1,[1]]]], 1))  # should print 4