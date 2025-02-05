#########################################
########### YOU TRY IT ##################
#########################################
# Write a function that meets the specification:
def make_ordered_list(n):
    ''' 
    - n is a positive int.
    ---
    #### Returns:
        a list containing all ints in order from 0 
        to n (inclusive).
    '''
    list1 = []
    
    # Loop: iterate over numbers from 0 to n (inclusive)
    for x in range(n+1):
        list1.append(x)
    
    return list1

print(make_ordered_list(6))  # prints [0, 1, 2, 3, 4, 5, 6]

#########################################
def remove_elem(L, e):
    ''' 
    - L is a list.
    ---
    #### Returns:
        a new list with elements in the same order as L
        but without any elements equal to e. 
    '''
    # Loop: loop as long as e is in the list
    while e in L:
        L.remove(e)
    
    return L

L = [1,2,2,2]
print(remove_elem(L, 2))    # prints [1]
L = [1,2,2,2]
print(remove_elem(L, 1))    # prints [2,2,2]
L = [1,2,2,2]
print(remove_elem(L, 0))    # prints [1,2,2,2]

#########################################
# Write a function that meets this specification
def count_words(sen):
    ''' 
    - sen is a string representing a sentence.
    ---
    #### Returns:
        how many words are in sen (i.e. a word is a 
        sequence of characters between spaces). 
    '''
    ss = sen.split(' ')
    
    return len(ss)

s = "Hello it's me"
print(count_words(s))   # prints 3

s = "I just took a DNA test turns out I'm 100% splitting strings"
print(count_words(s))   # prints 12

#########################################
# Write a function that meets this specification
def sort_words(sen):
    ''' 
    - sen is a string representing a sentence.
    ---
    #### Returns:
        a list containing all the words in sen but
        sorted in alphabetical order. 
    '''
    l = sen.split(' ')
    
    return sorted(l)

#########################################
################ AT HOME ################
#########################################
def apply_to_each(L, f):
    ''' 
    - L is a list of numbers .
    - f is a list that takes in a number and returns a number.
    ---
    Mutate L such that you apply function f to every element in L .
    '''
    # Loop: iterate over each index in the list
    for e in range(len(L)):
        L[e] = f(L[e])
    
test = [1,-2,3]
apply_to_each(test, lambda x: x**2)
print(test)   # prints [1,4,9]

test = [-7, 8, 5, -8, -3]
apply_to_each(test, abs)
print(test)   # prints [7, 8, 5, 8, 3]