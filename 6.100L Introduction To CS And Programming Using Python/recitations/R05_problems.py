# Problem 1: Given a list of numbers. Write a function to turn every item of 
# a list into its square.
def square_list(my_list):
    '''
    - my_list: list, list of numbers.
    ---
    #### Return:
        list, list with the squared values of the original elements.
    '''
    # Loop: iterate over each index in the list
    for e in range(len(my_list)):
        my_list[e] = my_list[e] ** 2
    
    return my_list

# # test
print(square_list([1, 2, 3, 4])) # prints [1, 4, 9, 16]
print(square_list([10, 12, 13])) # prints [100, 144, 169]

#########################################
# Problem 2: Write a Python program to concatenate element-wise 
# three given lists of same length
# Original lists:
list1 = ['0', '1', '2', '3', '4']
list2 = ['red', 'green', 'black', 'blue', 'white']
list3 = ['100', '200', '300', '400', '500']

# Expected output : ['0red100', '1green200', '2black300', '3blue400', '4white500']
def concatenate_lists(l1, l2, l3):
    '''
    - l1: list, first list containing elements to be concatenated.
    - l2: list, second list containing elements to be concatenated.
    - l3: list, third list containing elements to be concatenated.
    ---
    #### Return:
        list, new list where each element is the sum of corresponding elements 
            from l1, l2, and l3.
    '''
    new_list = []
    
    # Lopp: iterate over each index in the first list
    for e in range(len(l1)):
        new_list.append(l1[e] + l2[e] + l3[e])
    
    return new_list

print(concatenate_lists(list1, list2, list3))

#########################################
# Problem 3: Write a function to shift a given list to the right or left 
# direction by a specified amount. Direction, rotation amount, and a 
# list of integers should be inputs to the function.
# e.g. 
# Input list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Rotate the input list in left direction by 2:
# [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
# Rotate the input list in Right direction by 4:
# [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
# edit this to be "right" or "left"
direction = 'right'

def rotate_list(input_list, direction, shift):
    '''
    - input_list: list, to rotate.
    - direction: string, direction which to rotate the list.
    - shift: int, number of elements to shift.
    ---
    #### Return:
        list, shiftefd to the right or left direction by a specified amount.
    '''
    shift = shift % len(input_list)
    
    if direction == "right":
        return input_list[-shift:] + input_list[:-shift]
    
    return input_list[shift:] + input_list[:shift]

# test 
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rotate_list(input_list, "right", 14))
# print(rotate_list(input_list, "left", 4))